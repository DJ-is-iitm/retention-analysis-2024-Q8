# analysis.py
# Author: Ashish Kumar Yadav
# Email: 24f1002855@ds.study.iitm.ac.in
#
# Processes quarterly MRR growth data, computes average, and generates a
# comparison chart vs industry target (15). Saves chart as 'trend.png'.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data: Quarterly MRR growth (percent)
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "MRR_Growth": [69.02, 68.11, 75.98, 75.22]
}

df = pd.DataFrame(data)

# Compute average and print (should be 7.21)
average = df["MRR_Growth"].mean()
print(f"Average MRR Growth: {average:.2f}")  # Expect 7.21

# Add industry benchmark
industry_target = 15.0

# Styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Plot
plt.figure(figsize=(8, 8))             # 8x8 in @ dpi=64 -> 512x512 px
ax = sns.lineplot(data=df, x="Quarter", y="MRR_Growth", marker="o", linewidth=3)
ax.axhline(industry_target, color="red", linestyle="--", linewidth=2, label=f"Industry Target ({industry_target})")

# Annotate points
for i, row in df.iterrows():
    ax.text(i, row["MRR_Growth"] + 0.6, f"{row['MRR_Growth']:.2f}", ha="center", fontsize=12)

# Labels and title
ax.set_title("Quarterly MRR Growth vs Industry Target", fontsize=18, weight="bold")
ax.set_ylabel("MRR Growth (%)")
ax.set_ylim(0, max(df["MRR_Growth"].max(), industry_target) * 1.12)
ax.legend()

# Save exact 512x512 PNG
plt.tight_layout()
plt.savefig("trend.png", dpi=64, bbox_inches="tight", pad_inches=0)
plt.close()
