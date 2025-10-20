import streamlit as st

def mulch_tonnage(area_sqft: float, depth_inch: float, mulch_type: str = 'medium') -> float:
    """
    Convert square feet of mulch coverage at a given depth (inches) to tons.

    Parameters:
    - area_sqft: float — area in square feet
    - depth_inch: float — mulch depth in inches
    - mulch_type: str — 'light' (~400 lb/yd³), 'medium' (~500 lb/yd³), or 'heavy' (~600 lb/yd³)

    Returns:
    - tons: float — total tons of mulch required
    """

    # Convert depth to feet
    depth_ft = depth_inch / 12
    cuft_per_cuyd = 27

    # Volume in cubic yards
    cubic_yards = (area_sqft * depth_ft) / cuft_per_cuyd

    # Determine mulch weight
    mulch_weights = {
        'light': 400,
        'medium': 500,
        'heavy': 600
    }

    weight_lb_per_yd3 = mulch_weights.get(mulch_type.lower(), 500)

    # Convert to tons
    tons_per_yd3 = weight_lb_per_yd3 / 2000
    total_tons = cubic_yards * tons_per_yd3

    return total_tons


# --- Streamlit App ---
st.title('🌿 Mulch Tonnage Calculator')

st.write('Easily convert square feet of mulch coverage to **tons** for any mulch type and depth.')

# User inputs
area = st.number_input('Enter Area (sq ft):', min_value=0.0, step=10.0)
depth_inch = st.slider('Select Mulch Depth (inches):', min_value=1.0, max_value=6.0, value=3.0, step=0.5)
mulch_type = st.radio('Select Mulch Type:', ['Light (~400 lb/yd³)', 'Medium (~500 lb/yd³)', 'Heavy (~600 lb/yd³)'])

# Parse mulch type
mulch_key = mulch_type.split()[0].lower()

# Calculate result
tons = mulch_tonnage(area, depth_inch, mulch_key)

# Display
st.metric(label='Estimated Tons Needed', value=f'{tons:.2f} tons')

st.caption('Formula: Tons = (Area × Depth × Weight) / (27 × 2000)')

