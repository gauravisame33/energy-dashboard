import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="VIT Energy Dashboard", layout="wide")

# ----- STYLE -----

st.markdown("""

<style>
body {background-color: #0E1117; color: white;}
h1, h2, h3 {color: #00FFAA;}
</style>

""", unsafe_allow_html=True)

# Sidebar

st.sidebar.title("⚡ VIT Energy Dashboard")
page = st.sidebar.radio("Navigate", ["Dashboard", "Insights", "Sustainability"])

# Data

data = pd.DataFrame({
"Area": ["M Block", "Old Building", "Library", "Hostel"],
"Energy": [3000, 2200, 1800, 1460],
"CO2": [1500, 1200, 1000, 1061]
})

# ---------------- DASHBOARD ----------------

if page == "Dashboard": st.markdown("## ⚡ VIT Campus Energy Utility & Sustainability Dashboard")

if page == "Dashboard": col1, col2, col3, col4 = st.columns(4)
if page == "Dashboard": col1.metric("🔋 Total Energy (kWh/day)", "8460")
if page == "Dashboard": col2.metric("☀️ Solar Share (%)", "31%")
if page == "Dashboard": col3.metric("🌍 CO₂ Emissions (kg/day)", "4761")
if page == "Dashboard": col4.metric("👥 Avg Occupancy", "54%")

# Banner

if page == "Dashboard": st.image("https://images.unsplash.com/photo-1509395176047-4a66953fd231", use_column_width=True)

# Alerts

if page == "Dashboard" and 8460 > 8000: st.warning("⚠️ High energy usage detected today!")
if page == "Dashboard" and 31 < 40: st.info("💡 Solar usage can be improved")

# Efficiency Score

if page == "Dashboard": efficiency = 100 - (4761 / 100)
if page == "Dashboard": st.progress(int(efficiency))
if page == "Dashboard": st.write(f"⚡ Energy Efficiency Score: {int(efficiency)}%")

# Charts

if page == "Dashboard": st.subheader("📊 Energy Consumption by Area")
if page == "Dashboard": st.plotly_chart(px.bar(data, x="Area", y="Energy"), use_container_width=True)

if page == "Dashboard": st.subheader("☀️ Solar vs Grid Split")
if page == "Dashboard": st.plotly_chart(px.pie(values=[31,69], names=["Solar","Grid"]))

if page == "Dashboard": st.subheader("🌱 CO₂ Emissions by Area")
if page == "Dashboard": st.plotly_chart(px.bar(data, x="Area", y="CO2"), use_container_width=True)

# Selector

if page == "Dashboard": selected = st.selectbox("Select Building", data["Area"])
if page == "Dashboard": st.write(data[data["Area"] == selected])

# ---------------- INSIGHTS ----------------

if page == "Insights": st.title("🧠 Key Insights & Observations")

if page == "Insights": st.markdown("""
• M Block shows the highest energy consumption due to labs and events
• Lower floors maintain consistent power usage throughout the day
• Solar energy helps reduce dependence on grid electricity
• Older buildings can improve efficiency with retrofitting
""")

# Smart insights

if page == "Insights": st.subheader("🔍 Smart Insight Engine")
if page == "Insights": st.write("M Block requires optimization due to high demand")
if page == "Insights": st.write("Solar integration is performing efficiently")

# ---------------- SUSTAINABILITY ----------------

if page == "Sustainability": st.title("📌 Long-Term Sustainability Plan")

if page == "Sustainability": st.metric("🌱 Sustainability Score", "75/100")

if page == "Sustainability": st.markdown("""
• Expand rooftop solar installations across campus
• Install smart meters for real-time monitoring
• Use AI-based HVAC systems for energy optimization
• Implement sensor-based lighting systems
• Goal: Achieve net-zero energy campus by 2035
""")

if page == "Sustainability": st.download_button("Download Plan", "Sustainability Plan", file_name="plan.txt")
