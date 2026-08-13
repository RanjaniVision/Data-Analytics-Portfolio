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
