import streamlit as st

st.title("📏 Length Unit Converter")

# List of all supported units
units = {
    "Kilometre": 1000,
    "Metre": 1,
    "Centimetre": 0.01,
    "Millimetre": 0.001,
    "Micrometre": 1e-6,
    "Nanometre": 1e-9,
    "Mile": 1609.34,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254,
    "Nautical mile": 1852
}

# User input
value = st.number_input("Enter value", value=1.0)
from_unit = st.selectbox("From", units.keys())
to_unit = st.selectbox("To", units.keys())

# Convert input value to metres
value_in_metres = value * units[from_unit]

# Convert from metres to target unit
result = value_in_metres / units[to_unit]

# Show result
st.write(f"### Result: {result} {to_unit}")
