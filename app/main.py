# main.py
from flask import Blueprint, request, jsonify, send_file
from .youtube_processor import download_and_transcribe_video
from .chatbot_handler import ask_question_to_chatbot
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return send_file('templates/index.html')

@main.route('/process_video', methods=['POST'])
def process_video():
    data = request.get_json()
    youtube_url = data['url']
    transcript = download_and_transcribe_video(youtube_url)
    return jsonify({'transcript': transcript})

@main.route('/ask_question', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data['question']
    answer = ask_question_to_chatbot(question)
    return jsonify({'answer': answer})
