import streamlit as st
import openai

# Function to retrieve the OpenAI API key from the user
def get_openai_api_key():
    openai_api_key = st.sidebar.text_input("OpenAI API Key", key="openai_api_key", type="password")
    return openai_api_key

# Function to generate the response using the OpenAI API
def generate_response(email_text, api_key):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=email_text,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].text.strip()

def main():
    # Retrieve the OpenAI API key from the user
    api_key = get_openai_api_key()

    # Get the user's email input
    email_text = st.text_area("Enter your email text", height=200)

    # Generate the response using the OpenAI API
    if st.button("Generate Response"):
        response = generate_response(email_text, api_key)
        st.markdown(f"**Response:**\n{response}")

if __name__ == "__main__":
    main()
