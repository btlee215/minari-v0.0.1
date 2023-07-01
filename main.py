import streamlit as st
import openai

def generate_response(email_text):
    openai.api_key = "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"

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
    # Set page title
    st.set_page_config(page_title="Email Assistant")

    # Set up sidebar
    st.sidebar.title("Email Assistant")

    # Get user input
    email_text = st.text_area("Enter the email text")

    # Generate response
    if st.button("Generate Response"):
        if email_text:
            response = generate_response(email_text)
            st.success(response)
        else:
            st.warning("Please enter some email text.")

if __name__ == "__main__":
    main()
