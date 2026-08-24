# Plastic Waste Estimator

A tool that estimates your household's yearly plastic waste footprint based on everyday consumption habits — single-use bottles, bags, food delivery packaging, snack wrappers, takeaway cups, clothing, electronics packaging, and personal care products.

🔗 [Try it live](https://plastic-waste-estimator-adovdgvt7bh7vr6xkavipq.streamlit.app)

## Features

- 🧴 Estimates footprint across 8 categories of everyday plastic consumption
- 📊 Instant weekly/annual footprint calculation with fun real-world comparisons
- 🌍 Regional benchmark comparison (Global, India, Ahmedabad, Delhi, Mumbai, US, EU averages)
- 📈 Progress tracking that persists across sessions, with a trend chart
- ⬇️ Export your tracked history as a CSV file
- 💡 Practical, actionable tips to reduce your footprint

## How it works

The tool asks about your weekly and monthly habits across plastic-heavy categories, applies research-based average weight estimates per item, and calculates your annual plastic footprint in kilograms. It classifies your footprint level, compares it against regional benchmarks, and offers practical reduction tips.

## Usage

### Web app (Streamlit)

Just open the [live app](https://plastic-waste-estimator-adovdgvt7bh7vr6xkavipq.streamlit.app) — no installation needed. Adjust the sliders for your habits and see your footprint update instantly.

### Run locally

```bash
git clone https://github.com/VRAJCODES-bit/plastic-waste-estimator.git
cd plastic-waste-estimator
pip install -r requirements.txt
streamlit run app.py
```

### CLI version

A simpler command-line version is also included:

```bash
python main.py
```

Answer the prompts about your weekly habits (or press Enter to accept the default shown).

## Example output
Weekly plastic waste: 885 grams
Annual plastic waste: 46.02 kg (46020 grams)

That's roughly equivalent to:
🧴 3835 single-use water bottles worth of plastic
⚖️ 65.7% of an average adult's body weight in plastic

Footprint Level: VERY HIGH — Consider major lifestyle changes to reduce plastic waste.


## Note on history persistence

Progress history is saved to a local file on the server, so it persists across your visits within the same deployment. However, Streamlit Cloud's filesystem is not permanent storage — history may reset if the app redeploys or restarts after extended inactivity. For guaranteed long-term tracking, use the CSV export feature to save your own copy.

## Tech stack

- Streamlit
- Pandas
- Pure Python (CLI version has no external dependencies)

## Future improvements

- Move history storage to a proper database (e.g., Supabase, SQLite with persistent volume) for guaranteed durability
- Add more granular, data-backed regional benchmarks (currently illustrative estimates)
- Add a comparison view showing footprint trend against benchmark over time, not just a single snapshot