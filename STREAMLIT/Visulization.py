import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("📊 Interactive Data Filtering and Visualization")

# Load dataset
data = pd.read_csv("./marksheet.csv")  # Replace with your dataset path

# Display the dataset
st.subheader("Dataset Preview")
st.write(data.head())

# Filter options
st.sidebar.header("Filter Options")
columns = data.columns.tolist()

# Select column for filtering
filter_column = st.sidebar.selectbox("Select a column to filter", columns)

# Get unique values from the selected column
unique_values = data[filter_column].unique()

# Multi-select filter
selected_values = st.sidebar.multiselect(f"Select values for {filter_column}", unique_values, default=unique_values)

# Filter the data
filtered_data = data[data[filter_column].isin(selected_values)]

# Display filtered data
st.subheader("Filtered Data")
st.write(filtered_data)

# Visualization options
st.sidebar.header("Visualization Options")
chart_type = st.sidebar.radio("Choose Chart Type", ["Pie Chart", "Bar Chart"])

# Visualization
st.subheader("Visualization")
fig, ax = plt.subplots(figsize=(8, 5))

if chart_type == "Pie Chart":
    # Pie chart for the selected column
    pie_data = filtered_data[filter_column].value_counts()
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax.set_title(f"Pie Chart of {filter_column}")

elif chart_type == "Bar Chart":
    # Bar chart for the selected column
    bar_data = filtered_data[filter_column].value_counts()
    ax.bar(bar_data.index, bar_data.values, color="skyblue")
    ax.set_title(f"Bar Chart of {filter_column}")
    ax.set_xlabel(filter_column)
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)

# Display the chart
st.pyplot(fig)