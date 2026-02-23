import streamlit as st

st.title("Student Form")


st.markdown("""
<style>
.stButton > button {
    background-color: blue;
    color: white;
    border-radius=50%;
}
</style>
""", unsafe_allow_html=True)


name = st.text_input("Enter Name")
roll_no = st.number_input("Enter Roll No", step=1)
student_class = st.text_input("Enter Class")


if st.button("Submit"):
    st.write("Form Submitted!")
    