import os
import openai

# Configuración del API Key de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_question_to_chatbot(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question}
            ],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        return f"Error: {str(e)}"
