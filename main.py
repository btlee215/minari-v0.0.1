import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer

def main():
    st.title("Patient Email Assistant")
    st.subheader("Input Email")

    # Load the T5 model and tokenizer
    model_name = "google/flan-t5-xxl"
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = T5Tokenizer.from_pretrained(model_name)

    # Input text area
    email_text = st.text_area("Enter the email", height=200)

    # Generate button
    if st.button("Generate Response"):
        response = generate_response(email_text, model, tokenizer)
        st.subheader("Generated Response")
        st.write(response)

def generate_response(email_text, model, tokenizer):
    # Tokenize the input text
    input_ids = tokenizer.encode(email_text, return_tensors="pt")

    # Generate the response
    output = model.generate(input_ids)

    # Decode the generated output
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

if __name__ == "__main__":
    main()
