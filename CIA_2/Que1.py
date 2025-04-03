import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("🐱 Kitten Data Analysis Dashboard")

# Load the dataset
data = pd.read_csv("./big_kitten_dataset.csv")

# Display the dataset preview
st.subheader("Dataset Preview")
st.write(data.head())

# 1. Bar chart: Breed vs Average Energy Level
st.subheader("Bar Chart: Breed vs Average Energy Level")
avg_energy = data.groupby("Breed")["Energy_Level"].mean()
st.bar_chart(avg_energy)

# 2. Pie chart: Favorite Toy Distribution
st.subheader("Pie Chart: Favorite Toy Distribution")
toy_distribution = data["Favorite_Toy"].value_counts()
fig, ax = plt.subplots()
ax.pie(toy_distribution, labels=toy_distribution.index, autopct="%1.1f%%", startangle=90)
ax.set_title("Favorite Toy Distribution")
st.pyplot(fig)

# 3. Line graph: Age (Months) vs Weight (kg)
st.subheader("Line Graph: Age (Months) vs Weight (kg)")
data_sorted = data.sort_values("Age_Months")
fig, ax = plt.subplots()
ax.plot(data_sorted["Age_Months"], data_sorted["Weight_kg"], marker="o", color="green")
ax.set_xlabel("Age (Months)")
ax.set_ylabel("Weight (kg)")
ax.set_title("Age (Months) vs Weight (kg)")
st.pyplot(fig)

# 4. Insights
st.subheader("Insights")
highest_energy_breed = avg_energy.idxmax()
most_favorite_toy = toy_distribution.idxmax()
min_weight_age = data.loc[data["Weight_kg"].idxmin(), "Age_Months"]
max_weight_age = data.loc[data["Weight_kg"].idxmax(), "Age_Months"]

st.write(f"Breed with the highest average Energy Level: **{highest_energy_breed}**")
st.write(f"Most favorite toy: **{most_favorite_toy}**")
st.write(f"Age with the least weight: **{min_weight_age} months**")
st.write(f"Age with the most weight: **{max_weight_age} months**")