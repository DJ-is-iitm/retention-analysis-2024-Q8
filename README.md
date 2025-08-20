# Customer Retention Rate — 2024 Quarterly Analysis

**Contact / Verification:** 24f1002241@ds.study.iitm.ac.in

## Data (Customer Retention Rate - 2024 Quarterly)
- Q1: 69.02  
- Q2: 68.11  
- Q3: 75.98  
- Q4: 75.22  

**Average: 72.08**

**Industry Target:** 85

---

## Key Findings
1. The company’s average retention for 2024 is **72.08%**, which is **12.92 percentage points below** the industry target (85%).
2. There is a clear dip in Q1–Q2 (≈69%), followed by recovery in Q3–Q4 (≈76%).
3. The improvement in Q3 & Q4 suggests seasonal or campaign-related gains, but still not sufficient to meet the benchmark.

---

## Business Implications
- Current retention levels are below industry norms; this gap likely translates to lost long-term revenue and higher acquisition costs.
- The Q3–Q4 improvement shows interventions can move the metric — but interventions must be scaled and targeted.

---

## Recommended Actions (Solution: implement targeted retention campaigns)
**Primary solution:** implement targeted retention campaigns focusing on at-risk cohorts.

Actionable recommendations:
1. **Segment customers** by tenure, engagement, and recent activity to identify at-risk groups (e.g., recently downgraded users or users with low engagement).
2. **Design targeted offers**: personalized outreach, discounts, and product nudges tailored to different segments (win-back campaigns, loyalty incentives).
3. **Operationalize lifecycle campaigns**: onboarding improvement for new users, proactive escalation for mid-tenure users, and win-back for those showing churn signals.
4. **A/B test campaign variants** and track lift on retention measured at 30/90/180 day horizons.
5. **Set OKRs**: aim to reduce churn by X% per quarter and increase retention by 3–5 percentage points in the next 2 quarters as an incremental target toward 85.
6. **Monitor & iterate** with dashboards tracking retention by cohort, campaign lift, and cost-per-retained-customer.

---

## Visualizations included
- `retention_trend.png` — quarterly trend with industry target and average annotated
- `retention_vs_benchmark.png` — side-by-side average vs target

---

## How to reproduce locally
1. Clone the repo.
2. Create a Python environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   pip install pandas numpy matplotlib seaborn
