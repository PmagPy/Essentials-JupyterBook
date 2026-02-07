import plotly.graph_objects as go
import numpy as np
import itertools

def format_miller(h, k, l):
    """Converts indices to standard crystallographic string with overbars."""
    def to_char(n):
        if n < 0:
            return f"{abs(n)}\u0305"
        return str(n)
    return f"[{to_char(h)}{to_char(k)}{to_char(l)}]"

def plot_magnetocrystalline_anisotropy(K1, K2, radius_nm, temperature, cbar_max=None):
    """Plot 3D magnetocrystalline anisotropy energy surface for magnetite.

    Creates an interactive 3D visualization showing the magnetocrystalline
    anisotropy energy as a function of magnetization direction. The energy
    surface is color-coded and includes crystallographic axes for reference.

    Args:
        K1 (float): First magnetocrystalline anisotropy constant (J/m³).
        K2 (float): Second magnetocrystalline anisotropy constant (J/m³).
        radius_nm (float): Grain radius in nanometers.
        temperature (float): Temperature in Kelvin.
        cbar_max (float, optional): Maximum value for colorbar. If None,
            uses the actual maximum energy. Useful for comparing multiple
            plots with consistent color scales.

    Returns:
        tuple: (fig, energy_max) where fig is the Plotly figure object and
            energy_max is the maximum energy barrier value (J).
    """
    exaggeration = 0.6   # Geometric distortion factor
    cube_scale = 1.5     # Reference cube size

    # --- 1. MATH: Energy Surface ---
    phi = np.linspace(0, 2 * np.pi, 100)
    theta = np.linspace(0, np.pi, 100)
    phi, theta = np.meshgrid(phi, theta)

    # Direction Cosines
    a1 = np.sin(theta) * np.cos(phi)
    a2 = np.sin(theta) * np.sin(phi)
    a3 = np.cos(theta)

    # Energy Density (Eq. 4.3)
    term1 = (a1**2 * a2**2) + (a2**2 * a3**2) + (a3**2 * a1**2)
    term2 = a1**2 * a2**2 * a3**2
    E_density = (K1 * term1) + (K2 * term2)

    # Convert to Total Energy (J) and Normalize
    r_particle = radius_nm * 1e-9
    Volume = (4/3) * np.pi * r_particle**3
    E_total = E_density * Volume
    E_norm = E_total - E_total.min()

    # Store actual max for return value
    energy_max = E_norm.max()

    # Use provided cbar_max or calculated energy_max for consistent scaling
    cmax_val = cbar_max if cbar_max is not None else energy_max

    # Map energy to radius (Geometric Scaling) - use cmax_val for consistent comparison
    r_blob = 1.0 + (exaggeration * (E_norm / cmax_val))

    x_blob = r_blob * np.sin(theta) * np.cos(phi)
    y_blob = r_blob * np.sin(theta) * np.sin(phi)
    z_blob = r_blob * np.cos(theta)

    # --- 2. GEOMETRY: The Reference Cube ---
    v_val = 0.6 * cube_scale
    x_cube = [v_val, v_val, -v_val, -v_val, v_val, v_val, -v_val, -v_val]
    y_cube = [v_val, -v_val, -v_val, v_val, v_val, -v_val, -v_val, v_val]
    z_cube = [v_val, v_val, v_val, v_val, -v_val, -v_val, -v_val, -v_val]

    i_ind = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2]
    j_ind = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3]
    k_ind = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6]

    # --- 3. PLOTTING ---
    fig = go.Figure()

    # TRACE 0: Energy Surface
    fig.add_trace(go.Surface(
        z=z_blob, x=x_blob, y=y_blob,
        surfacecolor=E_norm,
        cmin=0,
        cmax=cmax_val,
        colorscale='magma_r',
        colorbar=dict(title='Energy<br>Barrier (J)', len=0.5, thickness=15, x=0.9, exponentformat='e'),
        opacity=1.0,
        hoverinfo='none',
        contours_x=dict(highlight=False), contours_y=dict(highlight=False), contours_z=dict(highlight=False),
        name='Energy'
    ))

    # TRACE 1: Reference Cube
    fig.add_trace(go.Mesh3d(
        x=x_cube, y=y_cube, z=z_cube, i=i_ind, j=j_ind, k=k_ind,
        color='silver', opacity=1, flatshading=True, lighting=dict(ambient=0.5, diffuse=0.8),
        hoverinfo='skip', visible=False, name='Cube'
    ))

    # --- 4. AXIS GENERATION ---
    max_extent = max(1.0 + exaggeration, v_val)
    axis_scale = max_extent + 0.5

    # Hard axes <100> (red, solid)
    hard_axes = [([1,0,0]), ([-1,0,0]), ([0,1,0]), ([0,-1,0]), ([0,0,1]), ([0,0,-1])]
    for vec in hard_axes:
        v = np.array(vec) * axis_scale
        fig.add_trace(go.Scatter3d(x=[0, v[0]], y=[0, v[1]], z=[0, v[2]], mode='lines', line=dict(color='red', width=5), hoverinfo='skip', showlegend=False))
        fig.add_trace(go.Scatter3d(x=[v[0]], y=[v[1]], z=[v[2]], mode='text', text=[f"{format_miller(*vec)}"], textfont=dict(color='red', size=12), hoverinfo='skip', showlegend=False))

    # Easy axes <111> (blue, dashed)
    for x, y, z in itertools.product([1, -1], repeat=3):
        vec = np.array([x, y, z])
        v = (vec / np.linalg.norm(vec)) * axis_scale
        fig.add_trace(go.Scatter3d(x=[0, v[0]], y=[0, v[1]], z=[0, v[2]], mode='lines', line=dict(color='blue', width=4, dash='dash'), hoverinfo='skip', showlegend=False))
        fig.add_trace(go.Scatter3d(x=[v[0]], y=[v[1]], z=[v[2]], mode='text', text=[f"{format_miller(x,y,z)}"], textfont=dict(color='blue', size=11), hoverinfo='skip', showlegend=False))

    # --- 5. LAYOUT ---
    n_traces = len(fig.data)
    vis_energy = [True, False] + [True] * (n_traces - 2)
    vis_cube   = [False, True] + [True] * (n_traces - 2)

    fig.update_layout(
        width=650, height=470,
        margin=dict(r=180, b=0, l=10, t=0),
        title=dict(text=f'Magnetocrystalline anisotropy (equant grain, diameter = {radius_nm*2} nm; temp = {temperature} K)', x=0.0, y=0.99, font=dict(size=13)),
        hovermode=False,
        updatemenus=[dict(
            type="buttons", direction="left", x=0.5, xanchor="center", y=0.0, yanchor="top",
            bgcolor="rgba(255, 255, 255, 0.9)",
            pad=dict(t=0, b=2, l=0, r=0),
            font=dict(size=11),
            buttons=list([
                dict(label="Energy Landscape", method="update",
                     args=[{"visible": vis_energy}, {"title": f"Magnetite Energy Surface (equant grain, diameter = {radius_nm*2} nm; temperature = {temperature} K)"}]),
                dict(label="Crystal Geometry", method="update",
                     args=[{"visible": vis_cube}, {"title": f"Physical Crystal Shape (equant grain, diameter = {radius_nm*2} nm)"}]),
            ]),
        )],
        scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
            aspectmode='data', camera=dict(eye=dict(x=1.2, y=0.6, z=0.9)), dragmode='orbit'),
    )

    return fig, energy_max

# --- Generate visualization at 300 K ---
fig_300K, energy_max = plot_magnetocrystalline_anisotropy(
    K1=-1.35e4,  # J/m³
    K2=-0.44e4,  # J/m³
    radius_nm=25,
    temperature=300
)
fig_300K.show()

# --- Generate visualization at isotropic point (130 K) ---
fig_130K, _ = plot_magnetocrystalline_anisotropy(
    K1=0.0,      # At isotropic point
    K2=-0.44e4,  # J/m³ (approximately same as 300 K)
    radius_nm=25,
    temperature=130,
    cbar_max=energy_max  # Use same colorbar scale as 300 K for comparison
)
fig_130K.show()
