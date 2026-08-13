# 📞 Call Center Performance Analytics & AI Business Analyst

An interactive **Call Center Performance Analytics** application built using **Python, Pandas, Streamlit, Matplotlib, and Google Gemini AI**.

This project analyzes call-center operational data and converts it into meaningful business metrics, visual insights, evidence-based recommendations, and natural-language business analysis.

The project follows a simple principle:

> **Python calculates the metrics. AI interprets the verified data.**

---

## 📌 Project Overview

Call-center data contains valuable information about customer interactions, representatives, purchases, ratings, locations, and call activity.

However, raw data alone does not provide an immediate business view.

This project transforms the available operational data into:

- Key Performance Indicators (KPIs)
- Representative performance analysis
- City-level performance analysis
- Monthly performance analysis
- Customer rating analysis
- Interactive visualizations
- AI-generated business insights
- Evidence-based recommendations
- Natural-language business questions

The goal is to demonstrate a practical **Data Analytics + Generative AI** workflow using a real-world business scenario.

---

## 🎯 Business Objective

The main objective of this project is to analyze call-center performance and provide a simple analytical interface for understanding:

- Call volume
- Purchase revenue
- Average purchase value
- Customer satisfaction
- Representative performance
- City-level performance
- Monthly performance variation

The project also demonstrates how Generative AI can be integrated into a data analytics workflow to help translate verified analytical results into business-friendly insights.

---

## ❓ Business Questions

The application is designed to help answer questions such as:

1. How many calls were handled during the selected period?
2. What is the total purchase revenue?
3. What is the average purchase value?
4. What is the average customer rating?
5. Which representatives handled the highest number of calls?
6. Which representative generated the highest purchase revenue?
7. Which cities contributed the highest revenue?
8. How does call volume vary across cities?
9. How does revenue vary across months?
10. What measurable performance patterns require further analysis?

---

## 📊 Dataset

The project uses a cleaned call-center dataset containing operational and customer-related information.

### Main Dataset Columns

| Column | Description |
|---|---|
| `Call number` | Call reference number |
| `Customer ID` | Customer identifier |
| `Duration` | Call duration |
| `Representative` | Representative handling the call |
| `Date of Call` | Date of customer interaction |
| `Purchase` | Purchase amount associated with the call |
| `Rating` | Customer rating |
| `Month` | Month of the call |
| `Customer ID.1` | Additional customer identifier |
| `Gender` | Customer gender |
| `Age` | Customer age |
| `City` | Customer city |

Dataset file:

```text
src/Cleaned_Data.csv

##Technology Stack
Programming & Data Analysis
Python
Pandas
NumPy
Visualization
Matplotlib
Application
Streamlit
Generative AI
Google Gemini API
google-genai
Environment Management
python-dotenv
Version Control
Git
GitHub

##AI Business Analyst

One of the main features of the project is the AI Business Analyst.

The purpose is not to allow AI to freely generate business claims.

Instead, Python first calculates verified metrics from the dataset.

These verified metrics are then provided to Gemini for business interpretation.

##Workflow
Raw Data
   ↓
Python / Pandas
   ↓
Verified Calculations
   ↓
Structured Prompt
   ↓
Gemini AI
   ↓
Business Interpretation

This approach helps reduce:

Unsupported assumptions
Invented numbers
Duplicate insights
Unverified business conclusions
💡 Business Insights

The Generate Business Insights feature produces five structured insights.

Each insight contains:

Business Title

Finding:
Data-supported observation.

Recommendation:
A practical recommendation logically connected
to the finding.
Example
[Revenue Concentration]

Finding:
Cleveland generated 37,692.02, representing 39.06%
of total revenue.

Recommendation:
Compare Cleveland's call volume, average purchase,
and rating with other cities to identify measurable
differences in regional performance.

The AI is instructed to:

Use only verified metrics
Avoid invented numbers
Avoid unsupported assumptions
Avoid causal claims
Avoid duplicate calculations
Keep insights unique
Provide recommendations connected to the finding

#Recommendation System

The project separates Business Insights from Recommendations.

Business Insights answer:

What does the data show?

Recommendations answer:

What action should be considered based on the available evidence?

Recommendations are generated using the verified analytical metrics.

The system avoids recommendations involving unavailable information such as:

Staffing capacity
Marketing budgets
Profit margins
Customer retention
Market share
Pricing strategy

unless those metrics are actually available in the dataset
