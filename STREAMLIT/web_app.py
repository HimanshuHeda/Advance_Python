import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
from PIL import Image

# Configure Streamlit Page
st.set_page_config(page_title="🚀 Interactive Web App", page_icon="🌍", layout="wide")

# Title & Description
st.title("🌟 Welcome to the Interactive Web Page 🌟")
st.write("Explore the **AI Chatbot, Data Visualization**, and **Image Upload** features.")

# Sidebar Navigation
st.sidebar.header("📌 Navigation")
page = st.sidebar.radio("Select a page", ["🏠 Home", "💬 Chatbot", "📊 Data Visualization", "🖼 Upload Image"])

# --- Home Page ---
if page == "🏠 Home":
    st.subheader("🚀 Explore the Features!")
    st.markdown("""
    - 💬 **AI Chatbot**: Ask any question and receive an AI-generated response.
    - 📊 **Data Visualization**: Explore interactive charts with both **sample & random data**.
    - 🖼 **Upload Image**: Upload and view an image directly.
    """)
    
    # Display an image from the internet
    st.image("https://source.unsplash.com/800x400/?technology,ai", caption="Technology & AI", use_container_width=True)
    st.success("Use the sidebar to navigate through different features!")

# --- Chatbot Page ---
elif page == "💬 Chatbot":
    st.subheader("💬 AI Chatbot - Ask Me Anything!")
    user_input = st.text_input("🤖 Type your question below:")

    if st.button("Get Response"):
        responses = [
            "That's an interesting question! 🤔",
            "I'm still learning, but that's a great thought!",
            "Can you clarify? I'd love to give you a better answer!",
            "Hmm... I'll have to think about that! 🤖"
        ]
        if user_input:
            st.info(f"🤖 AI says: {random.choice(responses)}")
        else:
            st.warning("Please enter a question before clicking the button!")

# --- Data Visualization Page ---
elif page == "📊 Data Visualization":
    st.subheader("📊 Interactive Data Visualization")

    # Option to generate random data
    data_option = st.radio("Choose Data Type:", ["Sample Data", "Random Data"])

    if data_option == "Sample Data":
        data = pd.DataFrame({
            'Category': ['A', 'B', 'C', 'D'],
            'Values': [10, 25, 15, 30]
        })
    else:
        data = pd.DataFrame({
            'Category': ['A', 'B', 'C', 'D', 'E'],
            'Values': [random.randint(10, 100) for _ in range(5)]
        })

    # Display Data Table
    st.write("### 📋 Data Table:")
    st.dataframe(data)

    # Generate Bar Chart
    st.write("### 📊 Bar Chart:")
    fig, ax = plt.subplots()
    ax.bar(data['Category'], data['Values'], color=['blue', 'green', 'red', 'purple', 'orange'])
    plt.xlabel("Category")
    plt.ylabel("Values")
    plt.title("Data Visualization")
    st.pyplot(fig)

# --- Image Upload Page ---
elif page == "🖼 Upload Image":
    st.subheader("🖼 Upload and View Your Image")
    uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_container_width=True)

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.info("🔧 Built with ❤️ using Streamlit")

