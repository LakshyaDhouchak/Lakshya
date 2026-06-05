from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()
model = ChatOllama(model = "minimax-m3:cloud", temperature= 0.5)

 
st.header("Research Tool")

# Define the parameter
ResearchPaper = st.selectbox("Enter the Research paper name:",  ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )
ModeLevel = st.selectbox("Enter the difficuly mode:", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])
length = st.selectbox("Enter the length of the result:",["Short(1-2 paragraph)","Medium(3-5 paragtaph)","Long (Detail Explanation)"])
template = load_prompt('template.json')

prompt = template.invoke({
    'paper_input':ResearchPaper,
    'style_input':ModeLevel,
    'length_input':length
}
)

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)