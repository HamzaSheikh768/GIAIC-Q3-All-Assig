import streamlit as st

st.header("Unit Convertor")
st.write("Easily Convert between different units of length, weight, temprature...")

conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temprature"])
value = st.number_input("Enter Value...", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

# --------------------------------------Lenght Define------------------------------------------- #
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilograms", "Centimeters", "Milimeters", "Miles", "Yards", "Inches", "Feets"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilograms", "Centimeters", "Milimeters", "Miles", "Yards", "Inches", "Feets"])

# -------------------------------------- weight Define------------------------------------------- #
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Miligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Miligrams", "Pounds", "Ounces"])

# --------------------------------------Temprature Define------------------------------------------- #
elif conversion_type == "Temprature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])



# -----------------------------------------add lenght function-------------------------------------- #
def length_convertor(value, from_unit, to_unit):
    lenght_units = {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Milimeters": 1000, "Miles":0.000621371, 
        "Yards":1.09361, "Inches":39.37, "Feets":3.28 
    }
    return (value / lenght_units [from_unit]) * lenght_units[to_unit]


# -----------------------------------------add Weight function-------------------------------------- #

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1, "Grams": 1000, "Miligrams": 1000000, "Pounds": 2.2046, "Ounces": 35.27
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]


# -----------------------------------------add Temperature function-------------------------------------- #

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == "Calsius":
        return(value * 9/5 +32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return((value - 32) * 5/9) if to_unit == "Celsius" else (value -32) * 5/9 - 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5+32  if to_unit == "Fahrenheit" else value
    return value

if st.button("Convert ( ͡° ͜ʖ ͡°)"):
    if conversion_type == "Lenght":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temprature":
        result = temperature_convertor(value, from_unit, to_unit)

    st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")