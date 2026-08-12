import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils import generate_ai_response

st.set_page_config(page_title="Call Center Analytics")

st.title("📞 Call Center Analytics Dashboard")

df = pd.read_csv(r"src\Cleaned_Data.csv")
total_calls = len(df)

revenue = df["Purchase Amount"].sum()

avg_purchase = df["Purchase Amount"].mean()

avg_satisfaction = df["Satisfaction Rating"].mean()

c1,c2,c3,c4 = st.columns(4)

c1.metric("Total Calls",total_calls)

c2.metric("Revenue",f"₹{revenue:,.0f}")

c3.metric("Avg Purchase",round(avg_purchase,2))

c4.metric("Avg Satisfaction",round(avg_satisfaction,2))
months = ["All"] + sorted(df["Month"].unique().tolist())

selected_month = st.sidebar.selectbox(
   "Select Month",
   months
)

if selected_month != "All":
   filtered_df = df[df["Month"]==selected_month]
else:
   filtered_df = df
rep = filtered_df.groupby("Representative")["Call Number"].count()

fig,ax = plt.subplots()

rep.plot(kind="bar",ax=ax)

ax.set_title("Calls Handled by Representative")

st.pyplot(fig)
st.header(" AI Business Analyst")
if st.button("Generate Executive Summary"):

   prompt = f"""
You are a Senior Business Analyst.

Dataset Summary

Total Calls : {total_calls}

Revenue : {revenue}

Average Purchase : {avg_purchase:.2f}

Average Satisfaction : {avg_satisfaction:.2f}

Write an executive summary suitable for senior management.
"""

   summary = generate_ai_response(prompt)

   st.write(summary)
if st.button("Generate Business Insights"):

   top_rep = filtered_df.groupby(
       "Representative"
   )["Purchase Amount"].sum().idxmax()

   top_city = filtered_df.groupby(
       "City"
   )["Purchase Amount"].sum().idxmax()

   prompt = f"""
Generate

Five Business Insights

using

Top Representative : {top_rep}

Top City : {top_city}

Average Satisfaction : {avg_satisfaction}

Revenue : {revenue}

Write professionally.
"""

   insights = generate_ai_response(prompt)

   st.write(insights)
if st.button("Generate Business Insights"):

   top_rep = filtered_df.groupby(
       "Representative"
   )["Purchase Amount"].sum().idxmax()

   top_city = filtered_df.groupby(
       "City"
   )["Purchase Amount"].sum().idxmax()

   prompt = f"""
Generate

Five Business Insights

using

Top Representative : {top_rep}

Top City : {top_city}

Average Satisfaction : {avg_satisfaction}

Revenue : {revenue}

Write professionally.
"""

   insights = generate_ai_response(prompt)

   st.write(insights)

#Recommendations
if st.button("Generate Recommendations"):

   prompt = f"""
Average Satisfaction : {avg_satisfaction}

Revenue : {revenue}

Provide

Five recommendations

to improve the business.
"""

   recommendations = generate_ai_response(prompt)

   st.write(recommendations)

#Ask Your Data
question = st.text_input(
   "Ask a business question"
)

if st.button("Ask AI"):

   prompt = f"""
Dataset Information

Rows : {len(filtered_df)}

Columns

{list(filtered_df.columns)}

Question

{question}

Answer as a Business Analyst.

If the answer requires exact calculations that are not provided, clearly state that additional analysis is needed rather than making up values.
"""

   answer = generate_ai_response(prompt)

   st.write(answer)

