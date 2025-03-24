import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("🚗 Car Sales Analysis Dashboard")

# Load the dataset
data = pd.read_csv("./Car Sales.csv")

# Display the dataset preview
st.subheader("Dataset Preview")
st.write(data.head())

# Display data summary
st.subheader("Data Summary")
st.write(data.describe())

# Sidebar for filtering options
st.sidebar.header("Filter Options")

# Filter by Dealer Region
regions = data["Dealer_Region"].unique()
selected_region = st.sidebar.selectbox("Select Dealer Region", regions)

# Filter by Car Company
companies = data["Company"].unique()
selected_company = st.sidebar.selectbox("Select Car Company", companies)

# Filter data based on selected options
filtered_data = data[(data["Dealer_Region"] == selected_region) & (data["Company"] == selected_company)]

# Display filtered data
st.subheader(f"Filtered Data for Region: {selected_region} and Company: {selected_company}")
st.write(filtered_data)

# Sidebar for visualization options
st.sidebar.header("Visualization Options")
chart_type = st.sidebar.radio("Choose Chart Type", ["Bar Chart", "Pie Chart"])

# Visualization
st.subheader("Visualization")
fig, ax = plt.subplots(figsize=(8, 5))

if chart_type == "Bar Chart":
    # Bar chart for car models
    bar_data = filtered_data["Model"].value_counts()
    ax.bar(bar_data.index, bar_data.values, color="skyblue")
    ax.set_title(f"Car Models Sold in {selected_region} by {selected_company}")
    ax.set_xlabel("Car Model")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)

elif chart_type == "Pie Chart":
    # Pie chart for car colors
    pie_data = filtered_data["Color"].value_counts()
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax.set_title(f"Car Color Distribution in {selected_region} by {selected_company}")

# Display the chart
st.pyplot(fig)

# Additional Insights
st.subheader("Additional Insights")
total_sales = filtered_data["Price ($)"].sum()
average_price = filtered_data["Price ($)"].mean()
st.write(f"**Total Sales:** ${total_sales:,.2f}")
st.write(f"**Average Price of Cars Sold:** ${average_price:,.2f}")