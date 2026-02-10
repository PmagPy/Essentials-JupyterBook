---
title: "Chapter 4: Magnetic Anisotropy and Domains"
label: chap:anisotropy
numbering:
  enumerator: 4.%s
kernelspec:
  name: python3
  display_name: Python 3
---

Rocks often contain assemblages of ferromagnetic minerals dispersed within a matrix of diamagnetic and paramagnetic minerals. In later chapters, we will be concerned with the magnetization of these assemblages, but here we continue our investigation of the behavior of individual particles.
In Chapter 3, we learned that in some crystals electronic spins work in concert to create a spontaneous magnetization that remains in the absence of an external field. The basis of paleomagnetism is that these ferromagnetic particles carry the record of ancient magnetic fields. What allows the magnetic moments to come into equilibrium with the geomagnetic field and then what fixes that equilibrium magnetization into the rock so that we may measure it millions or even billions of years later? We will begin to answer these questions over the next few chapters.

We will start with the second part of the question: what fixes magnetizations in particular directions? A basic principle is that ferromagnetic particles have various contributions to the magnetic energy which controls their magnetization. No matter how simple or complex the combination of energies may become, the grain will seek the configuration of magnetization which minimizes its total energy. The short answer to our question is that certain directions within magnetic crystals are at lower energy than others. To shift the magnetization from one "easy" direction to another requires energy. If the barrier is high enough, the particle will stay magnetized in the same direction for a very long time—say, billions of years. In this chapter, we will address the causes and some of the consequences of these energy barriers for the magnetization of rocks. Note that in this chapter we will be dealing primarily with energy densities (volume normalized energies) as opposed to energy. We will distinguish the two by the convention that energies are given with the symbol $E$ and energy densities with $\epsilon$.

In Chapter 6, we will discuss the behavior of common magnetic minerals, but to develop the general theory, it is easiest to focus on a single mineral. We choose here magnetite [](#fig:magnetite), as it has a simple cubic structure and has been the subject of intensive study. However, we will occasionally introduce concepts appropriate for other magnetic minerals when it will be informative.

:::{figure} ../figures/chapter4/magnetite.png
:name: fig:magnetite
:width: 100%

a) A magnetite octahedron. [Photo of Lou Perloff in The Photo-Atlas of Minerals.] b) Internal crystal structure. Directions of the body diagonal ([111] direction) and orthogonal to the cubic faces ([001] direction) are shown as arrows. Big red dots are the oxygen anions. The blue dots are iron cations in octahedral coordination and the yellow dots are in tetrahedral coordination. Fe$^{3+}$ sits on the A sites and Fe$^{2+}$ and Fe$^{3+}$ sit on the B sites. c) Magnetocrystalline anisotropy energy as a function of direction within a magnetite crystal at room temperature. The easiest direction to magnetize (the direction with the lowest energy — note dimples in energy surface) is along the body diagonal (the [111] direction). [Figure from {cite}`williams1995`.]
:::

The simplest permanently magnetized particles are uniformly magnetized and are called *single domain* (SD). It is only in the smallest grains that such parallel alignment of spins is the lowest energy state. As particles get larger, the energy landscape changes and energy is minimized by spins curling around within a grain to form a vortex. This vortex state can be stable and long-lived and have behavior similar to single-domain grains which has led to such grains being referred to as *pseudo-single domain* (PSD). In grains that are larger still, spins organize themselves into regions with quasi-uniform magnetization (magnetic domains) separated by domain walls and are called *multi-domain* (MD) particles. These more complicated spin structures are challenging to model and most paleomagnetic theory is based on single domain behavior. Therefore, we begin with a discussion of the energies of uniformly magnetized (single-domain) particles.

## The magnetic energy of particles

(sect:exchange)=
### Exchange energy

We learned in Chapter 3 that some crystalline states are capable of ferromagnetic behavior because of quantum mechanical considerations. Electrons in neighboring orbitals in certain crystals "know" about each other's spin states. In order to avoid sharing the same orbital with the same spin (hence having the same quantum numbers — not allowed by Pauli's exclusion principle), electronic spins in such crystals act in a coordinated fashion. They will be either aligned parallel or antiparallel according to the details of the interaction. This *exchange energy density* ($\epsilon_e$) is the source of spontaneous magnetization and is given for a pair of spins by:

$$
\epsilon_e = -2J_e \mathbf{S}_i \cdot \mathbf{S}_j,
$$

where $J_e$ is the *exchange integral* and $\mathbf{S}_i$ and $\mathbf{S}_j$ are spin vectors. Depending on the details of the crystal structure (which determines the size and sign of the exchange integral), exchange energy is at a minimum when electronic spins are aligned parallel or anti-parallel.

We define here a parameter that we will use later: the *exchange constant* $A=J_eS^2/a$ where $a$ is the interatomic spacing. $A$ = 1.33 × 10$^{-11}$ Jm$^{-1}$ for magnetite, a common magnetic mineral.

