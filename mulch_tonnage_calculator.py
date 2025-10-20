# 🌿 Mulch Tonnage Calculator (3-inch Depth)

import streamlit as st

def mulch_tonnage(area_sqft: float, mulch_type: str = 'medium') -> float:
    """
    Convert square feet of 3-inch mulch depth to tons.

    Parameters:
    - area_sqft: float — area in square feet
    - mulch_type: str — 'light' (~400 lb/yd³), 'medium' (~500 lb/yd³), or 'heavy' (~600 lb/yd³)

    Returns:
    - tons: float — total tons of mulch required
    """

    # Step 1: Constants
    depth_ft = 3 / 12  # 3 inches = 0.25 ft
    cuft_per_cuyd = 27

    # Step 2: Volume in cubic yards
    cubic_yards = (area_sqft * depth_ft) / cuft_per_cuyd

    # Step 3: Determine weight per cubic yard based on mulch type
    mulch_weights = {
        'light': 400,   # lb/yd³
        'medium': 500,
        'heavy': 600
    }

    weight_lb_per_yd3 = mulch_weights.get(mulch_type.lower(), 500)

    # Step 4: Convert to tons
    tons_per_yd3 = weight_lb_per_yd3 / 2000
    total_tons = cubic_yards * tons_per_yd3

    return total_tons

# --- Streamlit App ---
st.title('🌿 Mulch Tonnage Calculator (3-inch Depth)')

st.write('Easily convert square feet of 3-inch mulch coverage to **tons** based on mulch density.')

area = st.number_input('Enter Area (sq ft):', min_value=0.0, step=10.0)
mulch_type = st.radio('Select Mulch Type:', ['Light (~400 lb/yd³)', 'Medium (~500 lb/yd³)', 'Heavy (~600 lb/yd³)'])

# Map mulch type string to key
mulch_key = mulch_type.split()[0].lower()

tons = mulch_tonnage(area, mulch_key)

st.metric(label='Estimated Tons Needed', value=f'{tons:.2f} tons')

st.caption('Formula: Tons = (Area / 108) × (Weight per yd³ / 2000)')
