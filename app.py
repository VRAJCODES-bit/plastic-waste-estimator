"""
Plastic Waste Estimator — Streamlit Version
Interactive web app estimating yearly plastic waste footprint based on consumption habits.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import json
import os

st.set_page_config(page_title="Plastic Waste Estimator", page_icon="🌊", layout="centered")

st.title("🌊 Plastic Waste Estimator")
st.caption("Estimate your yearly plastic waste footprint based on everyday habits.")

FACTORS = {
    "water_bottles": 12,
    "plastic_bags": 8,
    "food_delivery": 45,
    "packaged_snacks": 5,
    "takeaway_cups": 10,
    "clothing_items": 150,
    "electronics_packaging": 80,
    "personal_care_items": 25,
}

BENCHMARKS = {
    "Global Average": 11.0,
    "India Average": 8.0,
    "Ahmedabad (est.)": 7.5,
    "Delhi (est.)": 9.5,
    "Mumbai (est.)": 10.0,
    "US Average": 22.0,
    "EU Average": 14.5,
}

HISTORY_FILE = "plastic_footprint_history.json"


def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_history(history):
    try:
        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f)
    except IOError:
        st.warning("Could not save history to disk — it will only persist for this session.")


if "history" not in st.session_state:
    st.session_state.history = load_history()

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
st.write(f"Your footprint is closest to **{closest_benchmark[0]}** ({closest_benchmark[1]} kg/year).")

# ---------------------------
# Track footprint over time (persisted to disk)
# ---------------------------
st.markdown("---")
st.markdown("### 📈 Track Your Progress")

if st.button("💾 Save this estimate to my history"):
    st.session_state.history.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "annual_kg": round(annual_kg, 2),
    })
    save_history(st.session_state.history)
    st.success("Saved! Your history now persists across sessions.")

if st.session_state.history:
    history_df = pd.DataFrame(st.session_state.history)
    st.line_chart(history_df.set_index("date"))
    st.dataframe(history_df, use_container_width=True)

    csv_data = history_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download history as CSV",
        data=csv_data,
        file_name="plastic_footprint_history.csv",
        mime="text/csv",
    )

    if st.button("🗑️ Clear my history"):
        st.session_state.history = []
        save_history([])
        st.rerun()
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