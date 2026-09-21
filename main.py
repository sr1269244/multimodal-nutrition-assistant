from fastapi import FastAPI, File, UploadFile
from AI_model import analyze_food_image

app = FastAPI(title="AI Image Food Analyzer API")

@app.get("/")
def home():
    return {"status": "AI Food Analyzer API is running!"}

@app.post("/analyze-image/")
async def analyze_image(file: UploadFile = File(...)):
    contents = await file.read()
    nutrition_info = analyze_food_image(contents)
    return {"filename": file.filename, "analysis": nutrition_info}
