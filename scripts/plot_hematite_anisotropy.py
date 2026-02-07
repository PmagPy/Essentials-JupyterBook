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
