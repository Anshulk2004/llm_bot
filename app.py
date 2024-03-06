from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

# Function to load OpenAI model and get responses
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.environ["OPEN_API_KEY"], model_name="gpt-3.5-turbo-instruct", temperature=0.5)
    response = llm.predict(question)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Question and Answer")

st.header("LLM Application")
input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the Question")

if submit:
    response = get_openai_response(input_text)
    st.subheader("The response is:")
    st.write(response)

