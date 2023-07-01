import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"
headers = {"Authorization": "Bearer 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"}

def main():
    st.title("Patient Email Assistant")
    st.subheader("Input Email")

    # Input text area
    email_text = st.text_area("Enter the email", height=200)

    # Generate button
    if st.button("Generate Response"):
        response = generate_response(email_text)
        st.subheader("Generated Response")
        generated_text = trim_response(response[0]['generated_text'], 1000)  # Trim to desired length
        edited_response = st.text_area("Edit the response", value=generated_text, height=200)
        st.write("Modified Response:")
        st.write(edited_response)

def generate_response(email_text):
    input_text = "Patient Email: {}\n\nClinician Response:".format(email_text)
    payload = {
        "inputs": input_text,
        "options": {
            "generate_explanations": True,
            "num_beams": 10,
            "max_length": 3000,  # Set a larger value for max_length
            "early_stopping": True
        }
    }
    response = query(payload)
    return response

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def trim_response(text, desired_length):
    # Trim the text while preserving context and structure
    words = text.split()
    trimmed_words = words[:desired_length]
    trimmed_text = " ".join(trimmed_words)
    return trimmed_text

if __name__ == "__main__":
    main()
