import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def main():
    st.title("Patient Email Assistant")
    st.subheader("Input Email")

    email_text = st.text_area("Enter the email", height=200)
    
    if st.button("Generate Response"):
        response = generate_response(email_text)
        st.subheader("Generated Response")
        st.write(response)

        
def generate_response(email_text):
    model_name = "google/flan-t5-xxl"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    inputs = tokenizer.encode(email_text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=1000)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response


if __name__ == "__main__":
    main()
