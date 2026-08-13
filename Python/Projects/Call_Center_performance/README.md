# 📞 Call Center Performance Analytics & AI Business Analyst

An interactive **Call Center Analytics Dashboard** built with Python, Pandas, Streamlit, Matplotlib, and Google Gemini AI to analyze operational performance and convert verified data into business-ready insights.

## 🎯 Project Objective

To analyze call-center performance across **call volume, purchase revenue, customer ratings, representatives, cities, and monthly performance**, while using Generative AI to simplify business interpretation.

## 📊 Key Analysis

- Total Calls & Revenue
- Average Purchase Value
- Average Customer Rating
- Representative Performance
- City-wise Revenue & Call Volume
- Monthly Performance
- Customer Rating Distribution
- Data-driven Business Insights

## 🤖 AI Business Analyst

The project integrates **Google Gemini AI** as an analytical interpretation layer.

**Workflow:**

`Dataset → Pandas Analysis → Verified Metrics → Gemini AI → Business Insights`

The AI generates:

- **5 unique business insights**
- Data-supported findings
- Evidence-based recommendations
- Natural-language business analysis

The AI is instructed to avoid **duplicate insights, invented numbers, unsupported assumptions, and conclusions not supported by the dataset.**

## 💬 Ask Your Data

Users can ask business questions in natural language and receive answers based on the available dataset.

Example:

> Which representative generated the highest revenue?

> Which city contributed the highest revenue?

## 🛠️ Tech Stack

- **Python** – Application & analysis
- **Pandas** – Data processing & aggregation
- **Matplotlib** – Data visualization
- **Streamlit** – Interactive dashboard
- **Google Gemini AI** – AI-powered business analysis
- **python-dotenv** – API key management
- **Git & GitHub** – Version control

## 📂 Project Structure

```text
Call_Center_performance/
│
├── src/
│   ├── app_ai.py
│   ├── utils.py
│   └── Cleaned_Data.csv
│
├── requirements.txt
└── README.md

Key Skills Demonstrated

Data Analytics:
Python, Pandas, Data Cleaning, GroupBy, KPI Analysis, Business Analysis

Visualization:
Matplotlib, Streamlit

Generative AI:
Gemini API, Prompt Engineering, AI-assisted Business Insights

Development:
Python Application Development, Environment Variables, Git, GitHub

💡 Business Value

This project demonstrates how traditional data analysis and Generative AI can work together:

Reliable Calculations → Clear Visuals → AI-assisted Interpretation → Business Insights

A key design principle of the project is:

Python calculates. AI interprets.

This keeps numerical analysis data-driven while using AI to communicate findings in a business-friendly way.

🚀 Run Locally
pip install -r requirements.txt
streamlit run src/app_ai.py

Configure the Gemini API key through a local .env file before running the application.

📌 Project Outcome

This project demonstrates practical experience in building an end-to-end Data Analytics + Generative AI application, from data processing and KPI development to interactive visualization and AI-assisted business analysis.


