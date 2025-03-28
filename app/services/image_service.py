from g4f.client import Client
from g4f.cookies import set_cookies
from g4f.Provider import BingCreateImages

from app.config.settings import APIConfig

class ImageService:
    @staticmethod
    def set_bing_cookies():
        set_cookies(".bing.com", {"_U": APIConfig.BING_COOKIE})

    @staticmethod
    def generate_image(prompt):
        ImageService.set_bing_cookies()

        response = Client(image_provider=BingCreateImages).images.generate(
            model="dall-e-3",
            prompt=prompt
        )

        return response.data[0].url
