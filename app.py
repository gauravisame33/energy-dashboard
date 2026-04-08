import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="VIT Energy Dashboard", layout="wide")

# Sidebar

st.sidebar.title("⚡ VIT Energy Dashboard")
page = st.sidebar.radio("Navigate", ["Dashboard", "Insights", "Sustainability Plan"])

# ---------------- DASHBOARD ----------------

if page == "Dashboard": st.markdown("## ⚡ VIT Campus Energy Utility & Sustainability Dashboard")

# KPI Cards

if page == "Dashboard": col1, col2, col3, col4 = st.columns(4)
if page == "Dashboard": col1.metric("🔋 Total Energy (kWh/day)", "8460")
if page == "Dashboard": col2.metric("☀️ Solar Share (%)", "31%")
if page == "Dashboard": col3.metric("🌍 CO₂ Emissions (kg/day)", "4761")
if page == "Dashboard": col4.metric("👥 Avg Occupancy", "54%")

# Sample Data

data = pd.DataFrame({
"Area": ["M Block", "Old Building", "Library", "Hostel"],
"Energy": [3000, 2200, 1800, 1460],
"CO2": [1500, 1200, 1000, 1061]
})

# Charts

if page == "Dashboard": st.subheader("📊 Energy Consumption by Area")
if page == "Dashboard": st.plotly_chart(px.bar(data, x="Area", y="Energy"), use_container_width=True)

if page == "Dashboard": st.subheader("☀️ Solar vs Grid Energy Split")
if page == "Dashboard": st.plotly_chart(px.pie(values=[31, 69], names=["Solar", "Grid"]))

if page == "Dashboard": st.subheader("📈 Occupancy vs Energy Demand")
if page == "Dashboard": st.plotly_chart(px.line(data, x="Area", y="Energy", markers=True))

if page == "Dashboard": st.subheader("🌱 CO₂ Emissions by Area")
if page == "Dashboard": st.plotly_chart(px.bar(data, x="Area", y="CO2"), use_container_width=True)

# ---------------- INSIGHTS ----------------

if page == "Insights": st.title("🧠 Key Insights & Observations")

if page == "Insights": st.markdown("""
• Academic blocks such as M Block show higher energy usage due to labs and events
• Lower floors maintain consistent energy demand throughout operational hours
• Solar energy integration helps reduce dependence on conventional grid supply
• Older infrastructure has potential for energy optimization through retrofitting
""")

# ---------------- SUSTAINABILITY PLAN ----------------

if page == "Sustainability Plan": st.title("📌 Long-Term Sustainability Plan")

if page == "Sustainability Plan": st.markdown("""
• Expansion of rooftop solar installations across major campus blocks
• Deployment of smart meters for real-time energy monitoring
• Implementation of AI-based HVAC systems for efficient cooling
• Use of motion-sensor lighting in low-traffic areas
• Goal: Achieve a net-zero energy campus by 2035
""")
