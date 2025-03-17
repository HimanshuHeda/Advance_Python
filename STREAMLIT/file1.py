import streamlit as st

form = st.form('my_form')

name = form.text_input('Your Name')
age = form.number_input('Your Age',min_value=0,max_value=100)
submitted = form.form_submit_button('Submit')

if submitted:
    st.write(f'Hello : {name}')
    st.write(f'You are {age} Years Old')