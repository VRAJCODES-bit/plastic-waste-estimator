# Plastic Waste Estimator

A tool that estimates your household's yearly plastic waste footprint based on everyday consumption habits — single-use bottles, bags, food delivery packaging, snack wrappers, and takeaway cups.

🔗 [Try it live](https://plastic-waste-estimator-adovdgvt7bh7vr6xkavipq.streamlit.app)

## How it works

The tool asks about your weekly habits across five common single-use plastic sources, applies research-based average weight estimates per item, and calculates your annual plastic footprint in kilograms. It classifies your footprint level and offers practical reduction tips.

## Usage

### Web app (Streamlit)

Just open the [live app](https://plastic-waste-estimator-adovdgvt7bh7vr6xkavipq.streamlit.app) — no installation needed. Adjust the sliders for your weekly habits and see your footprint update instantly.

### Run locally

```bash
git clone https://github.com/VRAJCODES-bit/plastic-waste-estimator.git
cd plastic-waste-estimator
pip install -r requirements.txt
streamlit run app.py
```

### CLI version

A command-line version is also included:

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


## Tech stack

- Streamlit
- Pure Python (no other external dependencies)

## Future improvements

- Include more categories (clothing/textile plastic, electronics packaging, personal care products)
- Track footprint over time with a simple logging feature
- Add regional plastic waste comparison benchmarks