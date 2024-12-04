import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
data = pd.read_csv("transformed_dataset.csv")  
analysis = data.copy()

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
    value=(int(data['AGE'].min()), int(data['AGE'].max()))  # Default range: entire data range
)

# Apply age filter
filtered_data = filtered_data[(filtered_data['AGE'] >= age_range[0]) & (filtered_data['AGE'] <= age_range[1])]

# Copy filtered data to avoid warnings
filtered_data = filtered_data.copy()

st.header("Visualizations Based on Selected Filters")

# Create AGE_GROUP column for visualization
filtered_data['AGE_GROUP'] = pd.cut(filtered_data['AGE'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
labels=["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-100"])


# Group the filtered data by AGE_GROUP and SEX
grouped_data = filtered_data.groupby(['AGE_GROUP', 'SEX']).size().unstack(fill_value=0)

# Plotting the grouped bar chart using matplotlib
fig, ax = plt.subplots(figsize=(10, 6))  # Set the size of the plot
grouped_data.plot(kind='bar', ax=ax, color=['skyblue', 'lightcoral'], width=0.8)

# Adding labels and title
ax.set_title('Distribution of COVID-19 Cases by Gender & Age Group', fontsize=14)
ax.set_xlabel('Age Group', fontsize=12)
ax.set_ylabel('Number of Cases', fontsize=12)

# Displaying the x-axis ticks for age groups
ax.set_xticklabels(grouped_data.index, rotation=45)

# Adding legend for gender
ax.legend(['Female', 'Male'], title='Gender')

# Ensure everything fits well
plt.tight_layout()

# Display the chart in Streamlit
st.pyplot(fig)