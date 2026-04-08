import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="REM Dashboard", layout="wide")

# Sidebar

st.sidebar.title("⚡ REM System")
page = st.sidebar.radio("Navigate", ["Home", "Dashboard", "Applications", "Data Explorer", "Report"])

# Data

data = pd.DataFrame({
"Year": [2018, 2019, 2020, 2021, 2022, 2023],
"Solar": [20, 30, 45, 60, 80, 100],
"Wind": [25, 35, 50, 65, 85, 110],
"Hydro": [40, 45, 50, 55, 60, 70]
})

# ---------------- HOME ----------------

if page == "Home": st.markdown("<h1 style='color:#00FFAA;'>🌱 Renewable Energy Management (REM)</h1>", unsafe_allow_html=True)
if page == "Home": st.write("""
Renewable Energy Management focuses on the efficient use, monitoring, and control of energy generated from sustainable sources.
It plays a crucial role in reducing dependency on fossil fuels and minimizing environmental damage.

The system integrates technologies like solar panels, wind turbines, and hydropower systems to ensure optimized energy utilization
while maintaining reliability and cost-effectiveness.
""")

# ---------------- DASHBOARD ----------------

if page == "Dashboard": st.title("📊 REM System Overview")
if page == "Dashboard": st.write("""
This dashboard presents the growth and performance of different renewable energy sources.
It helps in understanding how energy production varies over time and how each source contributes to the overall system.
""")
if page == "Dashboard": st.plotly_chart(px.line(data, x="Year", y=["Solar", "Wind", "Hydro"], markers=True), use_container_width=True)
if page == "Dashboard": st.plotly_chart(px.pie(values=[100,110,70], names=["Solar","Wind","Hydro"]))

# ---------------- APPLICATIONS ----------------

if page == "Applications": st.title("⚙️ Applications of REM")
if page == "Applications": st.markdown("""

* **Smart Grids:** Enable real-time monitoring and efficient distribution of electricity
* **Solar Power Systems:** Used in residential and industrial setups for clean energy generation
* **Wind Energy Farms:** Generate large-scale electricity with minimal environmental impact
* **Hydropower Plants:** Provide consistent and reliable energy supply
* **Energy Storage Systems:** Store excess energy for later use, improving efficiency
  """)

# ---------------- DATA EXPLORER ----------------

if page == "Data Explorer": st.title("📁 Data Analysis")
if page == "Data Explorer": st.write("""
Users can upload datasets to analyze energy trends and consumption patterns.
This helps in better decision-making and understanding system performance.
""")
if page == "Data Explorer": file = st.file_uploader("Upload CSV File")

if page == "Data Explorer" and file is not None:
df = pd.read_csv(file)
st.dataframe(df)
col = st.selectbox("Select column", df.columns)
st.plotly_chart(px.histogram(df, x=col))

# ---------------- REPORT ----------------

if page == "Report": st.title("📄 REM Summary Report")
if page == "Report": st.markdown("""

### Overview:

Renewable Energy Management systems are essential for sustainable energy development.

### Key Points:

* Efficient utilization of renewable resources improves energy availability
* Integration of multiple sources increases system reliability
* Reduction in carbon emissions supports environmental protection

### Conclusion:

REM systems are a key step toward achieving a clean, efficient, and sustainable energy future.
""")
if page == "Report": st.download_button("Download Report", "REM Report Content", file_name="REM_Report.txt")
