"""
Plastic Waste Estimator — Streamlit Version
Interactive web app estimating yearly plastic waste footprint based on consumption habits.
"""

import streamlit as st

st.set_page_config(page_title="Plastic Waste Estimator", page_icon="🌊", layout="centered")

st.title("🌊 Plastic Waste Estimator")
st.caption("Estimate your yearly plastic waste footprint based on everyday habits.")

FACTORS = {
    "water_bottles": 12,
    "plastic_bags": 8,
    "food_delivery": 45,
    "packaged_snacks": 5,
    "takeaway_cups": 10,
}

st.markdown("### Your Weekly Habits")

col1, col2 = st.columns(2)
with col1:
    water_bottles = st.slider("🧴 Single-use water bottles per week", 0, 30, 5)
    plastic_bags = st.slider("🛍️ Plastic shopping bags per week", 0, 20, 3)
    food_delivery = st.slider("🥡 Food delivery orders per week", 0, 15, 2)

with col2:
    packaged_snacks = st.slider("🍫 Packaged snacks/wrappers per week", 0, 30, 7)
    takeaway_cups = st.slider("☕ Takeaway cups per week", 0, 20, 4)

weekly_grams = (
    water_bottles * FACTORS["water_bottles"]
    + plastic_bags * FACTORS["plastic_bags"]
    + food_delivery * FACTORS["food_delivery"]
    + packaged_snacks * FACTORS["packaged_snacks"]
    + takeaway_cups * FACTORS["takeaway_cups"]
)
annual_grams = weekly_grams * 52
annual_kg = annual_grams / 1000

st.markdown("---")
st.markdown("### 📊 Your Plastic Footprint")

col1, col2 = st.columns(2)
col1.metric("Weekly Waste", f"{weekly_grams:.0f} g")
col2.metric("Annual Waste", f"{annual_kg:.2f} kg")

bottles_equivalent = annual_grams / FACTORS["water_bottles"]
body_weight_pct = (annual_kg / 70) * 100

st.write(f"🧴 That's roughly **{bottles_equivalent:.0f} single-use water bottles** worth of plastic.")
st.write(f"⚖️ Or about **{body_weight_pct:.1f}%** of an average adult's body weight in plastic.")

if annual_kg < 5:
    st.success("Footprint Level: **LOW** — Great job minimizing plastic use!")
elif annual_kg < 15:
    st.info("Footprint Level: **MODERATE** — Room to cut back on single-use plastics.")
elif annual_kg < 30:
    st.warning("Footprint Level: **HIGH** — Significant single-use plastic consumption.")
else:
    st.error("Footprint Level: **VERY HIGH** — Consider major lifestyle changes to reduce plastic waste.")

st.markdown("---")
st.markdown("### 💡 Tips to Reduce Your Footprint")
tips = [
    "Carry a reusable water bottle instead of buying single-use ones",
    "Bring your own bags when shopping",
    "Choose restaurants/delivery apps that use eco-friendly packaging",
    "Buy snacks in bulk instead of individually wrapped portions",
    "Carry a reusable cup for coffee/tea on the go",
]
for tip in tips:
    st.write(f"• {tip}")