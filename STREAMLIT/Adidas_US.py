import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("📊 Adidas US Sales Data Analysis")

# Load dataset
data = pd.read_csv("./Adidas US Sales Datasets.csv")

# Clean the dataset
data.columns = data.columns.str.strip()  # Remove extra spaces from column names
data["Price per Unit"] = data["Price per Unit"].replace('[\$,]', '', regex=True).astype(float)
data["Total Sales"] = data["Total Sales"].replace('[\$,]', '', regex=True).astype(float)
data["Operating Profit"] = data["Operating Profit"].replace('[\$,]', '', regex=True).astype(float)
data["Units Sold"] = data["Units Sold"].replace('[,]', '', regex=True).astype(int)

# Display first 5 rows
st.subheader("First 5 Rows of the Dataset")
st.write(data.head())

# Data Summary
st.subheader("Data Summary")
st.write(data.describe())

# Display available columns and number of rows
columns = data.columns.tolist()
num_rows = data.shape[0]
st.write("Available Columns:", columns)
st.write("Total Rows in Dataset:", num_rows)

# Select X and Y axis
x_axis = st.selectbox("Select X-axis", columns)
y_axis = st.selectbox("Select Y-axis", columns)

# Ensure selected columns are numeric
try:
    # Convert selected columns to numeric (if possible)
    data[x_axis] = pd.to_numeric(data[x_axis], errors='coerce')
    data[y_axis] = pd.to_numeric(data[y_axis], errors='coerce')

    # Drop NaN values (avoid errors when plotting)
    data = data.dropna(subset=[x_axis, y_axis])

    # Select chart type
    chart = st.radio("Choose Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot"])

    fig, ax = plt.subplots(figsize=(8, 5))

    if chart == "Line Chart":
        # Ensure X-axis is sorted for Line Chart
        data = data.sort_values(by=x_axis)
        ax.plot(data[x_axis], data[y_axis], marker='o', linestyle='-')
        ax.set_title("Line Chart")

    elif chart == "Bar Chart":
        # Bar Chart requires categorical X-axis
        if data[x_axis].dtype == 'object' or data[x_axis].nunique() < 20:
            bar_data = data.groupby(x_axis)[y_axis].sum()
            ax.bar(bar_data.index, bar_data.values, color="skyblue")
            ax.set_title("Bar Chart")
        else:
            st.error("Bar Chart requires a categorical X-axis with fewer unique values.")

    elif chart == "Scatter Plot":
        # Scatter Plot requires numeric X and Y axes
        if pd.api.types.is_numeric_dtype(data[x_axis]) and pd.api.types.is_numeric_dtype(data[y_axis]):
            ax.scatter(data[x_axis], data[y_axis], color="red")
            ax.set_title("Scatter Plot")
        else:
            st.error("Scatter Plot requires both X-axis and Y-axis to be numeric.")

    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)

    st.pyplot(fig)

except Exception as e:
    st.error(f"An error occurred: {e}")