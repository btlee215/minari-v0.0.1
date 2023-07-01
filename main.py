import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

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
    prompt = "As an experienced clinician, I understand your concerns. Based on your email, I would like to provide you with the following insights and possible next steps:"
    input_text = f"{prompt}\n{email_text}"

    payload = {
        "inputs": input_text,
    }
    response = query(payload)
    return response

if __name__ == "__main__":
    main()
