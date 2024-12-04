import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
df = pd.read_csv('dataset.csv')

# List of disease columns
disease_columns = [
    'DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 'HYPERTENSION', 'CARDIOVASCULAR', 
    'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO'
]

# Filter the dataset to include only deceased patients (date_of_death is not null)
deceased_patients = df[df['DATE_OF_DEATH'].notna()]

# Count the number of deceased patients with each disease
disease_counts = deceased_patients[disease_columns].sum()

# Streamlit header and description
st.title("Analysis of Common Diseases Among Deceased Patients")
st.write("This chart shows the number of deceased patients who had each disease.")

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
disease_counts.plot(kind='bar', color='lightcoral', edgecolor='black', ax=ax)

# Adding titles and labels
ax.set_title('Common Diseases Among Deceased Patients')
ax.set_xlabel('Disease')
ax.set_ylabel('Number of Deceased Patients')
ax.set_xticklabels(disease_counts.index, rotation=45)

# Show the plot in Streamlit
plt.tight_layout()
st.pyplot(fig)

