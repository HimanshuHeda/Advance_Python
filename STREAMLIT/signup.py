import streamlit as st
import re

st.title("Sign Up")



user_name=st.text_input("Enter Your Name ",key="name",placeholder="User-Name")

if user_name:
    if any(char.isdigit() for char in user_name):
        st.error("User-name cannot have Numbers")
    elif re.search(r'[^a-zA-Z\s]', user_name):
        st.error("User-name cannot have Special Characters")
    



user_email=st.text_input("Email-ID ",key="email")

if user_email:
    if not bool(re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', user_email)):
        st.error("Invalid Email")



country_codes = {
    "🇮🇳 India": "+91",
    "🇺🇸 USA": "+1",
    "🇬🇧 UK": "+44",
    "🇦🇺 Australia": "+61",
    "🇨🇦 Canada": "+1",
    "🇩🇪 Germany": "+49",
    "🇫🇷 France": "+33"
}
options = ["Select your country..."] + list(country_codes.keys())
selected_country = st.selectbox("Country:",options,index=0)
if selected_country!=options[0]:
    st.success(f"Country Code for {selected_country}: *{country_codes[selected_country]}*")


user_phone=st.text_input("Phone Number : ",key="phone",placeholder="0123456789")
if user_phone:
    if not bool(re.fullmatch(r'^[0-9]{10,12}$',user_phone)):
        st.error("Invalid Phone Number")

states = ["",
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", 
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", 
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", 
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

user_state=st.selectbox("State",states,index=0)

assam_districts = ["",
    "Baksa", "Barpeta", "Biswanath", "Bongaigaon", "Cachar", 
    "Charaideo", "Chirang", "Darrang", "Dhemaji", "Dhubri", 
    "Dibrugarh", "Dima Hasao", "Goalpara", "Golaghat", "Hailakandi", 
    "Hojai", "Jorhat", "Kamrup", "Kamrup Metropolitan", "Karbi Anglong", 
    "Karimganj", "Kokrajhar", "Lakhimpur", "Majuli", "Morigaon", 
    "Nagaon", "Nalbari", "Sivasagar", "Sonitpur", "South Salmara-Mankachar", 
    "Tinsukia", "Udalguri", "West Karbi Anglong"
]

assam_cities = ["",
    "Guwahati", "Dibrugarh", "Silchar", "Jorhat", "Nagaon",
    "Tinsukia", "Tezpur", "Diphu", "Karimganj", "Golaghat",
    "Sivasagar", "Dhubri", "Lakhimpur", "Barpeta", "Bongaigaon",
    "Hailakandi", "North Lakhimpur", "Kokrajhar", "Goalpara", "Udalguri"
]



user_district=st.selectbox("District",assam_districts,index=0)
user_city=st.selectbox("City",assam_cities,index=0)