Recalling the discussion in Chapter 3, while $s$ orbitals are spherical, the $3d$ electronic orbitals "poke" in certain directions. Hence spins in some directions within crystals will be easier to coordinate than in others. We can illustrate this using the example of magnetite, a common magnetic mineral ([](#fig:magnetite)a).
Magnetite octahedra ([](#fig:magnetite)a), when viewed at the atomic level ([](#fig:magnetite)b) are composed of one ferrous (Fe$^{2+}$) cation, two ferric (Fe$^{3+}$) cations and four O$^{2-}$ anions. Each oxygen anion shares an electron with two neighboring cations in a covalent bond.

In Chapter 3, we mentioned that in some crystals, spins are aligned anti-parallel, yet there is still a net magnetization, a phenomenon we called ferrimagnetism. This can arise from the fact that not all cations have the same number of unpaired spins. Magnetite, with its ferrous (4 $m_b$) and ferric (5 $m_b$) states is a good example. There are three iron cations in a magnetite crystal giving a total of 14 $m_b$ to play with. Magnetite is very magnetic, but not that magnetic! From [](#fig:magnetite)b we see that the ferric ions all sit on the tetrahedral (A) lattice sites and there are equal numbers of ferrous and ferric ions sitting on the octahedral (B) lattice sites. The unpaired spins of the cations in the A and B lattice sites are aligned anti-parallel to one another because of superexchange (Chapter 3) so we have 9 $m_b$ on the B sites minus 5 $m_b$ on the A sites for a total of 4 $m_b$ per unit cell of magnetite.

### Magnetic moments and external fields

We know from experience that there are energies associated with magnetic fields. Just as a mass has a potential energy when it is placed in the gravitational field of another mass, a magnetic moment has an energy when it is placed in a magnetic field. This energy has many names (magnetic energy, magnetostatic energy, Zeeman energy, etc.). Here we will work with the volume normalized *magnetostatic interaction energy density* ($\epsilon_m$). This energy density essentially represents the interaction between the magnetic lines of flux and the magnetic moments of the electronic spins. It is energy that aligns magnetic compass needles with the ambient magnetic field. We find the volume-normalized form (in units of J m$^{-3}$) by noting that magnetization is moment per unit volume, $\mathbf{M} = \mathbf{m}/v$ (see Chapter 1)::

$$
\epsilon_m = - \mathbf{M} \cdot \mathbf{B}.
$$ (eq:Em1)

$\epsilon_m$ is at a minimum when $\mathbf{M}$ is aligned with $\mathbf{B}$, so the magnetostatic energy acts to rotate the magnetization toward the applied field. Single-domain particles have a quasi-uniform magnetization and the application of a magnetic field does not change the net magnetization, which remains at saturation ($M_s$). Although the magnetostatic energy favors alignment with the applied field, the magnetizations in many particles do not rotate freely (or we would not have paleomagnetism!). There is another contribution to the energy of the magnetic particle associated with the magnetic crystal itself. This energy depends on the direction of magnetization in the crystal — it is anisotropic — and is called *anisotropy energy*. Anisotropy energy creates barriers to free rotation of the magnetization within the magnetic crystal, which lead to energetically preferred directions for the magnetization within individual single-domain grains.

There are many causes of anisotropy energy. The most important ones derive from the details of crystal structure *(magnetocrystalline anisotropy energy)*, the state of stress within the particle *(magnetostriction)*, and the shape of the particle, *(shape anisotropy)*. We will consider these briefly in the following subsections.

### Magnetocrystalline anisotropy energy
(sect:K1)=

For equant single-domain particles or particles with low saturation magnetizations, the crystal structure dominates the magnetic energy. The so-called *easy directions* of magnetization are crystallographic directions along which magnetocrystalline energy is at a minimum.

For a cubic crystal like magnetite at room temperature, the magnetocrystalline anisotropy energy density is expressed in terms of the direction cosines $\alpha_1, \alpha_2, \alpha_3$ — the cosines of the angles between the magnetization direction and the crystallographic axes [100], [010], [001] (see Appendix for review of direction cosines):

$$
\epsilon_a = K_1(\alpha_1^2 \alpha_2^2 + \alpha_2^2\alpha^2_3 + \alpha_3^2\alpha_1^2) + K_2\alpha_1^2\alpha_2^2\alpha_3^2,
$$ (eq:xtalline)

where $K_1$ and $K_2$ are empirically determined *magnetocrystalline anisotropy constants* with units of Jm$^{-3}$ (so $\epsilon_a$ is an energy density). Magnetite (cubic above 120 K) has $K_1$ = −1.35 × 10$^4$ Jm$^{-3}$ at room temperature. The result of this equation with these constants is that the easy directions are along the [111] body diagonals and the hard directions are along [100]. The **interactive visualization below** lets you explore this energy surface in 3D: the bulges along the hard [100] directions (red axes) and the dimples along the easy [111] directions (blue dashed axes) are a direct result of of [](#eq:xtalline). The energy is minimized along the [111] body diagonals with energy barriers between them due to the hard directions. Toggle between "Energy Landscape" and "Crystal Geometry" to compare the energy surface with the physical cubic crystal geometry.

```{code-cell} python
:tags: [remove-input]

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
```

As a consequence of the magnetocrystalline anisotropy energy, once the magnetization is aligned with an easy direction, work must be done to change it. In order to switch from one easy axis to another (e.g. from one direction along the body diagonal to the opposite for cubic magnetite), the magnetization has to traverse a path over an energy barrier which is the difference between the energy in the easy direction and that in the intervening hard direction. In the case of magnetite at room temperature, this energy barrier is $\epsilon_{[110]}-\epsilon_{[111]} = K_1/4 - K_1/3 = -K_1/12 = |K_1|/12$ (for $K_1<0$)

#### Temperature dependence of anisotropy

Because electronic interactions depend heavily on interatomic spacing, magnetocrystalline anisotropy constants are a strong function of temperature. The effect of this is dramatic in magnetite with $K_1$ progressively changing until it becomes zero at 130 K — this temperature is known as the *isotropic point* ([](#fig:K-T)). 

:::{note} Temperature Scales in Paleomagnetism
We often use the Kelvin scale when discussing magnetic properties because it is the SI standard for thermodynamic temperature. The conversion from Celsius is straightforward: K = °C + 273.15. Room temperature is commonly approximated as **300 K** (27°C; 80°F). While this is slightly warmer than typical indoor temperatures, the round number simplifies calculations and discussions. Magnetite's isotropic point of **130 K** corresponds to approximately -143°C, very chilly 🥶!
:::

:::{figure} ../figures/chapter4/K-T.png
:name: fig:K-T
:width: 60%

Variation of $K_1$ and $K_2$ of magnetite as a function of temperature. Solid lines are data from {cite}`syono1963`. Dashed lines are data from {cite}`fletcher1974`.
:::

Given that $K_1=0$ at the isotropic point, there is minimal magnetocrystalline anisotropy at 130 K. The large energy barriers that act to keep the magnetizations parallel to the body diagonal are gone and the spins can wander more freely through the crystal. **The interactive visualization below** shows the energy landscape at 130 K, where the anisotropy energy is nearly uniform in all directions.

```{code-cell} python
:tags: [remove-input]

# --- Generate visualization at isotropic point (130 K) ---
fig_130K, _ = plot_magnetocrystalline_anisotropy(
    K1=0.0,      # At isotropic point
    K2=-0.44e4,  # J/m³ (approximately same as 300 K)
    radius_nm=25,
    temperature=130,
    cbar_max=energy_max  # Use same colorbar scale as 300 K for comparison
)
fig_130K.show()
```

The change in magnetocrystalline anisotropy at low temperature can have a profound effect on the magnetization. As temperature decreases from room temperature, $K_1$ passes through zero at about 130 K — the *isotropic point* ($T_i$). Below the isotropic point, the energy barriers rise again, but with a different topology: the cube axes become the energy minima and the body diagonals become the high energy directions — the reverse of the room-temperature situation. At still lower temperature (~120 K), the crystal structure of magnetite distorts from cubic to monoclinic at the *Verwey temperature* ($T_v$). This distortion is driven by charge ordering: above $T_v$, the extra electron shared between Fe²⁺ and Fe³⁺ on the octahedral lattice sites hops rapidly, making the sites equivalent; below $T_v$, the charges localize into an ordered arrangement of Fe²⁺ and Fe³⁺, and the size difference between these ions distorts the lattice.

The combined effect of these transitions on magnetization is illustrated in [](#fig:verwey), which shows the remanence of a sample magnetized to saturation at room temperature, then cooled to low temperature and rewarmed. On cooling, the magnetization progressively decreases through the isotropic point — where the anisotropy momentarily drops to zero and the easy axes switch — and drops further through the Verwey transition where the crystal structure changes. On rewarming, only partial recovery occurs. This is the basis for *low-temperature demagnetization* (LTD). The remanence loss is predominantly a multidomain effect: loosely pinned domain walls reorganize as the anisotropy changes and do not all return to their original positions on rewarming. The portion that survives — the *low-temperature memory* — includes the remanence of single-domain grains (which are largely unaffected by LTD) as well as remanence held by strongly pinned domain walls in larger grains.

:::{figure} ../figures/chapter4/verwey.png
:name: fig:verwey
:width: 50%

The magnetization of magnetite-bearing basaltic dike specimen that was given a saturating isothermal remanent magnetization at room temperature (RTSIRM) before being cooled to 10 K and warmed back up to 300 K. On cooling, the magnetization decreases through the isotropic point (~130 K) and drops sharply at the Verwey transition (~120 K). On rewarming, only partial recovery occurs — the difference is the multidomain remanence lost during LTD. Data from {cite}`swanson-hysell2021` available in the MagIC database https://earthref.org/MagIC/20213.
:::

#### Uniaxial magnetocrystalline anisotropy

Cubic symmetry (as in the case of magnetite) is just one of many types of crystal symmetries. Another important form is uniaxial symmetry which can arise from crystal shape or structure. The energy density for uniaxial magnetic anisotropy is:

$$
\epsilon_a  = K_{u1} \sin^2 \theta + K_{u2} \sin^4 \theta + \ldots
$$ (eq:Ku)

Here the magnetocrystalline constants have been designated $K_{u1}, K_{u2}$ to distinguish them from $K_1, K_2$ used before. When $K_{u1} > 0$, the symmetry axis itself is the easy direction — an *easy axis*. When $K_{u1}$ is negative, the symmetry axis is energetically unfavorable and the magnetization is confined to the plane perpendicular to it — an *easy plane*.

An example of a mineral dominated by uniaxial anisotropy is hematite. The magnetization of hematite is complicated, as we shall learn in Chapters 6 and 7, but one source of magnetization is spin-canting (see Chapter 3) within the basal plane. The uniaxial anisotropy perpendicular to the basal plane is very strong ($K_{u1} < 0$), confining the magnetization to the easy plane. Within the basal plane, the anisotropy is orders of magnitude weaker so the magnetization theoretically wanders fairly freely. In reality, stress anisotropy from defects and internal strain (see next section) pins the magnetization direction within the basal plane much more effectively than magnetocrystalline anisotropy alone would predict.

**The interactive visualization below** demonstrates the energy landscape for hematite's uniaxial anisotropy. The perpendicular anisotropy constant is K₁ = -1.2 × 10⁶ J/m³ {cite}`dunlop1997`, while the in-plane anisotropy is much weaker at 0-13 J/m³ {cite}`martin-hernandez2012`. The energy surface shows high energy along the c-axis (hard direction) and low energy in the basal plane (easy directions).

```{code-cell} python
:tags: [remove-input]

import plotly.graph_objects as go
import numpy as np

def plot_hematite_anisotropy(K1, K3, radius_nm, temperature):
    """Plot 3D hematite magnetocrystalline anisotropy energy surface.

    Creates an interactive 3D visualization showing the energy landscape for
    hematite's uniaxial anisotropy with easy plane behavior.

    Args:
        K1 (float): Perpendicular anisotropy constant (J/m³). Use negative for easy plane.
        K3 (float): In-plane (basal plane) anisotropy constant (J/m³).
        radius_nm (float): Grain radius in nanometers.
        temperature (float): Temperature in Kelvin.

    Returns:
        tuple: (fig, energy_max) - Plotly figure and maximum energy value
    """

    exaggeration = 1.8  # Geometric distortion factor (increased to show energy variations)
    crystal_scale = 2.0   # Reference crystal size (increased for visibility)

    # --- 1. MATH: Energy Surface ---
    phi = np.linspace(0, 2 * np.pi, 100)
    theta = np.linspace(0, np.pi, 100)
    phi_grid, theta_grid = np.meshgrid(phi, theta)

    # Hematite anisotropy energy
    # Hematite is rhombohedral (R3̄c) but conventionally indexed on hexagonal axes
    #
    # K1 = -1.2e6 J/m³: c-axis perpendicular anisotropy (Dunlop & Özdemir 1997, Table 3.1)
    #     Sign convention: negative means easy plane (basal plane is energetically favorable)
    # K3 = 13 J/m³: maximum triaxial in-plane anisotropy (Martín-Hernández & Guerrero-Suárez 2012)
    #     This is ~5 orders of magnitude smaller than |K1|
    #
    # The 6-fold cos(6φ) term reflects the trigonal symmetry of the basal plane
    # projected onto the hexagonal setting
    E_density = K1 * np.sin(theta_grid)**2 + K3 * np.sin(theta_grid)**4 * np.cos(6 * phi_grid)

    # Convert to Total Energy (J) and Normalize
    r_particle = radius_nm * 1e-9
    Volume = (4/3) * np.pi * r_particle**3
    E_total = E_density * Volume
    E_norm = E_total - E_total.min()
    energy_max = E_norm.max()

    # Map energy to radius (Geometric Scaling)
    r_blob = 1.0 + (exaggeration * (E_norm / energy_max))

    x_blob = r_blob * np.sin(theta_grid) * np.cos(phi_grid)
    y_blob = r_blob * np.sin(theta_grid) * np.sin(phi_grid)
    z_blob = r_blob * np.cos(theta_grid)

    # --- 2. GEOMETRY: Hexagonal Plate ---
    # Hematite has rhombohedral symmetry (space group R3̄c) but commonly forms
    # hexagonal plate crystals (platy habit) due to strong easy-plane anisotropy
    # Create hexagonal plate with c-axis vertical (short axis)

    # Scale factor
    r_hex = 0.9 * crystal_scale  # radius of hexagonal plate
    c_height = 0.15 * crystal_scale  # height along c-axis (very short for platy habit)

    # Create 6 vertices for hexagonal outline
    angles_hex = np.linspace(0, 2*np.pi, 7)[:-1]  # 6 vertices, evenly spaced

    x_hex = []
    y_hex = []
    z_hex = []

    # Bottom hexagon (6 vertices)
    for angle in angles_hex:
        x_hex.append(r_hex * np.cos(angle))
        y_hex.append(r_hex * np.sin(angle))
        z_hex.append(-c_height/2)

    # Top hexagon (6 vertices)
    for angle in angles_hex:
        x_hex.append(r_hex * np.cos(angle))
        y_hex.append(r_hex * np.sin(angle))
        z_hex.append(c_height/2)

    # Define triangular faces
    # 12 vertices total: 0-5 bottom hexagon, 6-11 top hexagon
    i_ind = []
    j_ind = []
    k_ind = []

    # Bottom cap (6 triangles forming hexagon)
    for i in range(6):
        i_next = (i + 1) % 6
        i_ind.append(0)
        j_ind.append(i)
        k_ind.append(i_next)

    # Top cap (6 triangles forming hexagon)
    for i in range(6):
        i_next = (i + 1) % 6
        i_ind.append(6)
        j_ind.append(6 + i)
        k_ind.append(6 + i_next)

    # Side faces (12 triangles, 2 per rectangular face)
    for i in range(6):
        i_next = (i + 1) % 6
        # Two triangles per side face
        i_ind.extend([i, i_next])
        j_ind.extend([6+i, 6+i_next])
        k_ind.extend([i_next, 6+i])

    # --- 3. PLOTTING ---
    fig = go.Figure()

    # TRACE 0: Energy Surface
    fig.add_trace(go.Surface(
        z=z_blob, x=x_blob, y=y_blob,
        surfacecolor=E_norm,
        cmin=0,
        colorscale='plasma',
        colorbar=dict(title='Energy<br>Barrier (J)', len=0.5, thickness=15, x=0.9, exponentformat='e'),
        opacity=1.0,
        hoverinfo='none',
        contours_x=dict(highlight=False), contours_y=dict(highlight=False), contours_z=dict(highlight=False),
        name='Energy'
    ))

    # TRACE 1: Hexagonal Plate
    fig.add_trace(go.Mesh3d(
        x=x_hex, y=y_hex, z=z_hex, i=i_ind, j=j_ind, k=k_ind,
        color='lightcoral', opacity=0.9, flatshading=True,
        lighting=dict(ambient=0.5, diffuse=0.8),
        hoverinfo='skip', visible=False, name='Crystal'
    ))

    # --- 4. AXIS GENERATION ---
    max_extent = max(1.0 + exaggeration, r_hex, c_height/2)
    axis_scale = max_extent + 0.3  # Reduced to keep c-axis label visible

    # For hematite: c-axis is hard (red), basal plane is easy (blue)
    hard_color = 'red'
    easy_color = 'blue'

    # Hard axis along z (c-axis)
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[-axis_scale, axis_scale],
                               mode='lines', line=dict(color=hard_color, width=5, dash='dash'),
                               hoverinfo='skip', showlegend=False))
    fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[axis_scale], mode='text',
                               text=['c-axis<br>(hard)'], textfont=dict(color=hard_color, size=12),
                               hoverinfo='skip', showlegend=False))

    # Easy directions in basal plane (6-fold symmetry from hexagonal setting)
    basal_angles = np.linspace(0, 2*np.pi, 6, endpoint=False)
    for angle in basal_angles:
        x_end = axis_scale * 0.7 * np.cos(angle)
        y_end = axis_scale * 0.7 * np.sin(angle)
        fig.add_trace(go.Scatter3d(x=[0, x_end], y=[0, y_end], z=[0, 0],
                                   mode='lines', line=dict(color=easy_color, width=4),
                                   hoverinfo='skip', showlegend=False))

    # --- 5. LAYOUT ---
    n_traces = len(fig.data)
    vis_energy = [True, False] + [True] * (n_traces - 2)
    vis_crystal = [False, True] + [True] * (n_traces - 2)

    # Format anisotropy constants for display
    K1_abs = abs(K1)
    K3_val = K3

    fig.update_layout(
        width=650, height=470,
        margin=dict(r=180, b=0, l=10, t=0),
        title=dict(text=f'Hematite uniaxial anisotropy — easy plane (diameter = {radius_nm*2} nm; temp = {temperature} K)',
                   x=0.0, y=0.99, font=dict(size=13)),
        hovermode=False,
        annotations=[
            dict(
                text=f'K<sub>u1</sub> = {K1_abs:.1e} J/m³ (c-axis, hard); in-plane K₃ ≈ 0–{K3_val:.0f} J/m³',
                xref='paper', yref='paper',
                x=0.5, y=0.06,
                xanchor='center', yanchor='top',
                showarrow=False,
                font=dict(size=10, color='rgba(0,0,0,0.6)'),
                bgcolor='rgba(255,255,255,0.8)',
                borderpad=4
            )
        ],
        updatemenus=[dict(
            type="buttons", direction="left", x=0.5, xanchor="center", y=0.0, yanchor="top",
            bgcolor="rgba(255, 255, 255, 0.9)",
            pad=dict(t=0, b=2, l=0, r=0),
            font=dict(size=11),
            buttons=list([
                dict(label="Energy Landscape", method="update",
                     args=[{"visible": vis_energy},
                           {"title": f"Hematite Energy Surface (diameter = {radius_nm*2} nm; temp = {temperature} K)"}]),
                dict(label="Hematite Crystal", method="update",
                     args=[{"visible": vis_crystal},
                           {"title": f"Hematite Crystal (platy habit, diameter = {radius_nm*2} nm)"}]),
            ]),
        )],
        scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
            aspectmode='data', camera=dict(eye=dict(x=1.8, y=1.0, z=1.3)), dragmode='orbit'),
    )

    return fig, energy_max

# --- Generate hematite visualization ---
# K1 = 1.2e6 J/m³ (Dunlop & Özdemir 1997, Table 3.1)
# Use negative sign for easy plane behavior (sin²θ energy form)
# K3 = 13 J/m³ (Martín-Hernández & Guerrero-Suárez 2012)
fig_hematite, _ = plot_hematite_anisotropy(
    K1=-1.2e6,   # J/m³ (negative for easy plane)
    K3=13,       # J/m³ (in-plane anisotropy)
    radius_nm=200,
    temperature=300
)
fig_hematite.show()
```

### Magnetostriction — stress anisotropy

Exchange energy depends strongly on the details of the physical interaction between orbitals in neighboring atoms with respect to one another, hence changing the positions of these atoms will affect that interaction. Put another way, straining a crystal will alter its magnetic behavior. Similarly, changes in the magnetization can change the shape of the crystal by altering the shapes of the orbitals. This is the phenomenon of *magnetostriction*. The magnetic energy density caused by the application of stress to a crystal can be approximated by:

$$
\epsilon_{\sigma} = \frac{3}{2} \bar{\lambda} \sigma \sin^2 \theta,
$$

where $\bar{\lambda}$ is an experimentally derived constant, $\sigma$ is the stress, and $\theta$ is the angle of the stress with respect to the $c$ crystallographic axis. {cite}`moskowitz1993` measured the magnetostriction constants parallel to [111] and [100] in magnetite and found $\lambda_{111}$ and $\lambda_{100}$ to be $78.2 \times 10^{-6}$ and $-21.8 \times 10^{-6}$, respectively. $\bar{\lambda}$ is given by:

$$
\bar{\lambda} = \frac{2}{5} \lambda_{100} + \frac{3}{5} \lambda_{111},
$$

so $\bar{\lambda}$ for magnetite is about 38 × 10$^{-6}$. Stress has units of Nm$^{-2}$ which have the same fundamental units as Jm$^{-3}$, so $\bar{\lambda}$ is dimensionless. Note the similarity in form of magnetostriction and uniaxial anisotropy giving rise to a single "easy axis" within the crystal.

(sect:shape)=
### Magnetostatic (shape) anisotropy

There is one more important source of magnetic anisotropy: shape. To understand how crystal shape controls magnetic energy, we need to understand the concept of the internal *demagnetizing field* of a magnetized body. In [](#fig:demagfield)a we show the magnetic vectors within a ferromagnetic crystal. These produce a magnetic field external to the crystal that is proportional to the magnetic moment (see Chapter 1). This external field is identical to a field produced by a set of *free poles* distributed over the surface of the crystal ([](#fig:demagfield)b). The surface poles do not just produce the external field, they also produce an internal field shown in [](#fig:demagfield)c. The internal field is known as the *demagnetizing field* ($H_d$). $H_d$ is proportional to the magnetization of the body and is sensitive to the shape. For a simple sphere in [](#fig:demagfield)a and applied field condition shown in [](#fig:demagfield)d, the demagnetizing field is given by:

$$
\mathbf{H}_d = -N \mathbf{M},
$$

where $N$ is a *demagnetizing factor* determined by the shape. In fact, the demagnetizing factor depends on the orientation of $\mathbf{M}$ within the crystal and therefore is a tensor (see Appendix for review of tensors). The more general equation is $\mathbf{H}_d = \mathbf{N} \cdot \mathbf{M}$ where $\mathbf{H}_d$ and $\mathbf{M}$ are vectors and $\mathbf{N}$ is a 3 × 3 tensor. For now, we will simplify things by considering the isotropic case of a sphere in which $\mathbf{N}$ reduces to the single value scalar quantity $N$.

:::{figure} ../figures/chapter4/demagfield.png
:name: fig:demagfield
:width: 100%

a) Internal magnetizations within a ferromagnetic crystal. b) Generation of an identical external field from a series of surface monopoles. c) The internal "demagnetizing" field resulting from the surface monopoles. [Redrawn from {cite}`oreilly1984`.] d) Surface monopoles on a sphere. e) Surface monopoles on an ellipse, with the magnetization parallel to the elongation. f) Demagnetizing field $\mathbf{H}_d$ resulting from magnetization $M$ at angle $\theta$ from $a$ axis in prolate ellipsoid.
:::

For a sphere, the surface poles are distributed over the surface such that there are none at the "equator" and most at the "pole" (see [](#fig:demagfield)d). Potential field theory shows that the external field of a uniformly magnetized body is identical to that of a centered dipole moment of magnitude $m=v M$ (where $v$ is volume). At the equator of the sphere as elsewhere, $\mathbf{H}_d = -N\mathbf{M}$. But the external field at the equator is equal to the demagnetizing field just inside the body because the field is continuous across the body. We can find the equatorial (tangential) demagnetizing field at the equator by substituting in the equatorial colatitude $\theta=90°$ into $H_{\theta}$ from Chapter 1, so:

$$
H_d = -\frac{m}{4\pi r^3}.
$$

Using the fact that magnetization (in units of Am$^{-1}$) is the moment (in units of Am$^2$) per unit volume (in units of m$^3$) and the volume of a sphere is $\frac{4}{3} \pi r^3$, we have:

$$
m=\frac{4}{3} \pi r^3 M,
$$

so substituting and solving for $H_d$ we get $H_d=-\frac{1}{3} M$, hence $N=\frac{1}{3}$.

Different directions within a non-spherical crystal will have different distributions of free poles (see [](#fig:demagfield)e,f). In fact, the surface density of free poles is given by $\sigma_m=\mathbf{M}\cdot \hat{r}$. Because the surface pole density depends on the direction of magnetization, so too will $N$. In the case of a prolate ellipsoid magnetized parallel to the elongation axis $a$ ([](#fig:demagfield)e), the free poles are farther apart than across the grain, hence, intuitively, the demagnetizing field, which depends on $1/r^2$, must be less than in the case of a sphere. Thus, $N_a < \frac{1}{3}$. Similarly, if the ellipsoid is magnetized along $b$ ([](#fig:demagfield)e), the demagnetizing field is stronger or $N_b>\frac{1}{3}$.

Getting back to the magnetostatic energy density, $\epsilon_m = -\mathbf{M} \cdot \mathbf{B}$, remember that $\mathbf{B}$ includes both the external field $\mathbf{H}_e$ and the internal demagnetizing field $\mathbf{H}_d = -\mathbf{N}\cdot\mathbf{M}$. Therefore, magnetostatic energy density from both the external and internal fields is given by:

$$
\epsilon_{ms} = -\mu_o \mathbf{M} \cdot \mathbf{H}_e + \frac{1}{2} \mu_o \mathbf{M} \cdot \mathbf{N} \cdot \mathbf{M}.
$$ (eq:etot)

The two terms in [Equation %s](#eq:etot) are the by now familiar magnetostatic energy density $\epsilon_m$, and the *magnetostatic self energy density* or the *demagnetizing energy density* $\epsilon_{d}$. $\epsilon_d$ can be estimated by "building" a magnetic particle and considering the potential energy gained by each incremental volume $dv$ as it is brought in ($-\mu_o \mathbf{M} dv \cdot \mathbf{H}_d$) and integrating. The $\frac{1}{2}$ appears in order to avoid counting each volume element twice and the $v$ disappears because all the energies we have been discussing are energy densities — the energy per unit volume.

For the case of a uniformly magnetized sphere, we get back to the relation $\mathbf{H}_d = -N\mathbf{M}$ and $\epsilon_d$ simplifies to:

$$
\epsilon_d = -\frac{1}{2} \mu_o N M^2.
$$

In the more general case of a prolate ellipsoid, $\mathbf{M}$ can be represented by the two components parallel to the $a$ and $b$ axes (see [](#fig:demagfield)f) with unit vectors parallel to them $\hat{a}, \hat{b}$. So, $\mathbf{M} = M\cos \theta  \hat{a} + M\sin \theta \hat{b}$. Each component of $\mathbf{M}$ has an associated demagnetizing field $\mathbf{H}_d= -N_a M \cos  \theta \hat{a} - N_b M \sin \theta \hat{b}$ where $N_a, N_b$ are the eigenvalues of the tensor $\mathbf{N}$ (the values of the demagnetizing tensor along the principal axes $a$ and $b$). In this case, the demagnetizing energy can be written as:

$$
\epsilon_d =-\frac{1}{2} \mu_o(N_a \cos^2 \theta + N_b \sin^2 \theta)M^2
 = -\frac{1}{2} \mu_o(N_a + (N_b-N_a)\sin^2 \theta)M^2
 = -\frac{1}{2} \mu_o(N_b\sin^2 \theta)M^2.
$$ (eq:ed)

In an ellipsoid with three unequal axes $a,b,c$, $N_a+N_b+N_c =1$ (in SI; in cgs units the sum is 4$\pi$). For a long needle-like particle, $N_a\simeq 0$ and $N_b = N_c \simeq \frac{1}{2}$.
A useful approximation for nearly spherical particles is $N_a = \frac{1}{3} [ 1 - \frac{2}{5}(2 - \frac{b}{a} - \frac{c}{a} )]$ {cite}`stacey1974`. For more spheroids, see {cite}`nagata1961` (p. 70) and for the general case, see {cite}`dunlop1997`.
In the absence of an external field, the magnetization will be parallel to the long axis ($\theta=0$) and the magnetostatic energy density (also known as the 'self' energy) is given by:

$$
\epsilon_{ms}= -\frac{1}{2} \mu_o \Delta N M^2=-\frac{1}{2} \mu_o N_c M^2.
$$ (eq:self)

Note that the demagnetizing energy in [Equation %s](#eq:ed) has a uniaxial form, directionally dependent only on $\theta$, with the constant of uniaxial anisotropy $K_u = \frac{1}{2} \Delta N \mu_o M^2$. $\Delta N$ is the difference between the largest and smallest values of the demagnetizing tensor $N_c-N_a$.

For a prolate ellipsoid $N_c=N_b$ and choosing for example $a/c = 1.5$ we find that $N_a-N_c \approx 0.16$. The magnetization of magnetite is 480 kAm$^{-1}$, so $K_u \simeq$ 2.7 × 10$^4$ Jm$^{-3}$. This is somewhat larger than the absolute value of $K_1$ for magnetocrystalline anisotropy in magnetite ($K_1$= −1.35 × 10$^{4}$ Jm$^{-3}$), so the magnetization for even slightly elongate grains will be dominated by uniaxial anisotropy controlled by shape. Minerals with low saturation magnetizations (like hematite) will not be prone to shape dominated magnetic anisotropy, however.

(sect:coercivity)=
### Magnetic energy and magnetic stability

Paleomagnetists worry about how long a magnetization can remain fixed within a particle and we will begin to discuss this issue later in the chapter. It is worth pointing out here that any discussion of magnetic stability will involve magnetic anisotropy energy because this controls the energy required to change a magnetic moment from one easy axis to another. One way to accomplish this change is to apply a magnetic field sufficiently large that its magnetic energy exceeds the anisotropy energy. The magnetic field capable of flipping the magnetization of an individual uniformly magnetized particle (at saturation, or $M_s$) over the magnetic anisotropy energy barrier is the *microscopic coercivity* $H_k$. For uniaxial anisotropy ($K=K_u$) and for cubic magnetocrystalline anisotropy ($K=K_1$), microscopic coercivity is given by:

$$
H_k = \frac{2 K_u}{\mu_o M}   = \frac{4}{3} \frac{|K_1|}{\mu_o M_s}.
$$ (eq:Bk)

respectively (see {cite}`dunlop1997` for a more complete derivation). For elongate particles dominated by shape anisotropy, $H_k$ reduces to $\Delta NM$. [Note that the units for coercivity as derived here are in Am$^{-1}$, although they are often measured using instruments calibrated in tesla. Technically, because the field doing the flipping is inside the magnetic particle and $\mathbf{B}$ (measured in tesla) depends on the magnetization $\mathbf{M}$ as well as the field $\mathbf{H}$, coercivity should be written as $\mu_o H_k$ if the units are quoted in tesla.] Microscopic coercivity is another parameter with many names: *flipping field*, *switching field*, *intrinsic coercivity* and also more loosely, the *coercive field* and *coercivity*. We will come back to the topic of coercivity in Chapter 5.

## Magnetic domains

So far we have been discussing hypothetical magnetic particles that are uniformly magnetized. Particles with strong magnetizations (like magnetite) have self energies that quickly become quite large because of the dependence on the square of the magnetization. We have been learning about several mechanisms that tend to align magnetic spins. In very small particles of magnetite (less than 60 nm for equant grains {cite}`nagy2017`), exchange energy dominates and the spins are uniformly aligned — the particle is single domain (SD). In larger particles, the self energy increasingly competes with the exchange and magnetocrystalline energies, and crystals develop distinctly non-uniform states of magnetization.

<!-- Figure modified from williams2024, licensed CC BY 4.0 -->
:::{figure} ../figures/chapter4/vortex.png
:name: fig:nonuniform
:width: 80%

Micromagnetic simulations of remanent domain states in magnetite computed using MERRILL {cite:p}`williams2024`. The elongate particles have an aspect ratio (b/a) of 2.25 while the equant particles are equidimensional. The numbers above the grains correspond to the equivalent spherical volume diameters (which is effectively the diameter for the equant ones; and a way to succinctly summarize the grain length for the elongate ones). The arrows show local magnetization direction while the colors indicate alignment with magnetocrystalline easy axes. For the elongate grains, the 90 nm grain has single-domain behavoir while the 160 nm grain has a vortex aligned with the long axis (which is the easy axis). The 80 nm equant grain is in a single-domain state, while the 90 nm grain is in an intermediate flower state with the initiation of a vortex. At a size of 140 nm there is a vortex aligned with the crystallographic easy axis. [From {cite}`williams2024`.] 
:::

There are multiple strategies for magnetic particles to reduce self energy. Numerical models (called *micromagnetic models*) can find internal magnetization configurations that minimize the energies discussed in the preceding sections. Modern micromagnetic codes such as MERRILL {cite:p}`oconbhui2018` allow us to peer into the state of magnetization inside magnetic particles. [](#fig:nonuniform) shows the progression of remanent states as particle size increases, computed using MERRILL {cite:p}`williams2024`. In the smallest grains, the exchange energy overwhelms the self energy and the magnetization is nearly uniform — the SD state. As equant grains grow beyond about 60 nm, the self energy becomes large enough to perturb the magnetization near particle surfaces, causing spins at the edges to splay outward while the interior remains broadly aligned. This is the *flower state* ([](#fig:nonuniform)e), so named because the fanning spins at the surface resemble the opening of a flower. By about 80 nm, the self energy is large enough that the magnetization curls into a closed loop, forming a *vortex state* ([](#fig:nonuniform)b,c,f) with a narrow core of spins {cite:p}`nagy2017`. The net remanent moment of a vortex particle is carried almost entirely by this core, since the curling spins surrounding it largely cancel. In elongated grains, shape anisotropy aligns both the vortex core and the overall remanence along the long axis of the particle ([](#fig:nonuniform)a–c). The curling magnetization dramatically reduces the external field of the particle (and hence its self energy), while the exchange energy cost remains modest because neighboring spins change direction only gradually. In the smallest particles, the spins would have to curl too tightly and the exchange energy cost keeps them uniformly magnetized in the SD state. Particles with vortex cores share many properties of SD grains — in particular, they can carry extremely stable magnetic remanence with relaxation times exceeding the age of the Solar System {cite:p}`nagy2017` — which has led to them being termed *pseudo-single domain* (PSD) particles.

As particles grow larger (>~200 nm), they break into multiple magnetic domains, separated by narrow zones of rapidly changing spin directions called *domain walls*. Magnetic domains can take many forms. We illustrate a few in [](#fig:domains). The uniform case (single domain) is shown in [](#fig:domains)a. The external field is very large because the free poles are far apart (at opposite ends of the particle). When the particle organizes itself into two domains ([](#fig:domains)b), the external field is reduced by about a factor of two. In the case of four lamellar domains ([](#fig:domains)c), the external field is quite small. The introduction of *closure domains* as in [](#fig:domains)d reduces the external field to nothing.

:::{figure} ../figures/chapter4/domains.png
:name: fig:domains
:width: 80%

A variety of domain structures of a given particle. a) Uniformly magnetized (single domain). [Adapted from {cite}`tipler1999`.] b) Two domains. c) Four domains in a lamellar pattern. d) Essentially two domains with two closure domains.
:::

As you might already suspect, domain walls are not "free", energetically speaking. If, as in [](#fig:wall)a, the spins simply switch from one orientation to the other abruptly, the exchange energy cost would be very high. One way to get around this is to spread the change over several hundred atoms, as sketched in [](#fig:wall)b. The wall width $\delta$ is wider and the exchange energy price is much less. However, there are now spins in unfavorable directions from a magnetocrystalline point of view (they are in "hard" directions). Exchange energy therefore favors wider domain walls while magnetocrystalline anisotropy favors thin walls. With some work (see e.g., {cite}`dunlop1997`, pp. 117–118), it is possible to come up with the following analytical expressions for wall width ($\delta_w$) and wall energy density ($\epsilon_w$):

$$
\delta_w = \pi \left(\frac{A}{K}\right)^{1/2}, \quad \epsilon_w = 2\pi (AK)^{1/2},
$$ (eq:wall)

where $A$ is the exchange constant (see {ref}`sect:exchange`) and $K$ is the magnetic anisotropy constant (e.g., $K_u$ or $K_1$). Note that $\epsilon_w$ is the energy density per unit wall area, not per volume. Plugging in values for magnetite given previously we get $\delta_w$ = 90 nm and $\epsilon_w$ = 3×10$^{-3}$ Jm$^{-2}$.

:::{figure} ../figures/chapter4/wall.png
:name: fig:wall
:width: 100%

Examples of possible domain walls. a) There is a 180° switch from one atom to the next. The domain wall is very thin, but the exchange price is very high. b) There is a more gradual switch from one direction to the other [note: each arrow represents several 10's of unit cells]. The exchange energy price is lower, but there are more spins in unfavorable directions from a magnetocrystalline point of view.
:::

In [](#fig:energies) we plot the self energy ([Equation %s](#eq:self)) and the wall energy ($\epsilon_w$ from [Equation %s](#eq:wall)) for spheres of magnetite. We see that the wall energy in particles with diameters of some 50 nm is less than the self energy, yet the width of the walls is about twice as wide as that. So the smallest wall is really more like the vortex state and it is only for particles larger than a few tenths of a micron that true domains separated by discrete walls can form. Interestingly, this is precisely what is predicted from micromagnetic modelling (e.g., [](#fig:nonuniform)).

:::{figure} ../figures/chapter4/energies.png
:name: fig:energies
:width: 50%

Comparison of "self" energy versus the energy of the domain wall in magnetite spheres as a function of particle size.
:::

How can we test the theoretical predictions of domain theory? Do domains really exist? Are they the size and shape we expect? Are there as many as we would expect? In order to address these questions we require a way of imaging magnetic domains. {cite}`bitter1931` devised a way for doing just that. Magnetic domain walls are regions with large stray fields (as opposed to domains in which the spins are usually parallel to the sides of the crystals to minimize stray fields). In the *Bitter technique* magnetic colloid material is drawn to the regions of high field gradients on highly polished sections allowing the domain walls to be observed (see [](#fig:domain-images)a).

:::{figure} ../figures/chapter4/domain-images.png
:name: fig:domain-images
:width: 80%

a) Bitter patterns from an oriented polished section of magnetite. [Figure from {cite}`ozdemir1995`.] b) Domains revealed by longitudinal magneto-optical Kerr effect. [Image from {cite}`heider1992`.] c–e) Magnetic force microscopy technique. [Images from {cite}`feinberg2005`.] c) Image of topography of surface of a magnetite inclusion in a non-magnetic matrix. d) Magnetic image from MFM technique. e) Interpretation of magnetizations of magnetic domains.
:::

There are by now other ways of imaging magnetic domains. We will not review them all here, but will just highlight the ways that are more commonly used in rock and paleomagnetism. The *magneto-optical Kerr effect* or MOKE uses the interaction between polarized light and the surface magnetic field of the target. The light interacts with the magnetic field of the sample which causes a small change in the light's polarization and ellipticity. The changes are detected by reflecting the light into nearly-crossed polarizers. The longitudinal Kerr effect can show the alignment of magnetic moments in the surface plane of the sample. Domains with different magnetization directions show up as lighter or darker regions in the MOKE image (see [](#fig:domain-images)b.)

Another common method for imaging magnetic domains employs a technique known as *magnetic force microscopy*. Magnetic force microscopy (MFM) uses a scanning probe microscope that maps out the vertical component of the magnetic fields produced by a highly polished section. The measurements are made with a cantilevered magnetic tip that responds to the magnetic field of the sample. In practice, the measurements are made in two passes. The first establishes the topography of the sample ([](#fig:domain-images)c). Then in the second pass, the tip is raised slightly above the surface and by subtracting the "topographic only" signal the attraction of the magnetic surface can be mapped ([](#fig:domain-images)d). [](#fig:domain-images)e shows an interpretation of the magnetic directions of different magnetic domains.

(sect:tau)=
## Thermal energy

We have gone some way toward answering the questions posed at the beginning of the chapter. We see now that anisotropy energy, with contributions from crystal structure, shape and stress, inhibits changes in the magnetic direction thereby offering a possible mechanism whereby a given magnetization could be preserved for posterity. We also asked the question of what allows the magnetization to come into equilibrium with the applied magnetic field in the first place; this question requires a little more work to answer. The key to this question is to find some mechanism which allows the moments to "jump over" magnetic anisotropy energy barriers. One such mechanism is thermal energy $E_T$, which was given in Chapter 3 as:

$$
E_T = kT.
$$

We know from statistical mechanics that the probability $P$ of finding a grain with a given thermal energy sufficient to overcome some anisotropy energy $E_a$ and change from one easy axis to another is $P=\exp (-E_a/E_T )$. Depending on the temperature, such grains may be quite rare, and we may have to wait some time $t$ for a particle to work itself up to jumping over the energy barrier.

Imagine a block of material containing a random assemblage of magnetic particles that are for simplicity uniformly magnetized and dominated by uniaxial anisotropy. Suppose that this block has some initial magnetization $M_o$ and is placed in an environment with no ambient magnetic field. Anisotropy energy will tend to keep each tiny magnetic moment in its original direction and the magnetization will not change over time. At some temperature, certain grains will have sufficient energy to overcome the anisotropy energy and flip their moments to the other easy axis. As a result, over time, the magnetic moments will become random. Therefore, the magnetization as a function of time in this simple scenario will decay to zero. The equation governing this decay is:

$$
M(t) = M_o \exp \left(\frac{-t}{\tau}\right),
$$ (eq:MvT)

where $t$ is time and $\tau$ is an empirical constant called the *relaxation time*. Relaxation time is the time required for the remanence to decay to $1/e$ of $M_o$. This equation is the essence of what is called *Néel theory* (see, e.g., {cite}`neel1955`). The value of $\tau$ depends on the competition between magnetic anisotropy energy and thermal energy. It is a measure of the probability that a grain will have sufficient thermal energy to overcome the anisotropy energy and switch its moment. Therefore in zero external field:

$$
\tau = \frac{1}{C} \exp \frac{Kv}{kT},
$$ (eq:tau)

where $C$ is a frequency factor with a value of something like $10^{10}$ s$^{-1}$. The anisotropy energy is given by the dominant anisotropy parameter $K$ (either $K_u, K_1$, or $\lambda$) times the grain volume $v$.

Thus, the relaxation time is proportional to anisotropy constant and volume, and is inversely related to temperature. Relaxation time $\tau$ varies rapidly with small changes in $v$ and $T$. To see how this works, we can take $K_u$ for slightly elongate cuboids of magnetite (length to width ratio of 1.3 to 1) and evaluate relaxation time as a function of particle width (see [](#fig:tauvd)). There is a sharp transition between grains with virtually no stability ($\tau$ is on the order of seconds) and grains with stabilities of billions of years.

:::{figure} ../figures/chapter4/tauvd.png
:name: fig:tauvd
:width: 70%

Relaxation time in magnetite ellipsoids as a function of grain width in nanometers (all length to width ratios of 1.3:1.)
:::

Grains with $\tau \simeq 10^2 - 10^3$ seconds have sufficient thermal energy to overcome the anisotropy energy frequently and are unstable on a laboratory time scale. In zero field, these grain moments will tend to rapidly become random, and in an applied field, also tend to align rapidly with the field. The net magnetization is related to the field by a Langevin function (see Chapter 3). Therefore, this behavior is quite similar to paramagnetism, hence these grains are called *superparamagnetic* (SP). Such grains can be distinguished from paramagnets, however, because the field required to saturate the moments is typically much less than a tesla, whereas that for paramagnets can exceed hundreds of tesla.

## Putting it all together

We are now in a position to pull together all the threads we have considered in this chapter and make a plot of what sort of magnetic particles behave as superparamagnets, which should be single domain and which should be multi-domain according to our simple theories. We can estimate the superparamagnetic to single domain threshold for magnetite as a function of particle shape by finding the length (2a) that gives a relaxation time of 100 seconds as a function of width-to-length ratio ($b/a$) for parallelepipeds of magnetite (heavy blue line in [](#fig:butban)). To do this, we follow the logic of {cite}`evans1969` and {cite}`butler1975`. In this *Evans diagram*, we estimated relaxation time using [Equation %s](#eq:tau), plugging in values of $K$ as either the magnetocrystalline effective anisotropy constant ($\frac{1}{12}K_1$) or the shape anisotropy constant ($\frac{1}{2} \Delta N \mu_o M^2$), whichever was less. We also show the curve at which relaxation time is equal to 1 Gyr, reinforcing the point that very small changes in crystal size and shape make profound differences in relaxation time.
The figure also predicts the boundary between the single domain field and the two domain field, when the energy of a domain wall is less than the self energy of a particle that is uniformly magnetized. This can be done by evaluating wall energy with [Equation %s](#eq:wall) for a wall along the length of a parallelepiped and area ($4ab$) as compared to the self energy ($\frac{1}{2} \mu_o N_a M^2v$) for a given length and width-to-length ratio. When the wall energy is less than the self energy, we are in the two domain field.

:::{figure} ../figures/chapter4/butban.png
:name: fig:butban
:width: 70%

Expected domain states for various sizes and shapes of parallelepipeds of magnetite at room temperature. The parameters $a$ and $b$ are as in [](#fig:demagfield)e. Heavy blue (thin green) line is the superparamagnetic threshold assuming a relaxation time of 100s (1 Gyr). Dashed red line marks the SD/MD threshold size. Calculations done using assumptions and parameters described in the text.
:::

[](#fig:butban) suggests that there is virtually no SD stability field for equant magnetite; particles are either SP or MD (multi-domain). As the width-to-length ratio decreases (the particle gets longer), the stability field for SD magnetite expands. Of course micromagnetic modelling shows that there are several transitional states between uniform magnetization (SD) and MD, i.e. the flower and vortex remanent states (see {cite}`fabian1996`), but [](#fig:butban) has enormous predictive power and the version of {cite}`butler1975` (which is slightly different in detail) continues to be used extensively. It is worth pointing out however, that the size at which domain walls appear in magnetite is poorly constrained because it depends critically on the exact shape of the particle, its state of stress and even its history of exposure to past fields. Estimates in the literature range from as small as 20 nm to much larger (up to 100 nm) depending on how the estimates are made. Nonetheless, it is probably true that truly single domain magnetite is quite rare in nature, yet more complicated states are difficult to treat theoretically. Therefore most paleomagnetic studies rely on predictions made for single domain particles.

**Supplemental Reading:** {cite}`dunlop1997`, Chapters 2.8 and 5.

## Problems

**Problem 1**

Assume that the magnetization of magnetite is about 4.8 × 10$^5$ Am$^{-1}$. Using values for other parameters from the text, write a Python program to calculate the following:

a) Self energy (or magnetostatic energy) for a sphere 1, 10 and 100 $\mu$m in diameter. [Hint: see [Equation %s](#eq:self) for the 'self' energy density. Also, remember the difference between energy and energy density!]

$$
\epsilon_{ms}= -\frac{1}{2} \mu_o N_c M^2.
$$

b) Magnetostatic (shape) anisotropy energy for an ellipsoid whose principal semi-axis is 1 $\mu$m and whose major and minor semi-axes are each 0.25 $\mu$m. You may use the "nearly spherical" approximation in the text.

c) The critical radius of a sphere at which wall energy equals self energy.

**Problem 2**

Calculate grain diameter for magnetite spheres with $\tau$s of 10$^{-1}$, 10, 10$^2$, 10$^3$, 10$^5$, 10$^9$, 10$^{15}$ seconds. Use values for Boltzmann's constant, $C$ (the frequency factor) and $|K_1|$ at room temperature (300K).

**Problem 3** [From Jeff Gee]

a) Consider a highly elongate rod (needle-shaped grain) of magnetite. Explain why the demagnetizing factor along the long axis of the rod is about zero while that across the long axis is about one half.

b) The file *Chapter_4/prolate.txt* gives the values of demagnetizing factors for a prolate ellipsoid (with axes a > b = c). For an elongate rod of magnetite with range of aspect ratios (AR = c:b) provided in the table, plot the magnetostatic self energy density in the absence of an external field. Use this plot to estimate the aspect ratio at which shape anisotropy will be equal to that of magnetocrystalline anisotropy (use a value of $K_1$ at room temperature (300K) of −1.43 × 10$^4$ J/m$^3$).

c) What is the maximum microscopic coercivity ($H_k$) for such an elongate grain of magnetite (assume an infinitely long grain)? Coercivities are more commonly reported in units of T so provide this corresponding value as well.
