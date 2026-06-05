from langchain_ollama import ChatOllama
from dotenv import load_dotenv
#from langchain_core.messages import HumanMessage
import streamlit as st 

load_dotenv()
st.header('Research Tools')
UserInput = st.text_input("Enter the prompt")
model = ChatOllama(model ="minimax-m3:cloud", temperature=0.5)
if st.button('Summarize'):
    result = model.invoke(UserInput)
    st.write(result.content)

  