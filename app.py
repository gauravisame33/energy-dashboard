import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.set_page_config(page_title="VIT REM Dashboard", layout="wide")

# Sidebar

st.sidebar.title("⚡ VIT Energy System")
page = st.sidebar.radio("Navigate", ["Dashboard", "Insights", "Sustainability"])

# Data

data = pd.DataFrame({
"Area": ["M Block", "Old Building", "Library", "Hostel"],
"Energy": [3000, 2200, 1800, 1460],
"CO2": [1500, 1200, 1000, 1061],
"Occupancy": [60, 50, 70, 65]
})

# ---------------- DASHBOARD ----------------

if page == "Dashboard": st.markdown("## ⚡ VIT Campus Energy Utility & Sustainability Dashboard")

# Live KPI

if page == "Dashboard": live_energy = 8460 + random.randint(-200, 200)
if page == "Dashboard": col1, col2, col3, col4 = st.columns(4)
if page == "Dashboard": col1.metric("🔋 Total Energy (kWh/day)", f"{live_energy}")
if page == "Dashboard": col2.metric("☀️ Solar Share (%)", "31%")
if page == "Dashboard": col3.metric("🌍 CO₂ Emissions (kg/day)", "4761")
if page == "Dashboard": col4.metric("👥 Avg Occupancy", "54%")

# Alerts

if page == "Dashboard" and live_energy > 8500: st.error("🚨 Critical Alert: Energy usage exceeds safe threshold!")
if page == "Dashboard" and live_energy > 8000: st.warning("⚠️ Warning: High energy consumption detected")
if page == "Dashboard" and 31 < 40: st.info("💡 Suggestion: Increase solar utilization")

# Efficiency Score

if page == "Dashboard": efficiency = int(100 - (4761 / 100))
if page == "Dashboard": st.progress(efficiency)
if page == "Dashboard": st.write(f"⚡ Energy Efficiency Score: {efficiency}%")

# Charts

if page == "Dashboard": st.subheader("📊 Energy Consumption by Area")
if page == "Dashboard": st.plotly_chart(px.bar(data, x="Area", y="Energy"), use_container_width=True)

if page == "Dashboard": st.subheader("☀️ Solar vs Grid Energy Split")
if page == "Dashboard": st.plotly_chart(px.pie(values=[31, 69], names=["Solar", "Grid"]))

if page == "Dashboard": st.subheader("📈 Occupancy vs Energy Demand")
if page == "Dashboard": st.plotly_chart(px.scatter(data, x="Occupancy", y="Energy", size="Energy"), use_container_width=True)

if page == "Dashboard": st.subheader("🌱 CO₂ Emissions by Area")
if page == "Dashboard": st.plotly_chart(px.bar(data, x="Area", y="CO2"), use_container_width=True)

# Interactive

if page == "Dashboard": selected = st.selectbox("🔍 Select Building", data["Area"])
if page == "Dashboard": st.write(data[data["Area"] == selected])

# Prediction

if page == "Dashboard": future = int(data["Energy"].mean() * 1.1)
if page == "Dashboard": st.write(f"🔮 Predicted Next Day Energy Demand: {future} kWh")

# Savings Calculator

if page == "Dashboard":
st.subheader("💰 Energy Savings Calculator")
reduction = st.slider("Reduce Usage (%)", 0, 50, 10)
saved = int(live_energy * (reduction/100))
st.success(f"Estimated Savings: {saved} kWh/day")

# Ranking

if page == "Dashboard":
st.subheader("🏆 Energy Efficiency Ranking")
st.dataframe(data.sort_values(by="Energy"))

# ---------------- INSIGHTS ----------------

if page == "Insights": st.title("🧠 Key Insights & Smart Analysis")

if page == "Insights": st.markdown("""

### 📌 Observations:

• M Block records the highest energy consumption due to lab-intensive activities
• Library and academic zones show stable usage patterns
• Solar contribution reduces dependency on conventional power sources
• Older infrastructure can benefit from energy-efficient retrofitting

### 🤖 Smart Recommendations:

• Expand solar installations on high-demand buildings
• Implement smart meters for real-time tracking
• Optimize HVAC systems using AI-based scheduling
• Introduce motion-sensor lighting in low-traffic zones
""")

# ---------------- SUSTAINABILITY ----------------

if page == "Sustainability": st.title("📌 Long-Term Sustainability Strategy")

if page == "Sustainability": st.metric("🌱 Sustainability Score", "78/100")

if page == "Sustainability":
st.subheader("🎯 Net-Zero Goal Progress")
st.progress(68)
st.write("68% progress towards achieving a net-zero energy campus")

if page == "Sustainability": st.markdown("""

### 🚀 Strategic Plan:

• Large-scale rooftop solar deployment across campus blocks
• Installation of IoT-enabled smart energy meters
• AI-driven HVAC and energy optimization systems
• Efficient lighting systems using occupancy sensors
• Continuous monitoring and data-driven decision making

### 🎯 Target:

Achieve a fully sustainable, net-zero energy campus by 2035.
""")

if page == "Sustainability": st.download_button("Download Plan", "VIT Sustainability Plan", file_name="plan.txt")
