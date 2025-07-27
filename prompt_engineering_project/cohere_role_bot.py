import os
import cohere
import json
from dotenv import load_dotenv

# Load API Key
load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# Load roles from JSON
with open("roles.json", "r") as f:
    roles = json.load(f)

# Let user select a role
print("🔁 Choose a chatbot role:")
for i, role in enumerate(roles.keys(), 1):
    print(f"{i}. {role.replace('_', ' ').title()}")

choice = int(input("Enter your choice (1/2/3...): "))
role_key = list(roles.keys())[choice - 1]
selected = roles[role_key]

# Build base prompt with examples
base_prompt = f"{selected['description']}\n\n"
for ex in selected["examples"]:
    base_prompt += f"User: {ex['user']}\nBot: {ex['bot']}\n"
base_prompt += "\nUser: {}\nBot:"

# Start Chat
print(f"\n🤖 {role_key.replace('_', ' ').title()} Bot is ready — type 'exit' to quit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Bot: Goodbye!")
        break

    prompt = base_prompt.format(user_input)
    response = co.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=150
    )
    print("Bot:", response.generations[0].text.strip())
