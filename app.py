import streamlit as st
import requests

st.set_page_config(page_title="AI Food Vision Analyzer", page_icon="🥗", layout="centered")

st.title("🥗 AI Food Nutrition Analyzer")
st.subheader("Upload a photo of your meal to get instant macro facts!")

uploaded_file = st.file_uploader("Choose a food image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Your Uploaded Meal", use_container_width=True)
    
    if st.button("🔍 Analyze Nutrition"):
        with st.spinner("AI is scanning your food image..."):
            try:
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                response = requests.post("http://127.0.0.1:8000/analyze-image/", files=files)
                
                if response.status_code == 200:
                    result = response.json()
                    st.success("Analysis Complete!")
                    st.markdown("### 📊 Nutritional Breakdown")
                    st.markdown(result["analysis"])
                else:
                    st.error("Failed to analyze image. Please check backend server.")
            except Exception as e:
                st.error(f"Error connecting to backend: {e}")

            