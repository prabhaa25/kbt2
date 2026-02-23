import streamlit as st

st.title("Basic Calculator")

num1 = st.number_input("Enter your first number", step=1)
num2 = st.number_input("Enter your second number", step=1)

operation = st.selectbox("Choose Operation", ["add","subt","mult","div"])

if st.button("Calculate"):
    if operation == "add":
        st.write(num1 + num2)

    elif operation == "subt":
        st.write(num1 - num2)

    elif operation == "mult":
        st.write(num1 * num2)

    elif operation == "div":
        if num2 != 0:
            st.write(num1 / num2)
        else:
            st.write("Cannot divide by zero")