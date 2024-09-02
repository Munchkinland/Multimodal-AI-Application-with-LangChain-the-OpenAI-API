# chatbot_handler.py
import os
import openai

# Configuración del API Key de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_question_to_chatbot(question, transcript):
    try:
        # Combinar la transcripción con la pregunta
        prompt = f"Basado en la siguiente transcripción:\n\n{transcript}\n\nResponde la siguiente pregunta:\n{question}"
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        
        # Obtener la respuesta del chatbot
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        return f"Error: {str(e)}"
