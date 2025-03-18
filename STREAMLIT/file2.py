import streamlit as st

st.title("Simple Web App eith Form")

st.write("Fill out the From below and click on the submit button to see the output")

with st.form('my_form'):
    name = st.text_input('Your Name')
    email = st.text_input('Your Email')
    age = st.number_input('Your Age',min_value=18,max_value=100)
    feedback = st.text_area('Your Feedback')

    submitted = st.form_submit_button('Submit')

if submitted:
    st.success(f'Thank you {name} for your feedback')
    st.write(f'**Hello :** {name}')
    st.write(f'**Your Email :** {email}')
    st.write(f'**Your Age :** {age}')
    st.write(f'**Your Feedback :** {feedback}')