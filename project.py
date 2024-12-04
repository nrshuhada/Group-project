import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Homepage"
)

st.markdown("# :sunflower: PROJECT :sunflower:")
st.markdown("# :heart: NUR SHUHADA")
st.markdown("# :heart: NURUL IZZATUL BALQIS")
st.markdown("# :heart: SITI RAHIMAH")
st.markdown("# :heart: NUR SYAMIMI")
data2 = pd.read_csv("dataset.csv")
st.subheader('Data Overview')
st.dataframe(data2)

# Read CSV file directly
data = pd.read_csv("transformed_dataset.csv")

#st.dataframe(data)

# Display the DataFrame
st.subheader("Data Cleaning")

st.dataframe(data)



