import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

def generate_response(email_text):
    model_name = "google/flan-t5-xxl"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    prompt = f"Email: {email_text.strip()} \nResponse:"
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=200, num_beams=5, early_stopping=True)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def main():
    st.title("Patient Email Responder")

    email_text = st.text_area("Enter the email text:")
    if st.button("Generate Response"):
        response = generate_response(email_text)
        st.text("Generated Response:")
        st.text(response)

if __name__ == "__main__":
    main()
