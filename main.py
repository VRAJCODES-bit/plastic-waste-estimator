"""
Plastic Waste Estimator
A CLI tool that estimates a household's yearly plastic waste footprint
based on everyday consumption habits.
"""

# ---------------------------
# Emission/weight factors (grams of plastic per unit, rough estimates)
# ---------------------------
FACTORS = {
    "water_bottles_per_week": 12,      # grams per bottle (500ml PET bottle)
    "plastic_bags_per_week": 8,         # grams per bag
    "food_delivery_per_week": 45,       # grams per delivery (containers + bags)
    "packaged_snacks_per_week": 5,      # grams per wrapper
    "takeaway_cups_per_week": 10,       # grams per cup (lid + cup + straw)
}


def get_number_input(prompt, default=0):
    """Safely get a numeric input from the user, falling back to default on invalid entry."""
    raw = input(f"{prompt} [{default}]: ").strip()
    if raw == "":
        return default
    try:
        return float(raw)
    except ValueError:
        print("  Invalid number, using default.")
        return default


def classify_footprint(annual_kg):
    if annual_kg < 5:
        return "LOW — Great job minimizing plastic use!"
    elif annual_kg < 15:
        return "MODERATE — Room to cut back on single-use plastics."
    elif annual_kg < 30:
        return "HIGH — Significant single-use plastic consumption."
    else:
        return "VERY HIGH — Consider major lifestyle changes to reduce plastic waste."


def main():
    print("=" * 55)
    print("   🌊 PLASTIC WASTE ESTIMATOR")
    print("=" * 55)
    print("Answer the following questions about your weekly habits.")
    print("Press Enter to accept the default shown in brackets.\n")

    water_bottles = get_number_input("Single-use water bottles per week", 5)
    plastic_bags = get_number_input("Plastic shopping bags per week", 3)
    food_delivery = get_number_input("Food delivery orders per week", 2)
    packaged_snacks = get_number_input("Packaged snacks/wrappers per week", 7)
    takeaway_cups = get_number_input("Takeaway coffee/tea cups per week", 4)

    weekly_grams = (
        water_bottles * FACTORS["water_bottles_per_week"]
        + plastic_bags * FACTORS["plastic_bags_per_week"]
        + food_delivery * FACTORS["food_delivery_per_week"]
        + packaged_snacks * FACTORS["packaged_snacks_per_week"]
        + takeaway_cups * FACTORS["takeaway_cups_per_week"]
    )

    annual_grams = weekly_grams * 52
    annual_kg = annual_grams / 1000

    print("\n" + "=" * 55)
    print("   YOUR PLASTIC WASTE FOOTPRINT")
    print("=" * 55)
    print(f"Weekly plastic waste: {weekly_grams:.0f} grams")
    print(f"Annual plastic waste: {annual_kg:.2f} kg ({annual_grams:.0f} grams)")

    # Fun comparisons
    plastic_bottles_equivalent = annual_grams / FACTORS["water_bottles_per_week"]
    body_weight_comparison = annual_kg / 70  # avg adult body weight ~70kg

    print(f"\nThat's roughly equivalent to:")
    print(f"  🧴 {plastic_bottles_equivalent:.0f} single-use water bottles worth of plastic")
    print(f"  ⚖️  {body_weight_comparison*100:.1f}% of an average adult's body weight in plastic")

    status = classify_footprint(annual_kg)
    print(f"\nFootprint Level: {status}")

    print("\n" + "=" * 55)
    print("   TIPS TO REDUCE YOUR FOOTPRINT")
    print("=" * 55)
    tips = [
        "Carry a reusable water bottle instead of buying single-use ones",
        "Bring your own bags when shopping",
        "Choose restaurants/delivery apps that use eco-friendly packaging",
        "Buy snacks in bulk instead of individually wrapped portions",
        "Carry a reusable cup for coffee/tea on the go",
    ]
    for tip in tips:
        print(f"  • {tip}")

    print("\n" + "=" * 55)


if __name__ == "__main__":
    main()