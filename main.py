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
        if response:
            if isinstance(response, list) and len(response) > 0:
                generated_text = response[0].get("generated_text", "")
            elif isinstance(response, dict):
                generated_text = response.get("generated_text", "")
            else:
                generated_text = ""
                
            edited_response = st.text_area("Edit the response", value=generated_text, height=200)
            st.write("Modified Response:")
            st.write(edited_response)

def generate_response(email_text):
    payload = {
        "inputs": email_text,
        "options": {
            "generate_explanations": True,
            "num_beams": 5,
            "max_length": 500,
            "early_stopping": True,
            "no_repeat_ngram_size": 3,
            "length_penalty": 1.5
        }
    }
    response = query(payload)
    return response

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    main()
