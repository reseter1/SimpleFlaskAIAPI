from functools import wraps
from flask import jsonify

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return wrapper

def format_response(response_text, model="FXT"):

    return {
        'text': f"(Powered by Python AI Reseter API): {response_text}\n[Current model: {model}]"
    }

def validate_message(data):
    if not data or 'message' not in data:
        raise ValueError('No messages provided')
    return data.get('message', '')
