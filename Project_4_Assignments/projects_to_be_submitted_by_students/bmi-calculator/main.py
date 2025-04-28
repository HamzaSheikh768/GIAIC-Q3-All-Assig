# Project 8 - BMI Calculator Web App
# by Muhammad Faizan, 00398964

import streamlit as st

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def main():
    st.title("🧮 BMI Calculator By Muhammad Faizan...")
    st.write("Calculate your Body Mass Index")

    # Inputs
    weight = st.number_input("Enter your weight (kg)", min_value=1.0)
    height = st.number_input("Enter your height (cm)", min_value=1.0)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)

        st.success(f"Your BMI is: {bmi}")

        if bmi < 18.5:
            st.warning("You're underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You're in a healthy weight range.")
        elif 25 <= bmi < 29.9:
            st.info("You're overweight.")
        else:
            st.error("You're in the obese range.")

if __name__ == '__main__':
    main()
