import streamlit as st
import openai

def generate_response(email_text):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=email_text,
            max_tokens=100,
            temperature=0.7,
            n=1,
            stop=None,
            top_p=None,
            frequency_penalty=None,
            presence_penalty=None,
            log_level=None
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("OpenAI API Error:", e)
        return None

def main():
    st.title("Email Response Generator")

    api_key = st.sidebar.text_input("OpenAI API Key", key="openai_api_key", type="password")
    openai.api_key = api_key

    # Input email text
    email_text = st.text_area("Enter the email text", height=200)

    # Generate response
    if st.button("Generate Response"):
        response = generate_response(email_text)
        if response:
            st.text_area("Generated Response", value=response, height=200)

if __name__ == "__main__":
    main()
