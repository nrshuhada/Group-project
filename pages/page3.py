import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
import streamlit as st

# Create a copy of the dataset for analysis
data = pd.read_csv("transformed_dataset.csv")
analysis = data.copy()



# Visualizations
st.header("Visualizations Based on Selected Filters")


intubated_patients = data['INTUBATED'].value_counts()

# Plot: Bar chart of COVID-19 cases by age group
st.markdown("### COVID-19 Cases by Age Group")
fig, ax = plt.subplots()
intubated_patients.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('COVID-19 Cases by Age Group (Filtered)', fontsize=14)
ax.set_xlabel('Intubation Status', fontsize=12)
ax.set_ylabel('Number of Patients', fontsize=12)
st.pyplot(fig)