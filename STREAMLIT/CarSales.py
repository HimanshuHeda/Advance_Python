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
Regions = data["Dealer_Region"].unique()
selected_region = st.sidebar.selectbox("Select Dealer Region", Regions)

# Filter by Car Company
Companies = data["Company"].unique()
selected_company = st.sidebar.selectbox("Select Car Company", Companies)

# Filter data based on selected options
filtered_data = data[(data["Dealer_Region"] == selected_region) & (data["Company"] == selected_company)]

# Display filtered data
st.subheader(f"Filtered Data for Region: {selected_region} and Company: {selected_company}")
st.write(filtered_data)

# Sidebar for visualization options
st.sidebar.header("Visualization Options")
chart_type = st.sidebar.radio("Choose Chart Type", ["Bar Chart", "Pie Chart", "Line Chart", "Scatter Plot", "Histogram"])

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

elif chart_type == "Line Chart":
    # Line chart for car prices over models
    ax.plot(filtered_data["Model"], filtered_data["Price ($)"], marker='o', linestyle='-', color="green")
    ax.set_title(f"Line Chart: Car Prices in {selected_region} by {selected_company}")
    ax.set_xlabel("Car Model")
    ax.set_ylabel("Price ($)")
    plt.xticks(rotation=45)

elif chart_type == "Scatter Plot":
    # Scatter plot for car prices vs annual income
    if "Annual Income" in filtered_data.columns:
        ax.scatter(filtered_data["Annual Income"], filtered_data["Price ($)"], color="red")
        ax.set_title(f"Scatter Plot: Annual Income vs Price in {selected_region} by {selected_company}")
        ax.set_xlabel("Annual Income")
        ax.set_ylabel("Price ($)")
    else:
        st.error("The 'Annual Income' column is missing in the dataset.")

elif chart_type == "Histogram":
    # Histogram for car prices
    ax.hist(filtered_data["Price ($)"], bins=10, color="purple", edgecolor="black")
    ax.set_title(f"Histogram: Car Prices in {selected_region} by {selected_company}")
    ax.set_xlabel("Price ($)")
    ax.set_ylabel("Frequency")

# Display the chart
st.pyplot(fig)

# Additional Insights
st.subheader("Additional Insights")
total_sales = filtered_data["Price ($)"].sum()
average_price = filtered_data["Price ($)"].mean()
st.write(f"**Total Sales:** ${total_sales:,.2f}")
st.write(f"**Average Price of Cars Sold:** ${average_price:,.2f}")