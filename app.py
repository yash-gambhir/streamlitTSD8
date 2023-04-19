import streamlit as st

def find_largest_num(num1, num2, num3):
    return max(num1, num2, num3)

st.title("Find the largest number from the given three numbers")
st.subheader("Created by Yash Gambhir")
num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
num3 = st.number_input("Enter the third number")

if st.button("Find"):
    result = find_largest_num(num1, num2, num3)
    st.success(f"The largest number is {result}")
