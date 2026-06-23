import pandas as pd


def generate_report():

    history = pd.read_csv("history.csv")

    total_items = len(history)

    category_counts = history["Category"].value_counts()

    report = f"""
SUSTAINABILITY REPORT

Total Waste Items Analyzed: {total_items}

Waste Category Distribution:

{category_counts.to_string()}

Project Impact:
- Promotes responsible waste segregation.
- Encourages recycling awareness.
- Supports SDG 12, SDG 11, and SDG 13.
"""

    return report