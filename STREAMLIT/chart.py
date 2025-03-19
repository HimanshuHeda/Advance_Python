import matplotlib.pyplot as plt
import pandas as pd 
import streamlit as st 

st.title("📊 Data Analysis")

data = pd.read_csv("./marksheet.csv")

st.subheader("5 Rows of there data set")
st.write(data.head())

st.subheader(" Data Summary")
st.write(data.describe())

columns = data.columns.tolist()
st.write(columns)

x_axis = st.selectbox("Select X-axis", columns, index=0)  
y_axis = st.selectbox("Select Y-axis", columns, index=1)  
chart = st.radio("Choose Chart Type", ["Line Chart", "Bar Chart", "Histogram", "Boxplot", "Pie Chart", "Area Chart", "Scatter Plot"], index=0)

fig, ax = plt.subplots(figsize=(8, 5))

if chart == "Line Chart":
    ax.plot(data[x_axis], data[y_axis], marker='o', linestyle='-')
    ax.set_title("Line Chart")  

elif chart == "Bar Chart":
    ax.bar(data[x_axis], data[y_axis], color="skyblue")
    ax.set_title("Bar Chart") 

elif chart == "Scatter Plot":  
    ax.scatter(data[x_axis], data[y_axis], color="red")
    ax.set_title("Scatter Plot") 

ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)  

st.pyplot(fig)