import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils import generate_ai_response


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Call Center Analytics",
    page_icon="📞",
    layout="wide"
)

st.title("📞 Call Center Analytics Dashboard")


# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv(r"src\Cleaned_Data.csv")


# ============================================================
# MONTH FILTER
# ============================================================

months = ["All"] + sorted(
    df["Month"].dropna().unique().tolist()
)

selected_month = st.sidebar.selectbox(
    "Select Month",
    months
)


if selected_month != "All":
    filtered_df = df[
        df["Month"] == selected_month
    ].copy()
else:
    filtered_df = df.copy()


# ============================================================
# VERIFIED BUSINESS METRICS
# ============================================================

total_calls = len(filtered_df)

total_revenue = filtered_df["Purchase"].sum()

avg_purchase = filtered_df["Purchase"].mean()

avg_rating = filtered_df["Rating"].mean()


# ============================================================
# REPRESENTATIVE ANALYSIS
# ============================================================

representative_analysis = (
    filtered_df
    .groupby("Representative")
    .agg(
        Calls=("Call number", "count"),
        Revenue=("Purchase", "sum"),
        Average_Purchase=("Purchase", "mean"),
        Average_Rating=("Rating", "mean")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)


top_rep = representative_analysis.index[0]

top_rep_revenue = representative_analysis.iloc[0]["Revenue"]

top_rep_calls = representative_analysis.iloc[0]["Calls"]

top_rep_avg_purchase = (
    representative_analysis.iloc[0]["Average_Purchase"]
)

top_rep_avg_rating = (
    representative_analysis.iloc[0]["Average_Rating"]
)


rep_revenue_percentage = (
    top_rep_revenue / total_revenue * 100
    if total_revenue != 0
    else 0
)

rep_call_percentage = (
    top_rep_calls / total_calls * 100
    if total_calls != 0
    else 0
)


# ============================================================
# CITY ANALYSIS
# ============================================================

city_analysis = (
    filtered_df
    .groupby("City")
    .agg(
        Calls=("Call number", "count"),
        Revenue=("Purchase", "sum"),
        Average_Purchase=("Purchase", "mean"),
        Average_Rating=("Rating", "mean")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)


top_city = city_analysis.index[0]

top_city_revenue = city_analysis.iloc[0]["Revenue"]

top_city_calls = city_analysis.iloc[0]["Calls"]

top_city_avg_purchase = (
    city_analysis.iloc[0]["Average_Purchase"]
)

top_city_avg_rating = (
    city_analysis.iloc[0]["Average_Rating"]
)


city_revenue_percentage = (
    top_city_revenue / total_revenue * 100
    if total_revenue != 0
    else 0
)

city_call_percentage = (
    top_city_calls / total_calls * 100
    if total_calls != 0
    else 0
)


# ============================================================
# MONTHLY ANALYSIS
# ============================================================

monthly_analysis = (
    filtered_df
    .groupby("Month")
    .agg(
        Calls=("Call number", "count"),
        Revenue=("Purchase", "sum"),
        Average_Purchase=("Purchase", "mean"),
        Average_Rating=("Rating", "mean")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)


# ============================================================
# RATING DISTRIBUTION
# ============================================================

rating_distribution = (
    filtered_df["Rating"]
    .value_counts()
    .sort_index()
)


# ============================================================
# KPI CARDS
# ============================================================

c1, c2, c3, c4 = st.columns(4)


c1.metric(
    "Total Calls",
    total_calls
)

c2.metric(
    "Revenue",
    f"₹{total_revenue:,.0f}"
)

c3.metric(
    "Avg Purchase",
    round(avg_purchase, 2)
)

c4.metric(
    "Avg Satisfaction",
    round(avg_rating, 2)
)


# ============================================================
# REPRESENTATIVE PERFORMANCE CHART
# ============================================================

rep_calls = (
    filtered_df
    .groupby("Representative")["Call number"]
    .count()
    .sort_values(
        ascending=False
    )
)


fig, ax = plt.subplots()

rep_calls.plot(
    kind="bar",
    ax=ax
)

ax.set_title(
    "Calls Handled by Representative"
)

ax.set_xlabel(
    "Representative"
)

ax.set_ylabel(
    "Number of Calls"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

st.pyplot(fig)


# ============================================================
# AI BUSINESS ANALYST
# ============================================================

st.header("🤖 AI Business Analyst")


# ============================================================
# BUSINESS INSIGHTS
# ============================================================

if st.button(
    "Generate Business Insights",
    key="business_insights"
):

    prompt = f"""
You are a Senior Data Analyst preparing a professional
business performance report.

Analyze ONLY the verified metrics calculated from the
actual Call Center dataset.

VERIFIED METRICS:

Total Calls:
{total_calls}

Total Revenue:
{total_revenue:.2f}

Average Purchase:
{avg_purchase:.2f}

Average Customer Rating:
{avg_rating:.2f}


TOP REPRESENTATIVE

Representative:
{top_rep}

Calls:
{top_rep_calls}

Revenue:
{top_rep_revenue:.2f}

Revenue Contribution:
{rep_revenue_percentage:.2f}%

Call Contribution:
{rep_call_percentage:.2f}%

Average Purchase:
{top_rep_avg_purchase:.2f}

Average Rating:
{top_rep_avg_rating:.2f}


TOP CITY

City:
{top_city}

Calls:
{top_city_calls}

Revenue:
{top_city_revenue:.2f}

Revenue Contribution:
{city_revenue_percentage:.2f}%

Call Contribution:
{city_call_percentage:.2f}%

Average Purchase:
{top_city_avg_purchase:.2f}

Average Rating:
{top_city_avg_rating:.2f}


TOP REPRESENTATIVES

{representative_analysis.head(5).round(2).to_string()}


TOP CITIES

{city_analysis.head(5).round(2).to_string()}


MONTHLY PERFORMANCE

{monthly_analysis.round(2).to_string()}


RATING DISTRIBUTION

{rating_distribution.to_string()}


TASK:

Generate exactly FIVE unique and meaningful business insights
for management.


STRICT RULES:

1. Use ONLY the verified data provided above.

2. Do not invent numbers, facts, trends, causes,
   relationships, or business conditions.

3. Do not claim causation when the data only shows
   a measurement.

4. Do not introduce unavailable metrics such as profit,
   conversion rate, retention, customer lifetime value,
   market share, staffing capacity, marketing spend,
   pricing, product performance, or growth.

5. Each insight must focus on a DIFFERENT business topic.

6. Do not repeat the same metric or calculation
   in multiple insights.

7. Do not create multiple insights from the same
   underlying calculation.

8. Every recommendation must logically follow
   from its corresponding finding.

9. Do not treat an average value as a target,
   threshold, or benchmark unless the data explicitly
   supports that interpretation.

10. Do not make recommendations that require
    unavailable information.

11. If the available data is insufficient to explain
    WHY something happened, clearly state that
    further analysis is required.

12. Verify every number and percentage before
    presenting it.

13. Keep the language concise, professional,
    and suitable for management.

14. Create a meaningful business title using
    2–5 words.

15. Do not use unsupported phrases such as:
    market leader, market share, customer loyalty,
    retention, high conversion, guaranteed growth,
    or business growth.


OUTPUT FORMAT:

1. [Business Title]

Finding:
[Concise data-supported finding.]

Recommendation:
[Professional recommendation directly related
to the finding.]


2. [Business Title]

Finding:
[Concise data-supported finding.]

Recommendation:
[Professional recommendation directly related
to the finding.]


3. [Business Title]

Finding:
[Concise data-supported finding.]

Recommendation:
[Professional recommendation directly related
to the finding.]


4. [Business Title]

Finding:
[Concise data-supported finding.]

Recommendation:
[Professional recommendation directly related
to the finding.]


5. [Business Title]

Finding:
[Concise data-supported finding.]

Recommendation:
[Professional recommendation directly related
to the finding.]


FINAL QUALITY CHECK:

Before returning the answer:

- Verify every number.
- Verify every percentage.
- Ensure all five insights are genuinely different.
- Remove duplicate calculations.
- Remove unsupported assumptions.
- Remove unsupported causal statements.
- Ensure every recommendation directly follows
  from its corresponding finding.
"""

    insights = generate_ai_response(
        prompt
    )

    st.write(insights)


# ============================================================
# RECOMMENDATION SYSTEM
# ============================================================

if st.button(
    "Generate Recommendations",
    key="generate_recommendations"
):

    recommendation_prompt = f"""
You are a Senior Data Analyst.

Prepare exactly FIVE practical and professional
business recommendations using ONLY the verified
Call Center metrics below.

VERIFIED DATA:

Total Calls:
{total_calls}

Total Revenue:
{total_revenue:.2f}

Average Purchase:
{avg_purchase:.2f}

Average Customer Rating:
{avg_rating:.2f}

Top Representative:
{top_rep}

Top Representative Revenue:
{top_rep_revenue:.2f}

Top Representative Call Contribution:
{rep_call_percentage:.2f}%

Top City:
{top_city}

Top City Revenue:
{top_city_revenue:.2f}

Top City Revenue Contribution:
{city_revenue_percentage:.2f}%

Top City Call Contribution:
{city_call_percentage:.2f}%


RULES:

1. Use only the verified data.

2. Do not invent numbers or business facts.

3. Do not assume causes.

4. Do not promise revenue growth.

5. Do not recommend staffing, marketing,
   pricing, investment, or product changes
   unless supported by the available data.

6. Each recommendation must address
   a different business area.

7. Do not repeat recommendations.

8. Every recommendation must have a
   clear data-based rationale.

9. If additional analysis is required,
   clearly state what should be analyzed.

10. Keep the language professional and concise.


OUTPUT FORMAT:

1. [Recommendation Title]

Recommendation:
[Actionable recommendation.]

Data Rationale:
[Metric or data point supporting the recommendation.]


2. [Recommendation Title]

Recommendation:
[Actionable recommendation.]

Data Rationale:
[Metric or data point supporting the recommendation.]


3. [Recommendation Title]

Recommendation:
[Actionable recommendation.]

Data Rationale:
[Metric or data point supporting the recommendation.]


4. [Recommendation Title]

Recommendation:
[Actionable recommendation.]

Data Rationale:
[Metric or data point supporting the recommendation.]


5. [Recommendation Title]

Recommendation:
[Actionable recommendation.]

Data Rationale:
[Metric or data point supporting the recommendation.]
"""

    recommendations = generate_ai_response(
        recommendation_prompt
    )

    st.write(recommendations)


# ============================================================
# ASK YOUR DATA
# ============================================================

question = st.text_input(
    "Ask a business question"
)


if st.button(
    "Ask AI",
    key="ask_ai"
):

    question_prompt = f"""
You are a professional Data Analyst.

Answer the user's business question using ONLY
the actual Call Center dataset.

DATASET INFORMATION:

Rows:
{len(filtered_df)}

Columns:
{list(filtered_df.columns)}

Question:
{question}


RULES:

1. Use only the available dataset information.

2. Perform calculations when the required
   columns are available.

3. Never invent values.

4. Never assume unavailable information.

5. If the question cannot be answered accurately
   from the dataset, clearly explain what additional
   analysis or data is required.

6. Keep the answer concise and professional.

7. If you calculate a number, briefly explain
   the calculation used.
"""

    answer = generate_ai_response(
        question_prompt
    )

    st.write(answer)