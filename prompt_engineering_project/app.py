import streamlit as st
import cohere
import json
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# Load roles from roles.json
with open("roles.json", "r") as f:
    roles = json.load(f)

# Streamlit UI
st.set_page_config(page_title="Prompt Engineering Chatbot", page_icon="🤖")
st.title("🤖 Prompt Engineering Chatbot (Cohere API)")
st.markdown("Powered by free Cohere API | Created by **Rajan Kumar Gupta**")

# Role selection
role_names = list(roles.keys())
selected_role = st.selectbox("Choose a Chatbot Role:", role_names)

# Get role details
role = roles[selected_role]
description = role["description"]
examples = role["examples"]

# Chat input
user_input = st.text_input("🗣️ Your Message:")

# Generate and display response
if user_input:
    # Build few-shot prompt
    prompt = f"{description}\n\n"
    for example in examples:
        prompt += f"User: {example['user']}\nBot: {example['bot']}\n"
    prompt += f"User: {user_input}\nBot:"

    response = co.generate(model="command-r-plus", prompt=prompt, max_tokens=150)
    st.markdown(f"**🤖 Bot Response:**\n\n{response.generations[0].text.strip()}")
