import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
import streamlit as st

# Create a copy of the dataset for analysis
data = pd.read_csv("transformed_dataset.csv")
analysis = data.copy()


#######

###########

# Sidebar Filters
st.sidebar.header("Filter Options")

# Filter 1: Multi-Select for Sex
selected_sex = st.sidebar.multiselect(
    "Select Sex:",
    options=sorted(data['SEX'].unique()),  # Options: FEMALE, MALE, UNKNOWN
    default=sorted(data['SEX'].unique())  # Default: All selected
)

# Apply sex filter
filtered_data = data[data['SEX'].isin(selected_sex)] if selected_sex else data

# Filter 2: Slider for Age Range
age_range = st.sidebar.slider(
    "Select Age Range:",
    min_value=int(data['AGE'].min()),
    max_value=int(data['AGE'].max()),
    value=(0, 100),  # Default range
)

# Apply age filter
filtered_data = filtered_data[(filtered_data['AGE'] >= age_range[0]) & (filtered_data['AGE'] <= age_range[1])]

# Visualizations
st.header("Visualizations Based on Selected Filters")

# Bin the AGE column for grouped visualization
filtered_data['AGE_GROUP'] = pd.cut(filtered_data['AGE'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
labels=["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-100"])

# Count cases in each age group
age_group_counts = filtered_data['AGE_GROUP'].value_counts().sort_index()

# Plot: Bar chart of COVID-19 cases by age group
st.markdown("### COVID-19 Cases by Age Group")
fig, ax = plt.subplots()
age_group_counts.plot(kind='bar', color='blue', ax=ax)
ax.set_title('COVID-19 Cases by Age Group (Filtered)', fontsize=14)
ax.set_xlabel('Age Group', fontsize=12)
ax.set_ylabel('Number of Cases', fontsize=12)
st.pyplot(fig)

# Histogram: COVID-19 Cases by Age
st.markdown("### COVID-19 Cases Distribution by Age")
fig, ax = plt.subplots()
sns.histplot(
    filtered_data['AGE'], bins=20, kde=True, color='blue', ax=ax
)
ax.set_title('COVID-19 Cases by Age Group (Filtered)', fontsize=14)
ax.set_xlabel('Age', fontsize=12)
ax.set_ylabel('Number of Cases', fontsize=12)
st.pyplot(fig)