import streamlit as st

st.title("welcome to basic streamlit app")

age=st.slider("Select your age",1,100)
st.selectbox("Select your city",["Delhi","Mumbai","Nashik","Pune"])

if st.button("show details"):
    st.write("Age", age)
    st.wrte("city",city)
    