import streamlit as st

st.markdown("""
<style>
            
            .stButton > button
            {
            backgroundcolor:"green";
            color:"white";
            border-radius:50%;
            }
</style>

            """,unsafe_allow_html=True)










st.title("welcome to basic streamlit app")

age=st.slider("Select your age",1,100)
st.selectbox("Select your city",["Delhi","Mumbai","Nashik","Pune"])

if st.button("show details"):
    st.write("Age", age)
    st.wrte("city",city)
    