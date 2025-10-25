import streamlit as st
import requests

# --- PAGE CONFIG ---
st.set_page_config(page_title="💰 AI Financial Chatbot", page_icon="💬", layout="wide")

# --- BACKGROUND GRADIENT ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #c3ecf2, #f7c6ff, #b5e8a8);
    background-size: 400% 400%;
    animation: gradient 10s ease infinite;
}
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

h1, h2, h3 {
    text-align: center;
    color: #333333;
    font-family: 'Trebuchet MS', sans-serif;
}

.chatbox {
    background-color: white;
    border-radius: 15px;
    padding: 20px;
    margin-top: 30px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}

button[kind="primary"] {
    background-color: #ff69b4;
    color: white;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    font-weight: bold;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>💬 AI-Powered Financial Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<h3>Analyze your business finances with style 💸✨</h3>", unsafe_allow_html=True)

# --- CHAT INPUT AREA ---
query = st.text_input("💭 Type your financial question below:")

if st.button("✨ Ask the Chatbot"):
    if query.strip() == "":
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Thinking... 💭"):
            response = requests.get("http://127.0.0.1:8000/ask/", params={"query": query})
            result = response.json().get("response", "No response received.")
        
        st.markdown(f"""
        <div class="chatbox">
            <p><b>🧑‍💼 You:</b> {query}</p>
            <p><b>🤖 Chatbot:</b> {result}</p>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><center><b>Developed with ❤️ by Sanjana Malik</b></center>", unsafe_allow_html=True)
