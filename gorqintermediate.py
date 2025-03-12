import os
from groq import Groq

def ask_question(api_key, question):
    """Ask a question to the Groq API."""
    client = Groq(api_key=api_key)
    system_prompt = """Best Engineering Teacher in the world ."""
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        model="mixtral-8x7b-32768"
    )
    
    print("\nResponse:", response.choices[0].message.content)

def main():
    api_key = "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"
    question = input("Enter your question: ")
    ask_question(api_key, question)

if __name__ == "__main__":
    main()
