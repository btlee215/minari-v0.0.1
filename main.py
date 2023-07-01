pip install -r requirements.txt

import streamlit as st
from transformers import pipeline

# Load the language model
model = pipeline("text-generation", model="gpt2")

def generate_response(email_text):
    # Process the email text using the language model
    generated_text = model(email_text, max_length=100)[0]['generated_text']
    
    # Return the generated response
    return generated_text

def main():
    # Set the title and description of the app
    st.title("Email Response Generator")
    st.markdown("Enter an email and generate a response using the language model.")

    # Input email text
    email_text = st.text_area("Enter the email text", height=200)

    # Generate response button
    if st.button("Generate Response"):
        if email_text:
            # Generate the response
            response = generate_response(email_text)
            
            # Display the generated response
            st.markdown("## Generated Response")
            st.write(response)
        else:
            st.warning("Please enter an email text.")

if __name__ == "__main__":
    main()
