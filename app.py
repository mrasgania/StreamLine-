import streamlit as st

st.title('Find the Largest Number')

# Input fields for the numbers
num1 = st.number_input('Enter the first number', value=0)
num2 = st.number_input('Enter the second number', value=0)
num3 = st.number_input('Enter the third number', value=0)

# Button to find the largest number
if st.button('Find the Largest Number'):
    largest = max(num1, num2, num3)
    st.success(f'The largest number is {largest}')
