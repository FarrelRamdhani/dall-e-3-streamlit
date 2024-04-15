import os
import openai
from dotenv import load_dotenv

# load .env file
load_dotenv()

api = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_image(input_prompt: str, model_name: str, output_quality:str, image_size:str, image_style:str) -> str:
    """
    Generates an image using the DALL-E API.

    Args:
        input_prompt (str): The input prompt for generating the image.
        model_name (str): The name of the DALL-E model to use.
        quality (str): The quality of the generated image.
        size (str): The size of the generated image.
        style (str): The style of the generated image.

    Returns:
        str: The URL of the generated image.
    """
    response = api.images.generate(
        model=model_name,
        prompt=input_prompt,
        size=image_size,
        n=1,
        quality=output_quality,
        style=image_style
    )
    
    return response.data[0].url