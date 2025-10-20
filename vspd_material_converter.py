import streamlit as st
from PIL import Image

# --- Branding ---
st.set_page_config(page_title="VSPD Material Converter", page_icon="🪨", layout="centered")

# Load logo
def load_logo():
    try:
        return Image.open("vspd_logo.png")
    except Exception:
        return None

logo = load_logo()

# --- Header with Logo and Title ---
col1, col2 = st.columns([1, 3])
with col1:
    if logo:
        st.image(logo, use_container_width=True)
with col2:
    st.markdown("""<h1 style='color:#D4AF37;'>V.S.P.D. Material Converter</h1>
    <h4 style='color:#000;'>Valley Slope Protection Design — Material Estimating Tools</h4>""", unsafe_allow_html=True)

st.markdown("<hr style='border:2px solid #D4AF37;'>", unsafe_allow_html=True)

# --- Helper Data ---
material_densities = {
    'Decomposed Granite': 3000,
    'ABC': 3100,
    'Desert Pavement': 3000,
    'Rip Rap': 3300,
    'Mulch': 500,
    'Boulders': 4455
}

size_multipliers = {
    '3/8" - 1/4"': 1.00,
    '1/2"': 1.03,
    '3/4"': 1.05,
    '1"': 1.08,
    '1.5"': 1.10,
    '2" - 3"': 1.12,
    '3"': 1.15,
    '3" - 8"': 1.20
}

type_multipliers = {
    'N/A': 1.00,
    'Screened': 1.00,
    'Minus': 1.05,
    'Compacted': 1.15,
    'Stabilized': 1.20
}

# --- User Inputs ---
st.subheader("Select Material and Settings")
material = st.selectbox("Material Type", list(material_densities.keys()))

# Determine whether to show processing dropdown
if material in ["Mulch", "Rip Rap", "Boulders"]:
    process_type = "N/A"
    st.info("Processing type not applicable for this material.")
else:
    process_type = st.selectbox("Processing Type", list(type_multipliers.keys()))

if material != 'Boulders':
    size = st.selectbox("Material Size", list(size_multipliers.keys()))
    depth_in = st.slider("Depth (inches)", 1.0, 12.0, 3.0, 0.5)

conversion_dir = st.radio("Conversion Mode", ["Square Footage ➜ Tons", "Tons ➜ Square Footage"])

# --- Calculation ---
def calc_tons(area, depth_in, material, size, process):
    depth_ft = depth_in / 12
    cu_yds = (area * depth_ft) / 27
    base_density = material_densities[material]
    tons_per_yd3 = (base_density / 2000) * size_multipliers[size] * type_multipliers[process]
    return cu_yds * tons_per_yd3, cu_yds

def calc_area(tons, depth_in, material, size, process):
    base_density = material_densities[material]
    tons_per_yd3 = (base_density / 2000) * size_multipliers[size] * type_multipliers[process]
    cu_yds = tons / tons_per_yd3
    depth_ft = depth_in / 12
    return (cu_yds * 27) / depth_ft, cu_yds

# --- Boulder Calculation ---
def calc_boulders(qty, L, W, H):
    volume_ft3 = L * W * H * qty
    weight_lb = volume_ft3 * 165  # avg granite density
    tons = weight_lb / 2000
    cu_yds = volume_ft3 / 27
    return tons, cu_yds, weight_lb

# --- Display Inputs and Results ---
if material == 'Boulders':
    st.subheader("Boulder Dimensions")
    qty = st.number_input("Quantity", min_value=1, step=1)
    L = st.number_input("Length (ft)", min_value=0.1, step=0.1)
    W = st.number_input("Width (ft)", min_value=0.1, step=0.1)
    H = st.number_input("Height (ft)", min_value=0.1, step=0.1)

    tons, cu_yds, weight_lb = calc_boulders(qty, L, W, H)
    st.success(f"Total: **{tons:.2f} tons** ({cu_yds:.2f} CY / {weight_lb:,.0f} lbs)")

else:
    if conversion_dir == "Square Footage ➜ Tons":
        area = st.number_input("Enter Area (sq ft):", min_value=0.0, step=10.0)
        if area > 0:
            tons, cu_yds = calc_tons(area, depth_in, material, size, process_type)
            st.success(f"You need approximately **{tons:.2f} tons** ({cu_yds:.2f} cubic yards)")
    else:
        tons_input = st.number_input("Enter Tons:", min_value=0.0, step=0.1)
        if tons_input > 0:
            area, cu_yds = calc_area(tons_input, depth_in, material, size, process_type)
            st.success(f"{tons_input:.2f} tons will cover approximately **{area:,.0f} sq ft** ({cu_yds:.2f} cubic yards)")

st.markdown("<hr style='border:2px solid #D4AF37;'>", unsafe_allow_html=True)

# --- Footer Logo and Credits ---
if logo:
    st.image(logo, width=200)

st.markdown("<p style='color:#000;text-align:center;'>© 2025 Valley Slope Protection Design — V.S.P.D. Estimating Tools</p>", unsafe_allow_html=True)
