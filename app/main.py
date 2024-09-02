from dotenv import load_dotenv
import os
import openai
from flask import Blueprint, request, jsonify, send_file
from app.youtube_processor import download_and_transcribe_video
from app.chatbot_handler import ask_question_to_chatbot

# Cargar las variables de entorno desde el archivo .env
load_dotenv('app/.env')

# Obtener la clave API de OpenAI desde la variable de entorno
openai.api_key = os.getenv('OPENAI_API_KEY')

# Verificar que la clave API se haya cargado correctamente
if not openai.api_key:
    raise ValueError("La clave API de OpenAI no está configurada. Asegúrate de que el archivo .env contenga OPENAI_API_KEY.")

# Definición del Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return send_file('templates/index.html')

@main.route('/process_video', methods=['POST'])
def process_video():
    data = request.get_json()
    youtube_url = data['url']
    
    # Descargar y transcribir el video
    transcript, audio_file_path = download_and_transcribe_video(youtube_url)
    
    if audio_file_path:
        audio_filename = os.path.basename(audio_file_path)
        # Crear el nombre del archivo de transcripción basado en el nombre del audio
        transcript_filename = os.path.basename(audio_file_path).replace('.mp3', '.txt')
        return jsonify({
            'transcript': transcript,
            'transcript_filename': transcript_filename,
            'audio_filename': audio_filename
        })
    else:
        return jsonify({'transcript': transcript, 'transcript_filename': None, 'audio_filename': None})

@main.route('/ask_question', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data['question']
    transcript_filename = data.get('transcript_filename')

    # Obtener la ruta completa del archivo de transcripción
    if transcript_filename:
        transcript_file_path = os.path.join('app/static/audio/', transcript_filename)
    else:
        return jsonify({'error': 'No se proporcionó el archivo de transcripción'}), 400

    # Leer la transcripción del archivo
    try:
        with open(transcript_file_path, 'r') as file:
            transcript = file.read()
    except FileNotFoundError:
        return jsonify({'error': 'Archivo de transcripción no encontrado'}), 404

    # Obtener la respuesta del chatbot basada en la transcripción
    answer = ask_question_to_chatbot(question, transcript)
    return jsonify({'answer': answer})
