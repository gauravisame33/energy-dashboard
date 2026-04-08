import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Energy Dashboard", layout="wide")

# Sidebar

st.sidebar.title("⚡ Energy Dashboard")
page = st.sidebar.radio("Navigate", ["Home", "Dashboard", "Analysis", "Data"])

# Data

data = pd.DataFrame({
"Year": [2018, 2019, 2020, 2021, 2022, 2023],
"Solar": [20, 30, 45, 60, 80, 100],
"Wind": [25, 35, 50, 65, 85, 110],
"Hydro": [40, 45, 50, 55, 60, 70]
})

# Home Page

if page == "Home":
st.title("🌱 Renewable Energy Dashboard")
st.write("Clean Energy for a Better Future")

# Dashboard Page

elif page == "Dashboard":
st.title("📊 Energy Trends")
fig = px.line(data, x="Year", y=["Solar", "Wind", "Hydro"])
st.plotly_chart(fig, use_container_width=True)

# Analysis Page

elif page == "Analysis":
st.title("🔍 Energy Calculator")
usage = st.slider("Energy Usage", 100, 1000, 500)
cost = usage * 0.12
st.write(f"Estimated Cost: ₹{cost}")

# Data Page

elif page == "Data":
st.title("📁 Upload Data")
file = st.file_uploader("Upload CSV")

```
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df)
```
