import os
import cohere
from dotenv import load_dotenv

# Load API key
load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# Base prompt with few-shot examples
base_prompt = """
You are a helpful career advisor bot.

User: Can you review my resume for improvement?
Bot: Sure! Please paste your resume and I’ll give you tips on structure, keywords, and achievements.

User: How do I answer 'Tell me about yourself'?
Bot: Use the Present-Past-Future format. Start with what you do now, share past highlights, and explain your goal for the role.

User: {}
Bot:
"""

print("🤖 Career Advisor Bot (powered by Cohere) — type 'exit' to quit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Bot: Goodbye! Best of luck in your career.")
        break

    prompt = base_prompt.format(user_input)
    response = co.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=150
    )
    print("Bot:", response.generations[0].text.strip())
