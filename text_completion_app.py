# Capstone Project: AI-Powered Text Completion

from openai import OpenAI
import os

# Safely load OpenAI API key
api_key = os.getenv("OPEN_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=api_key)

def main():
    print("Welcome to your OpenAI chatbot!")
    print("Type 'exit' or 'quit' to stop.")

    while True:
        # Gets user input
        user_input = input("\nYou: ").strip()
        
        # Doesn't accept blank input
        if not user_input:
            print("Please enter something.")
            continue
        
        # Quits if user types 'exit' or 'quit'
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            
            reply = response.choices[0].message.content.strip()
            print("\nAssistant:", reply)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()