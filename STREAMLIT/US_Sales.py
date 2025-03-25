import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("👟 Adidas US Sales Analysis Dashboard")

# Load the dataset
data = pd.read_csv("./Adidas US Sales Datasets.csv")

# Clean the dataset
data.columns = data.columns.str.strip()  # Remove extra spaces from column names
data["Price per Unit"] = data["Price per Unit"].replace('[\$,]', '', regex=True).astype(float)
data["Total Sales"] = data["Total Sales"].replace('[\$,]', '', regex=True).astype(float)
data["Operating Profit"] = data["Operating Profit"].replace('[\$,]', '', regex=True).astype(float)
data["Units Sold"] = data["Units Sold"].replace('[,]', '', regex=True).astype(int)

# Convert Invoice Date to datetime, handling inc~onsistent formats
data["Invoice Date"] = pd.to_datetime(data["Invoice Date"], errors="coerce", infer_datetime_format=True)

# Drop rows with invalid dates
data = data.dropna(subset=["Invoice Date"])

# Display the dataset preview
st.subheader("Dataset Preview")
st.write(data.head())

# Display data summary
st.subheader("Data Summary")
st.write(data.describe())

# Sidebar for filtering options
st.sidebar.header("Filter Options")

# Filter by Region
regions = data["Region"].unique()
selected_region = st.sidebar.selectbox("Select Region", regions)

# Filter by Product
products = data["Product"].unique()
selected_product = st.sidebar.selectbox("Select Product", products)

# Filter data based on selected options
filtered_data = data[(data["Region"] == selected_region) & (data["Product"] == selected_product)]

# Display filtered data
st.subheader(f"Filtered Data for Region: {selected_region} and Product: {selected_product}")
st.write(filtered_data)

# Sidebar for visualization options
st.sidebar.header("Visualization Options")
chart_type = st.sidebar.radio("Choose Chart Type", ["Bar Chart", "Pie Chart", "Line Chart", "Scatter Plot", "Histogram"])

# Visualization
st.subheader("Visualization")
fig, ax = plt.subplots(figsize=(8, 5))

if chart_type == "Bar Chart":
    # Bar chart for sales methods
    bar_data = filtered_data["Sales Method"].value_counts()
    ax.bar(bar_data.index, bar_data.values, color="skyblue")
    ax.set_title(f"Sales Methods for {selected_product} in {selected_region}")
    ax.set_xlabel("Sales Method")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)

elif chart_type == "Pie Chart":
    # Pie chart for sales methods
    pie_data = filtered_data["Sales Method"].value_counts()
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax.set_title(f"Sales Method Distribution for {selected_product} in {selected_region}")

elif chart_type == "Line Chart":
    # Line chart for total sales over time
    line_data = filtered_data.groupby("Invoice Date")["Total Sales"].sum().sort_index()
    ax.plot(line_data.index, line_data.values, marker='o', linestyle='-', color="green")
    ax.set_title(f"Total Sales Over Time for {selected_product} in {selected_region}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Sales ($)")
    plt.xticks(rotation=45)

elif chart_type == "Scatter Plot":
    # Scatter plot for units sold vs operating profit
    ax.scatter(filtered_data["Units Sold"], filtered_data["Operating Profit"], color="red")
    ax.set_title(f"Units Sold vs Operating Profit for {selected_product} in {selected_region}")
    ax.set_xlabel("Units Sold")
    ax.set_ylabel("Operating Profit ($)")

elif chart_type == "Histogram":
    # Histogram for total sales
    ax.hist(filtered_data["Total Sales"], bins=10, color="purple", edgecolor="black")
    ax.set_title(f"Histogram: Total Sales for {selected_product} in {selected_region}")
    ax.set_xlabel("Total Sales ($)")
    ax.set_ylabel("Frequency")

# Display the chart
st.pyplot(fig)

# Additional Insights
st.subheader("Additional Insights")
total_sales = filtered_data["Total Sales"].sum()
average_price = filtered_data["Price per Unit"].mean()
st.write(f"**Total Sales:** ${total_sales:,.2f}")
st.write(f"**Average Price per Unit:** ${average_price:,.2f}")