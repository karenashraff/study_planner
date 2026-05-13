import streamlit as st
import requests

st.title("📚 AI Study Planner")

subject = st.text_input("Enter your subject (e.g. Math, History)")
task = st.text_area("What is your study problem?")

if st.button("Generate Plan 🚀"):
    if subject and task:
        headers = {
            "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama3-8b-8192",
            "messages": [
                {
                    "role": "user",
                    "content": f"You are an expert study coach. Create a personalized study plan for a student studying {subject} who has this problem: {task}. Give practical steps."
                }
            ]
        }
        res = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )
        result = res.json()
        st.write("### Result:")
        st.write(result["choices"][0]["message"]["content"])
    else:
        st.warning("Please enter subject and task")
