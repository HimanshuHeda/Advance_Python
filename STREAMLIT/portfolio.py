import streamlit as st

# Set Page Title
st.set_page_config(page_title="My Portfolio", page_icon="🌟", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Home Page
if page == "Home":
    st.title("Welcome to My Portfolio! 🚀")

    # Create columns for parallel layout
    col1, col2 = st.columns([1, 2])  # Adjust width ratio as needed

    with col1:
        st.image("./coder.png", width=500, use_container_width=False)  # Fixed image width

    with col2:
        st.markdown("## Hello! I am **Himanshu Heda**, a passionate developer 🚀")
        st.write("This is a simple portfolio web app built using Python and Streamlit.")
        st.success("Explore the different sections using the sidebar.")

        # About Me Section
        st.markdown("### 👋 About Me")
        st.write("""
        I am Himanshu Heda, a passionate and driven software developer with a flair for problem-solving and a love for technology. 
        I specialize in Web Design, Web Development, and Application Development, and continuously explore new avenues to expand my technical horizons. 
        My projects reflect my commitment to creating innovative and user-friendly solutions.
        """)

    # Add Skills Section Below
    st.markdown("---")  # Separator
    st.markdown("### 🚀 My Skills & Expertise")

    col3, col4 = st.columns([1, 2])  # Split for skills layout

    with col3:
        st.markdown("#### Programming Languages")
        st.markdown("""
        - **Proficient**: Python, JavaScript, C, Java  
        - **Familiar**: SQL, PHP
        """)

    with col4:
        st.markdown("#### Development Stacks")
        st.markdown("""
        - **Frontend**: HTML, CSS (Bootstrap), JavaScript, ReactJS  
        - **Backend**: Python, PHP, SQLite, MySQL  
        - **Tools & Platforms**: Git, GitHub, XAMPP Server
        """)

# About Page
elif page == "About":
    st.title("About Me")
    st.markdown("""
    - 🔭 **Tech Enthusiast & Developer**  
    - 💻 Skills: Python, JavaScript, Web Development  
    - 🌱 Currently Learning: AI & Open Source Contributions  
    - 🎯 Passion: Building impactful software solutions  
    - 📫 Connect with me on [GitHub](https://github.com/HimanshuHeda) & [Portfolio](https://himanshuheda.vercel.app/)
    """)
    st.info("I love coding and solving real-world problems through technology.")

# Contact Page
elif page == "Contact":
    st.title("Contact Me 📞")
    st.write("Feel free to reach out for collaborations or inquiries!")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.success(f"Thank you {name}, I will get back to you soon!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by Himanshu Heda</p>", unsafe_allow_html=True)
