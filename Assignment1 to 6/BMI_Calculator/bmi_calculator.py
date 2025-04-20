import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def main():
    st.title("💪 BMI Calculator")
    st.write("Enter your weight and height to calculate your Body Mass Index (BMI).")

    name = st.text_input("Enter your name", "")
    weight = st.number_input("Enter your weight (in kg)", min_value=0.0, format="%.2f")
    height = st.number_input("Enter your height (in meters)", min_value=0.0, format="%.2f")

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"{name}, your BMI is: {bmi}")

            if bmi < 18.5:
                st.warning("You are underweight.")
            elif 18.5 <= bmi < 25:
                st.success("You have a normal weight.")
            elif 25 <= bmi < 30:
                st.info("You are overweight.")
            else:
                st.error("You are obese.")
        else:
            st.error("Height must be greater than 0.")

if __name__ == "__main__":
    main()
