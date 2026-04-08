import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup

st.set_page_config(page_title="Renewable Energy Dashboard", layout="wide")

# Sidebar

st.sidebar.title("⚡ Energy Management System")
page = st.sidebar.radio("Navigate", ["Home", "Dashboard", "Analysis", "Data Explorer", "Report"])

# Sample Data

data = pd.DataFrame({
"Year": [2018, 2019, 2020, 2021, 2022, 2023],
"Solar": [20, 30, 45, 60, 80, 100],
"Wind": [25, 35, 50, 65, 85, 110],
"Hydro": [40, 45, 50, 55, 60, 70]
})

# ---------------- HOME ----------------

if page == "Home":
st.markdown("<h1 style='color:#00FFAA;'>🌱 Renewable Energy Management System</h1>", unsafe_allow_html=True)

```
st.write("""
This platform provides an overview of modern renewable energy systems and their role in reducing environmental impact. 
It focuses on sustainable energy sources such as solar, wind, and hydropower.

The objective is to highlight how efficient energy management strategies can support long-term sustainability 
while meeting increasing energy demands.
""")

col1, col2, col3 = st.columns(3)
col1.metric("Solar Adoption", "↑ 120%")
col2.metric("Wind Contribution", "↑ 95%")
col3.metric("Emission Reduction", "↓ 40%")

st.image("https://images.unsplash.com/photo-1509395176047-4a66953fd231")
```

# ---------------- DASHBOARD ----------------

elif page == "Dashboard":
st.title("📊 Energy Generation Overview")

```
st.write("""
This section visualizes energy production trends across different renewable sources. 
It helps in identifying growth patterns and comparing contributions from solar, wind, and hydro energy.
""")

fig = px.line(data, x="Year", y=["Solar", "Wind", "Hydro"], markers=True)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Energy Distribution")
pie = px.pie(values=[100, 110, 70], names=["Solar", "Wind", "Hydro"])
st.plotly_chart(pie)
```

# ---------------- ANALYSIS ----------------

elif page == "Analysis":
st.title("🔍 Energy Consumption Analysis")

```
st.write("""
This tool allows users to estimate their energy usage and understand cost implications. 
It also demonstrates how increasing renewable energy usage can help reduce carbon footprint.
""")

usage = st.slider("Energy Usage (kWh)", 100, 1000, 500)
cost = usage * 0.12

st.write(f"💰 Estimated Energy Cost: ₹{cost}")

renewable = st.slider("Renewable Energy Usage (%)", 0, 100, 50)
reduction = renewable * 0.5

st.success(f"🌿 Estimated CO₂ Reduction: {reduction}%")
```

# ---------------- DATA EXPLORER ----------------

elif page == "Data Explorer":
st.title("📁 Data Exploration")

```
st.write("""
Users can upload their own datasets to analyze energy consumption patterns. 
This feature enables interactive visualization and better decision-making through data insights.
""")

file = st.file_uploader("Upload CSV File")

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df)

    column = st.selectbox("Select column to visualize", df.columns)
    fig = px.histogram(df, x=column)
    st.plotly_chart(fig)
```

# ---------------- REPORT ----------------

elif page == "Report":
st.title("📄 Energy Insights Report")

```
st.markdown("""
### Overview:
Renewable energy sources are playing a vital role in fulfilling global energy requirements.

### Key Observations:
- Solar energy capacity is increasing rapidly  
- Wind energy is becoming more efficient and widespread  
- Hydropower continues to provide stable output  

### Conclusion:
The shift towards renewable energy combined with effective management practices 
can ensure a sustainable and environmentally friendly future.
""")

st.download_button("Download Report", "Renewable Energy Report", file_name="report.txt")
```
