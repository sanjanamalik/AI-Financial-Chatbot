import pandas as pd
import openai
import os
from dotenv import load_dotenv

# --- Load environment variables ---
# This allows the app to work both locally (.env) and on Render (Environment Variables)
load_dotenv()

# Get the OpenAI API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

# --- Load financial data ---
data = pd.read_csv("backend/finance_data.csv")


def get_financial_response(query):
    query = query.lower().strip()

    # --- Handle simple finance-related questions ---
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

    # --- Use OpenAI model for general financial queries ---
    else:
        prompt = (
            f"You are an AI financial assistant. Based on this data {data.to_dict()}, "
            f"answer the following user query in a helpful way:\n\n{query}"
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response["choices"][0]["message"]["content"]

        except Exception as e:
            return f"⚠️ Error fetching AI response: {str(e)}"
