import os
from g4f.client import Client
from g4f.cookies import set_cookies
from g4f.Provider import RetryProvider, Gemini, FreeGpt, Blackbox

from app.config.settings import APIConfig

class ChatService:
    @staticmethod
    def set_google_cookies():
        set_cookies(".google.com", {
            "__Secure-1PSID": APIConfig.SECURE_1PSID,
            "__Secure-1PSIDTS": APIConfig.SECURE_1PSIDTS
        })

    @staticmethod
    def get_response_gemini(message):
        ChatService.set_google_cookies()
        response = Client(provider=Gemini).chat.completions.create(
            model="gemini",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content, "Gemini Model"

    @staticmethod
    def get_response_fallback(message):
        response = Client(provider=RetryProvider([Blackbox, FreeGpt])).chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content, "GPT Model"

    @staticmethod
    def get_response(message):
        try:
            return ChatService.get_response_gemini(message)
        except Exception as e:
            print(f"An error occurred with Gemini: {e}")
            return ChatService.get_response_fallback(message)

    @staticmethod
    def format_simple_query(message):
        return ("Trả lời ngắn gọn, súc tích và thêm biểu tượng cảm xúc phù hợp để làm sinh động câu trả lời. "
                f"Luôn sử dụng tiếng `{APIConfig.LANG}` trong phản hồi. Nếu được hỏi về danh tính, hãy giới thiệu bạn là Python AI Reseter API, "
                "một dịch vụ API chatbot được phát triển và duy trì bởi Reseter. Hãy cung cấp thông tin chính xác, "
                "hữu ích và thân thiện với người dùng." + message)

    @staticmethod
    def format_detail_query(message):
        return (f"Trả lời chi tiết và đầy đủ. Luôn sử dụng tiếng `{APIConfig.LANG}` trong phản hồi. Nếu được hỏi về danh tính, hãy giới thiệu bạn là Python AI Reseter API, "
                "một dịch vụ API chatbot được phát triển và duy trì bởi Reseter. Hãy cung cấp thông tin chính xác, "
                "hữu ích và thân thiện với người dùng." + message)
