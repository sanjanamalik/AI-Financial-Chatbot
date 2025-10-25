import pandas as pd
import openai

import streamlit as st
openai.api_key = st.secrets["OPENAI_API_KEY"]


# Load financial data
data = pd.read_csv("backend/finance_data.csv")

def get_financial_response(query):
    query = query.lower()

    # Handle simple finance-related questions
    if "profit" in query:
        total_profit = data["Profit"].sum()
        return f"💰 Total profit till date is ₹{total_profit}."

    elif "revenue" in query:
        total_revenue = data["Revenue"].sum()
        return f"📈 Total revenue till date is ₹{total_revenue}."

    elif "expense" in query:
        total_expense = data["Expense"].sum()
        return f"💸 Total expense till date is ₹{total_expense}."

    elif "highest" in query:
        row = data.loc[data["Profit"].idxmax()]
        return f"🏆 Highest profit was ₹{row['Profit']} in {row['Date']}."

    else:
        # Use AI model for general financial queries
        prompt = f"You are an AI financial assistant. Based on this data {data.to_dict()}, answer: {query}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
