import streamlit as st
import anthropic

st.title("📚 AI Study Planner")

subject = st.text_input("Enter your subject (e.g. Math, History)")
task = st.text_area("What is your study problem?")

if st.button("Generate Plan 🚀"):
    if subject and task:
        client = anthropic.Anthropic(api_key="SECRET123")  # ← put your key

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"You are an expert study coach. Create a personalized study plan for a student studying {subject} who has this problem: {task}. Give practical steps."
                }
            ]
        )

        st.write("### Result:")
        st.write(message.content[0].text)
    else:
        st.warning("Please enter subject and task")