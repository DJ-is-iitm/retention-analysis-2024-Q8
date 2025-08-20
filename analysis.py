"""
analysis.py
Customer Retention Rate - 2024 Quarterly Data analysis and visualizations.

Author / Verification: 24f1002241@ds.study.iitm.ac.in
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure output directory (repo root) is current directory
OUT_TREND = "retention_trend.png"
OUT_COMP = "retention_vs_benchmark.png"

# --------------------------
# 1) Define the quarterly data
# --------------------------
q_names = ["Q1", "Q2", "Q3", "Q4"]
q_values = [69.02, 68.11, 75.98, 75.22]  # provided
industry_target = 85.0
given_average = 72.08  # known/correct average required in README

# Build DataFrame
df = pd.DataFrame({
    "quarter": q_names,
    "retention_rate": q_values
})

# --------------------------
# 2) Compute average & validate it matches 72.08
# --------------------------
computed_avg = float(np.mean(df["retention_rate"]))
computed_avg_rounded = round(computed_avg, 2)

print(f"Computed average (raw): {computed_avg}")
print(f"Computed average (rounded 2 dp): {computed_avg_rounded}")

# Guard: make sure the rounded average matches the required 72.08
if computed_avg_rounded != given_average:
    raise SystemExit(f"ERROR: computed average {computed_avg_rounded} != required {given_average}")

# --------------------------
# 3) Create visual: trend line with benchmark
# --------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 6))
ax = plt.gca()

# Plot the quarterly retention points and connecting line
sns.lineplot(x="quarter", y="retention_rate", marker="o", linewidth=2.2, markersize=10, data=df, ax=ax)
for i, (q, val) in enumerate(zip(df["quarter"], df["retention_rate"])):
    ax.annotate(f"{val:.2f}", (i, val), textcoords="offset points", xytext=(0,8), ha="center", fontsize=10)

# Draw industry target
ax.axhline(industry_target, color="red", linestyle="--", linewidth=2, label=f"Industry Target = {industry_target}")
# Draw average
ax.axhline(computed_avg, color="green", linestyle="-.", linewidth=1.8, label=f"Average = {computed_avg_rounded}")

ax.set_ylim(60, max(industry_target + 5, df["retention_rate"].max() + 5))
ax.set_title("Customer Retention Rate — 2024 Quarterly Trend", fontsize=16, fontweight="bold")
ax.set_ylabel("Retention Rate (%)")
ax.set_xlabel("Quarter")
ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig(OUT_TREND, dpi=150)
plt.close()
print(f"Saved trend chart to {OUT_TREND}")

# --------------------------
# 4) Create visual: average vs target bar chart
# --------------------------
plt.figure(figsize=(6, 6))
bars = pd.DataFrame({
    "label": ["Average (2024)", "Industry Target"],
    "value": [computed_avg, industry_target]
})
sns.barplot(x="label", y="value", data=bars, palette=["#2ca02c", "#d62728"], edgecolor="black")
plt.ylim(0, max(industry_target + 10, computed_avg + 20))
plt.ylabel("Retention Rate (%)")
plt.title("Average Retention vs. Industry Target (2024)", fontsize=14, fontweight="bold")
for idx, row in bars.iterrows():
    plt.text(idx, row["value"] + 1.0, f"{row['value']:.2f}%", ha="center", fontsize=12)
plt.tight_layout()
plt.savefig(OUT_COMP, dpi=150)
plt.close()
print(f"Saved comparison chart to {OUT_COMP}")

# --------------------------
# 5) Print summary and recommended solution
# --------------------------
print("\nSummary:")
print(f" - Quarterly values: {q_values}")
print(f" - Computed average (rounded): {computed_avg_rounded}")
print(f" - Industry target: {industry_target}")
print("\nKey recommendation (solution): implement targeted retention campaigns")
print(" - See README.md for full data story & recommended actions.")
