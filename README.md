 # 🥗 Multimodal Nutrition Assistant

A production-ready web application that analyzes meal imagery, estimates nutritional volume, and structures personalized macro breakdowns using multimodal AI.

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.31.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 🎯 Overview
* **Core Purpose:** Bridges computer vision and personalized dietary tracking into an automated, interactive web application.
* **System Design:** Integrates Google's multimodal intelligence with a reactive Python frontend for instant meal analysis.
* **Functional Scope:** Automatically identifies food components, estimates nutritional volume, and structures macro breakdowns.

---

## ✨ Features & Core Analysis
* **Multimodal Image Analysis:** Upload any meal photograph (`.jpg`, `.jpeg`, `.png`) for immediate automated ingredient detection.
* **Fitness-Goal Customization:** Muscle Building (high-protein focus), Weight Gain (calorie-dense strategies), Fat Loss (deficit tracking), and Maintenance (balanced ratios).
* **Comprehensive Macro Breakdowns:** Real-time estimations for Calories, Proteins, Carbohydrates, and Fats.
* **Security Compliance:** Secure environment variable isolation protecting secret API keys from public exposure.

---

## 🎨 User Experience
* **Interface Design:** Clean, responsive web layout optimized for desktop and mobile web browsers.
* **File Handling:** Intuitive file uploader component with instant visual feedback and image preview.
* **Goal Selection:** Interactive dropdown selectors for custom fitness targets and goals.
* **Feedback State:** Real-time spinner loading states during AI inference to maintain high responsiveness.

---

## 🛠️ Tech Stack Details
* **Frontend & UI:** `app.py` handles reactive UI rendering, widget state management, and user interaction routing.
* **Backend Logic:** `AI_model.py` encapsulates direct SDK communication, prompt formulation, and payload delivery.
* **AI Processing:** Google Gemini Multimodal API executes high-speed visual reasoning and dietary parsing.

---

## 📂 Project Structure
```text
food_analyzer_app/
│
├── .env                 # Root configuration file storing secret keys safely (Git-ignored)
├── .gitignore           # Exclusion rules preventing sensitive files & caches from tracking
├── requirements.txt     # Explicit package version thresholds and dependencies
├── app.py               # Primary Streamlit web application interface and routing
└── AI_model.py          # Core Gemini multimodal processing logic and API client

---

## 🚀 Quick Start & Installation
*Workspace Setup: Clone repository or open your working project directory in VS Code.

*Dependencies Installation: Open terminal and run:
```bash
 pip install -r requirements.txt
 ```

*Environment Configuration: 
```bash
Create a .env file in the root directory and add your API key:
```

```bash
GEMINI_API_KEY=your_actual_api_key_here
```

---

## 🏃‍♂️ Running the Application
*Execution Command: Execute the following command in your terminal:
```bash
streamlit run app.py
```

---

## 💡 Usage Guide

*Goal Selection: Select your target fitness goal from the interactive dropdown menu.

*Execution: Upload your meal photograph and click Analyze Nutrition.

---

## 📊 Understanding the Result

*Food Identification: Identifies discrete food items present in the uploaded image.

*Caloric Estimation: Computes approximate caloric volume per serving.

*Macro Breakdown: Provides exact grams of protein, carbohydrates, and fats.

---

## 📈 Exploiting Results

*Application: Use structured AI recommendations to adjust daily meal planning and fitness target alignment.

---

## ⚙️ Configuration, Model Selection & Performance Tuning

*API Setup: Set GEMINI_API_KEY securely in environment variables.

*Primary Vision Model: Uses gemini-2.0-flash for rapid multimodal inference and low-latency image processing.

*Performance Tuning: Optimize image resolution prior to upload to minimize payload latency and enhance response speed.

---

## 💻 Development & Adding New Features

*State Management: Use st.session_state in app.py to persist user history across interactions.

*Prompt Engineering: Modify prompt strings in AI_model.py to extract customized dietary parameters.

*Feature Expansion: Extend backend parsing to return structured JSON dictionaries for analytics dashboards.

---

## 🔍 Troubleshooting & Debug Mode

*Missing API Key Error
   Verify that your `.env` file exists in the root directory and contains a valid, active API key.
   ```bash
   GEMINI_API_KEY=your_actual_api_key_here
   ```

*Accidentally Committed Secret Files
If you accidentally tracked your .env file in Git, run the following command in your terminal to remove it from tracking without deleting it locally:
```bash
git rm --cached .env
```

*Port Conflicts (Address already in use)
If port 8501 is already occupied by another process, run Streamlit on an alternative port:
```bash
streamlit run app.py --server.port 8502
```

*Package Version Mismatches
If you encounter dependency conflicts or import errors, upgrade your pip installer and reinstall clean packages:
```bash
pip install --upgrade pip
pip install --force-reinstall -r requirements.txt
```

*Verbose Debug Logging
Enable verbose logging in your terminal to inspect raw payload exceptions and real-time backend traces during execution:
```bash
streamlit run app.py --logger.level=debug
```

---

## 🧠 Model Information & Embedding Models

*Generative Models: gemini-2.0-flash (primary multimodal engine for vision and text generation).

*Embedding Models: text-embedding-004 can be integrated for vector search and semantic dietary knowledge retrieval.

---

## 🎓 Educational Use & Perfect For

*Academic Value: Ideal for students studying computer vision, API integrations, and generative AI pipelines.

*Target Suitability: Perfect for fitness tracking, developer portfolio showcases, and hackathon prototypes.

---

## 🔮 Future Enhancements

*Database* Persistence: SQLite / PostgreSQL integration for long-term meal history logging.

*Visual Analytics: Plotly-based interactive charts for weekly macro aggregate tracking.

*Localization: Multi-language localization for global dietary descriptions.

---

## 📜 License, Contributing, Contact & Acknowledgements

*License: Distributed under the MIT License.

*Contributing: Pull requests and feature branches are welcome via GitHub.

*Contact: Reach out via GitHub repository discussions or issue boards.

---


