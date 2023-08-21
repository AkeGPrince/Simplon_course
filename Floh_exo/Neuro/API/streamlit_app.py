import streamlit as st
import requests

def main():
    # Set page title and description
    st.title("Text Generation with GPT-2")
    st.write("Enter a prompt and generate text using GPT-2 model.")

    # Prompt input
    prompt = st.text_input("Enter a prompt", "")

    if st.button("Generate Text"):
        if prompt:
            st.write("Generating, please wait...")

            # Send request to FastAPI service
            response = requests.post('http://localhost:8000', json={"prompt": prompt})

            if response.status_code == 200:
                output_text = response.json()['result']
                st.markdown("## Generated Text")
                st.write(output_text)
            else:
                st.error("An error occurred during text generation.")
        else:
            st.warning("Please enter a prompt.")

if __name__ == '__main__':
    main()
