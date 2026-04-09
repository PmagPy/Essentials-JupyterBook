import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def unit_vector_from_dec_inc(dec_deg: float, inc_deg: float) -> np.ndarray:
    """Convert declination/inclination to a Cartesian unit vector.

    Parameters
    ----------
    dec_deg : float
        Declination in degrees.
    inc_deg : float
        Inclination in degrees.

    Returns
    -------
    np.ndarray
        Cartesian unit vector with shape (3,) in North-East-Down coordinates.
    """
    dec = np.deg2rad(dec_deg)
    inc = np.deg2rad(inc_deg)

    north = np.cos(inc) * np.cos(dec)
    east = np.cos(inc) * np.sin(dec)
    down = np.sin(inc)

    return np.array([north, east, down], dtype=float)


def sample_fisher_like_cluster(
    mean_vector: np.ndarray,
    n: int,
    angular_std_deg: float,
    rng: np.random.Generator,
) -> np.ndarray:
    """Generate a tightly clustered directional population around a mean vector.

    This is not an exact Fisher sampler. It builds a small isotropic Gaussian
    cloud around the mean vector in Cartesian space and re-normalizes to the
    unit sphere, which is adequate for visualization.

    Parameters
    ----------
    mean_vector : np.ndarray
        Mean direction as a unit vector with shape (3,).
    n : int
        Number of directions to generate.
    angular_std_deg : float
        Controls angular dispersion of the cluster.
    rng : np.random.Generator
        Random number generator.

    Returns
    -------
    np.ndarray
        Array of shape (n, 3) containing unit vectors.
    """
    mean_vector = np.asarray(mean_vector, dtype=float)
    mean_vector = mean_vector / np.linalg.norm(mean_vector)

    sigma = np.deg2rad(angular_std_deg)

    cloud = mean_vector + rng.normal(scale=sigma, size=(n, 3))
    # Scale to approximately unit length with some radial scatter
    # so the cluster fills a 3D volume rather than a thin shell.
    norms = np.linalg.norm(cloud, axis=1)[:, None]
    radial_scatter = rng.normal(loc=1.0, scale=0.06, size=(n, 1))
    cloud = cloud / norms * radial_scatter

    return cloud


def orientation_matrix(vectors: np.ndarray) -> np.ndarray:
    """Compute the orientation matrix from unit vectors.

    Parameters
    ----------
    vectors : np.ndarray
        Array of shape (n, 3) containing unit vectors.

    Returns
    -------
    np.ndarray
        Orientation matrix of shape (3, 3).
    """
    return vectors.T @ vectors


