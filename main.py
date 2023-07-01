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
        edited_response = st.text_area("Edit the response", value=response["generated_text"], height=200)
        st.write("Modified Response:")
        st.write(edited_response)

def generate_response(email_text):
    payload = {
        "inputs": email_text,
        "options": {
            "generate_explanations": True,
            "num_beams": 5,
            "max_length": 1000,
            "early_stopping": True
        }
    }
    response = query(payload)
    return response

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    main()
