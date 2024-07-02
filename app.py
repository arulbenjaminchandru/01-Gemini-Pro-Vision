import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")

# function for Gemini Pro Vision API call

def gemini_pro_vision_api(image, prompt):
    # Simulate a response from the API
    if prompt != "":
        response = model.generate_content([prompt,image])
    else:
        response = model.generate_content(image)
    return response.text

def main():
    st.title("Gemini Pro Vision Image Recognition")

    # File uploader for image upload
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    # Prompt text box
    prompt = st.text_input("Enter your prompt:", "Describe the image content")

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        
        # Call the Gemini Pro Vision API
        response = gemini_pro_vision_api(image, prompt)
        
        # Display the API response
        st.write("Generated information from Gemini", response)


if __name__ == "__main__":
    main()
