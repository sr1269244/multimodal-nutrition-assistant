# ⚡ Multimodal Nutrition Assistant - Quick Reference Card

---

## ⏱️ 30-Second Start Guide

Clone & Open Directory
   ```bash
   cd food_analyzer_app

   Install Dependencies:
   ```bash
pip install -r requirements.txt

Configure Environment: 
Create a .env file and add your key:

```bash
GEMINI_API_KEY=your_actual_api_key_here

Launch Application:

```bash
streamlit run app.py


📊 Understanding Your Results

*Food Identification: Discovers and lists the individual food items detected in your uploaded meal photograph.

*Estimated Weight & Calories: Computes the approximate serving weight in grams and the total caloric volume.

*Macronutrient Breakdown: Provides the exact gram counts for proteins, carbohydrates, and fats.

*Vitamins & Minerals: Highlights essential micronutrients alongside their Daily Value percentages.

*Pros & Cons Analysis: Breaks down the nutritional benefits and potential drawbacks of the analyzed meal.

*Alternative Healthy Recipes: Recommends alternative culinary preparations that offer healthier nutritional profiles.


💻 Common Commands

Create Virtual Environment:
 ```bash
  python -m venv venv.

Activate Environment (Windows): 
```bash
 venv\Scripts\activate.

Activate Environment (Mac/Linux): 
```bash source venv/bin/activate.

Install Requirements:
 ```bash
  pip install -r requirements.txt.

Run App on Default Port:
 ``bash
  streamlit run app.py.

Run App on Custom Port: 
```bash
 streamlit run app.py --server.port 8502.


🔍 Troubleshooting Quick Fixes

*API Key Not Found Error: This happens when your .env file is missing or misnamed. Fix it by ensuring your .env file exists in the root directory with your correct key.

*Address Already in Use Error: This occurs when port 8501 is already occupied. Fix it by running the app on an alternative port using --server.port 8502.

*Git Tracking .env File: If you accidentally committed your secret key, untrack it safely by running
```bash
 git rm --cached .env.

*Module Import Errors: If dependencies fall out of sync, fix it by reinstalling clean packages using 
```bash
pip install --force-reinstall -r requirements.txt.