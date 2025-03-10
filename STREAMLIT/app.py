import streamlit as st

st.title("My Application")
st.header("My First Header")
st.text("Good Morning Hello")
st.markdown("# Hello")
st.markdown("## Hello")
st.markdown("**Hello**")
st.markdown("*Hello*")

st.markdown("<h1 style= 'text-align: center;'>This is header 1</h1>", unsafe_allow_html= True)
st.markdown("<p style= 'color: red;'>This Paragraph</p>", unsafe_allow_html= True)
st.markdown("<h1 style= 'text-align: center; color:'red'>Center and Colored Heading</h1>", unsafe_allow_html= True)

st.text("Writing")

st.info("This is for your information")
st.warning("Check before you upload")
st.error("Division by zero")
st.success("You have successfully uploaded")

ch=st.radio("Pick a color",["Black","White"])
st.write("You Choosed", ch)

agree = st.checkbox("I agree")

if agree:
    st.write("Great, you agree!")
else:
    st.write("Oh oh! You Don't agree")

# localhost:8501
# streamlit run app.py
# python -m streamlit run app.py