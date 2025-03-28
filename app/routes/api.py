from flask import Blueprint, request, jsonify, current_app

from app.services.chat_service import ChatService
from app.services.image_service import ImageService
from app.utils.helpers import handle_exceptions, format_response, validate_message

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

@api_bp.route('/simple_response', methods=['POST'])
@handle_exceptions
def process_messages_simple():
    data = request.json
    
    message = validate_message(data)
    
    formatted_message = ChatService.format_simple_query(message)
    
    response_text, model = ChatService.get_response(formatted_message)
    
    return jsonify(format_response(response_text, model)), 200

@api_bp.route('/detail_response', methods=['POST'])
@handle_exceptions
def process_messages_detail():
    data = request.json
    
    message = validate_message(data)
    
    formatted_message = ChatService.format_detail_query(message)
    
    response_text, model = ChatService.get_response(formatted_message)
    
    return jsonify(format_response(response_text, model)), 200

@api_bp.route('/image_response', methods=['POST'])
@handle_exceptions
def process_messages_image():
    data = request.json
    
    prompt = validate_message(data)
    
    image_url = ImageService.generate_image(prompt)
    
    return jsonify({'text': image_url}), 200
