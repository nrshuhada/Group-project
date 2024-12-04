import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
import streamlit as st

# Create a copy of the dataset for analysis
data = pd.read_csv("dataset.csv")
analysis = data.copy()

# Sidebar Filters
st.sidebar.header("Filter Options")

# Filter 1: Multi-Select for Sex
selected_disease= st.sidebar.multiselect(
    "Select Disease:",
    options=[
    'DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 'HYPERTENSION', 'CARDIOVASCULAR', 
    'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO'])
    



# Visualizations
st.header("Visualizations Based on Selected Filters")
#############################################################################################################

# Streamlit title and description
st.title("Correlation Analysis of Diseases and ICU Admission")
st.write("This heatmap shows the correlations between various diseases and ICU admission.")

# List of disease columns and the ICU column
disease_columns = [
    'DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 'HYPERTENSION', 'CARDIOVASCULAR', 
    'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO'
]
icu_column = 'ICU'

# Check if the required columns exist
missing_columns = [col for col in selected_disease + [icu_column] if col not in analysis.columns]
if missing_columns:
    st.error(f"The following required columns are missing from the dataset: {', '.join(missing_columns)}")
else:
    # Ensure the disease columns and ICU column are numerical (0 or 1)
    analysis[selected_disease] = analysis[selected_disease].apply(pd.to_numeric, errors='coerce')
    analysis[icu_column] = pd.to_numeric(analysis[icu_column], errors='coerce')

    # Calculate the correlation matrix
    correlation_matrix = analysis[selected_disease + [icu_column]].corr()

    # Plotting the correlation heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        correlation_matrix, 
        annot=True, 
        cmap='coolwarm', 
        fmt=".2f", 
        cbar=True, 
        ax=ax
    )
    ax.set_title("Correlation Heatmap: Diseases and ICU Admission")

    # Display the heatmap in Streamlit
    st.pyplot(fig)