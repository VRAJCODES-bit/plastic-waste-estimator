"""
Plastic Waste Estimator — Streamlit Version
Interactive web app estimating yearly plastic waste footprint based on consumption habits.
"""

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Plastic Waste Estimator", page_icon="🌊", layout="centered")

st.title("🌊 Plastic Waste Estimator")
st.caption("Estimate your yearly plastic waste footprint based on everyday habits.")

FACTORS = {
    "water_bottles": 12,
    "plastic_bags": 8,
    "food_delivery": 45,
    "packaged_snacks": 5,
    "takeaway_cups": 10,
    "clothing_items": 150,       # grams of microplastic-shedding synthetic textiles per item/year equivalent, simplified to per-week proxy
    "electronics_packaging": 80,  # grams per package (avg small electronics box + wrap)
    "personal_care_items": 25,    # grams per empty container (shampoo, toothpaste tube, etc.)
}

# Regional benchmark averages (kg/year, illustrative estimates)
BENCHMARKS = {
    "Global Average": 11.0,
    "India Average": 8.0,
    "US Average": 22.0,
    "EU Average": 14.5,
}

st.markdown("### Your Weekly Habits")

col1, col2 = st.columns(2)
with col1:
    water_bottles = st.slider("🧴 Single-use water bottles per week", 0, 30, 5)
    plastic_bags = st.slider("🛍️ Plastic shopping bags per week", 0, 20, 3)
    food_delivery = st.slider("🥡 Food delivery orders per week", 0, 15, 2)
    clothing_items = st.slider("👕 New synthetic clothing items per month", 0, 10, 1)

with col2:
    packaged_snacks = st.slider("🍫 Packaged snacks/wrappers per week", 0, 30, 7)
    takeaway_cups = st.slider("☕ Takeaway cups per week", 0, 20, 4)
    electronics = st.slider("📦 New electronics/gadget packages per month", 0, 5, 0)
    personal_care = st.slider("🧴 Personal care containers used per month", 0, 15, 3)

weekly_grams = (
    water_bottles * FACTORS["water_bottles"]
    + plastic_bags * FACTORS["plastic_bags"]
    + food_delivery * FACTORS["food_delivery"]
    + packaged_snacks * FACTORS["packaged_snacks"]
    + takeaway_cups * FACTORS["takeaway_cups"]
)

monthly_extra_grams = (
    clothing_items * FACTORS["clothing_items"]
    + electronics * FACTORS["electronics_packaging"]
    + personal_care * FACTORS["personal_care_items"]
)

annual_grams = (weekly_grams * 52) + (monthly_extra_grams * 12)
annual_kg = annual_grams / 1000

st.markdown("---")
st.markdown("### 📊 Your Plastic Footprint")

col1, col2 = st.columns(2)
col1.metric("Weekly Waste (core items)", f"{weekly_grams:.0f} g")
col2.metric("Annual Waste (total)", f"{annual_kg:.2f} kg")

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

# ---------------------------
# Regional comparison benchmarks
# ---------------------------
st.markdown("---")
st.markdown("### 🌍 How You Compare")

benchmark_df = pd.DataFrame({
    "Category": list(BENCHMARKS.keys()) + ["Your Footprint"],
    "Annual kg": list(BENCHMARKS.values()) + [annual_kg],
})
st.bar_chart(benchmark_df.set_index("Category"))

closest_benchmark = min(BENCHMARKS.items(), key=lambda x: abs(x[1] - annual_kg))
st.write(f"Your footprint is closest to the **{closest_benchmark[0]}** ({closest_benchmark[1]} kg/year).")

# ---------------------------
# Track footprint over time (session-based)
# ---------------------------
st.markdown("---")
st.markdown("### 📈 Track Your Progress")

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("💾 Save this estimate to my history"):
    st.session_state.history.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "annual_kg": round(annual_kg, 2),
    })
    st.success("Saved! Scroll down to see your history.")

if st.session_state.history:
    history_df = pd.DataFrame(st.session_state.history)
    st.line_chart(history_df.set_index("date"))
    st.dataframe(history_df, use_container_width=True)
    st.caption("Note: history is saved for this browser session only and resets when you close the tab.")
else:
    st.caption("No saved estimates yet — click the button above to start tracking your progress over time.")

st.markdown("---")
st.markdown("### 💡 Tips to Reduce Your Footprint")
tips = [
    "Carry a reusable water bottle instead of buying single-use ones",
    "Bring your own bags when shopping",
    "Choose restaurants/delivery apps that use eco-friendly packaging",
    "Buy snacks in bulk instead of individually wrapped portions",
    "Carry a reusable cup for coffee/tea on the go",
    "Choose natural fiber clothing over synthetic materials when possible",
    "Buy electronics/personal care refills instead of new packaging each time",
]
for tip in tips:
    st.write(f"• {tip}")