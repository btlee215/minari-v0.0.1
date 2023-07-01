import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = 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

def generate_response(email_text):
    # Construct the prompt with a system message
    prompt = f"Prompt: You are a doctor with great bedside manner. You received an email from a patient:\n\n{email_text}\n\nResponse:"

    # Make a request to the OpenAI API for text generation
    response = openai.Completion.create(
        engine="davinci-codex",  # GPT-3.5 engine
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None
    )
    
    # Extract the generated response from the API response
    generated_text = response.choices[0].text.strip()
    
    # Return the generated response
    return generated_text

def main():
    # Set the title and description of the app
    st.title("Email Response Generator")
    st.markdown("Enter an email and generate a response with the voice of a clinician with great bedside manner.")

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
