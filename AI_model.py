from google import genai
from PIL import Image

# Initialize the Gemini client directly with your API key
client = genai.Client(api_key="your_api_key")

def analyze_food_image(image_path: str):
    img = Image.open(image_path)
    
    prompt = """
    Analyze this food image in detail.
    Provide a structured summary containing:
    1. Food Item Name
    2. Estimated Portion Size / Weight
    3. Nutritional Breakdown (Calories, Protein, Carbs, Fats)
    4. Health Score & Nutritional Advice
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[img, prompt]
    )
    
    return response.text
import io
import os
from PIL import Image
import google.generativeai as genai
import io
from PIL import Image
import google.generativeai as genai

import io
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_food_image(contents):
    img = Image.open(io.BytesIO(contents))
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([
        img,
        "Analyze this food image in detail. Provide a structured summary containing:\n1. Food Item Name\n2. Estimated Portion Size / Weight\n3. Nutritional Breakdown (Calories, Protein, Carbs, Fats)\n4. Health Score & Nutritional Advice"
    ])
    return response.text