def principal_eigenvector(vectors: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return eigenvalues and the principal eigenvector of the orientation matrix.

    Parameters
    ----------
    vectors : np.ndarray
        Array of shape (n, 3) containing unit vectors.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Eigenvalues in descending order and corresponding principal eigenvector.
    """
    t_mat = orientation_matrix(vectors)
    evals, evecs = np.linalg.eigh(t_mat)

    order = np.argsort(evals)[::-1]
    evals = evals[order]
    evecs = evecs[:, order]

    v1 = evecs[:, 0]

    return evals, v1


def draw_spheres(
    ax: plt.Axes,
    centers: np.ndarray,
    radius: float = 0.04,
    color: str = "#4a90d9",
    resolution: int = 8,
) -> None:
    """Draw shaded spheres at each center point.

    Parameters
    ----------
    ax : plt.Axes
        Matplotlib 3D axes.
    centers : np.ndarray
        Array of shape (n, 3) with sphere center coordinates.
    radius : float
        Sphere radius.
    color : str
        Face color.
    resolution : int
        Number of grid points for the sphere mesh.
    """
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)
    sx = radius * np.outer(np.cos(u), np.sin(v))
    sy = radius * np.outer(np.sin(u), np.sin(v))
    sz = radius * np.outer(np.ones_like(u), np.cos(v))

    for c in centers:
        ax.plot_surface(
            sx + c[0], sy + c[1], sz + c[2],
            color=color, shade=True, alpha=0.85,
            lightsource=plt.matplotlib.colors.LightSource(azdeg=315, altdeg=45),
        )


def set_equal_axes(ax: plt.Axes) -> None:
    """Force equal scaling on 3D axes.

    Parameters
    ----------
    ax : plt.Axes
        Matplotlib 3D axes.
    """
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    y_range = abs(y_limits[1] - y_limits[0])
    z_range = abs(z_limits[1] - z_limits[0])

    x_middle = np.mean(x_limits)
    y_middle = np.mean(y_limits)
    z_middle = np.mean(z_limits)

    radius = 0.4 * max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - radius, x_middle + radius])
    ax.set_ylim3d([y_middle - radius, y_middle + radius])
    ax.set_zlim3d([z_middle - radius, z_middle + radius])


def plot_axes(ax: plt.Axes, length: float = 1.2) -> None:
    """Plot North-East-Down coordinate axes.

    Parameters
    ----------
    ax : plt.Axes
        Matplotlib 3D axes.
    length : float, optional
        Axis half-length.
    """
    ax.plot(
        [-length, length],
        [0, 0],
        [0, 0],
        color="black",
        lw=1.5,
        ls="--",
    )
    ax.plot(
        [0, 0],
        [-length, length],
        [0, 0],
        color="black",
        lw=1.5,
        ls="--",
    )
    ax.plot(
        [0, 0],
        [0, 0],
        [-length, length],
        color="black",
        lw=1.5,
        ls="--",
    )

    ax.text(length + 0.08, 0, 0, "North", fontsize=16)
    ax.text(0, length + 0.08, 0, "East", fontsize=16)
    ax.text(0, 0, length + 0.08, "Down", fontsize=16)


def make_figure(vectors, mean_dir, outpath, title=""):
    """Create a single eigenvector figure and save it.

    Parameters
    ----------
    vectors : np.ndarray
        Array of shape (n, 3) with data vectors.
    mean_dir : np.ndarray
        Mean direction unit vector (used to orient V1 sign).
    outpath : str
        Output file path.
    title : str, optional
        Figure title.
    """
    evals, v1 = principal_eigenvector(vectors)

    # Fix sign so V1 points toward the same hemisphere as cluster_1.
    if np.dot(v1, mean_dir) < 0:
        v1 = -v1

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_position([0, 0, 1, 1])

    draw_spheres(ax, vectors, radius=0.04, color="#d9534f")

    plot_axes(ax, length=1.25)

    # Plot principal eigenvector as a solid axis through the origin.
    line_len = 1.35
    line_pts = np.vstack([-line_len * v1, line_len * v1])
    ax.plot(
        line_pts[:, 0],
        line_pts[:, 1],
        line_pts[:, 2],
        color="black",
        lw=4,
    )

    ax.text(
        1.42 * v1[0],
        1.42 * v1[1],
        1.42 * v1[2] + 0.12,
        r"$\mathbf{V}_1$",
        fontsize=18,
    )

    ax.set_axis_off()
    set_equal_axes(ax)
    ax.view_init(elev=18, azim=-50)

    print(f"{title}")
    print(f"  Eigenvalues: {evals}")
    print(f"  Principal eigenvector V1: {v1}")

    fig.savefig(outpath, dpi=300, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)

    # Autocrop white space from the saved image.
    img = Image.open(outpath)
    arr = np.array(img)
    bg = arr[0, 0]
    mask = np.any(arr != bg, axis=2)
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    if rows.any() and cols.any():
        rmin, rmax = np.where(rows)[0][[0, -1]]
        cmin, cmax = np.where(cols)[0][[0, -1]]
        margin = 20
        crop_box = (
            max(cmin - margin, 0),
            max(rmin - margin, 0),
            min(cmax + margin, arr.shape[1]),
            min(rmax + margin, arr.shape[0]),
        )
        img.crop(crop_box).save(outpath)

    print(f"  Saved to {outpath}")


def main() -> None:
    """Create unit-vector and full-vector versions of the eigenvector figure."""
    rng = np.random.default_rng(42)

    mean_dir = unit_vector_from_dec_inc(dec_deg=210, inc_deg=40)
    antipode = -mean_dir

    # --- Unit-vector version (directions on the unit sphere) ---
    cluster_1_unit = sample_fisher_like_cluster(
        mean_vector=mean_dir,
        n=350,
        angular_std_deg=12,
        rng=rng,
    )
    # Renormalize to exact unit length (undo radial scatter)
    cluster_1_unit /= np.linalg.norm(cluster_1_unit, axis=1)[:, None]

    cluster_2_unit = sample_fisher_like_cluster(
        mean_vector=antipode,
        n=350,
        angular_std_deg=12,
        rng=rng,
    )
    cluster_2_unit /= np.linalg.norm(cluster_2_unit, axis=1)[:, None]

    vectors_unit = np.vstack([cluster_1_unit, cluster_2_unit])

    make_figure(
        vectors_unit,
        mean_dir,
        "book/figures/chapter12/eigenvector_unit.png",
        title="Unit vectors",
    )

    # --- Full-vector version (with intensity variation) ---
    rng2 = np.random.default_rng(42)

    cluster_1_full = sample_fisher_like_cluster(
        mean_vector=mean_dir,
        n=350,
        angular_std_deg=12,
        rng=rng2,
    )
    cluster_2_full = sample_fisher_like_cluster(
        mean_vector=antipode,
        n=350,
        angular_std_deg=12,
        rng=rng2,
    )

    vectors_full = np.vstack([cluster_1_full, cluster_2_full])

    make_figure(
        vectors_full,
        mean_dir,
        "book/figures/chapter12/eigenvector.png",
        title="Full vectors (with intensity variation)",
    )


if __name__ == "__main__":
    main()