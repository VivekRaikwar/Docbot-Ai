import streamlit as st
import aspose.pdf as pdf
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key= os.getenv("GROQ_API_KEY"),)


def chat(prompt): 
    chat_completion = client.chat.completions.create(
        messages=[ { "role": "user", "content": prompt,}],
        model="llama3-70b-8192",
    )
    return(chat_completion.choices[0].message.content)

def extract_text_from_pdf(pdf_file):
    input_pdf = pdf.Document(pdf_file)
    txt = pdf.text.TextAbsorber()
    txt.visit(input_pdf.pages[1])
    return txt.text

    
st.title("PDF Reader with Question Answering")
    
st.sidebar.header("Upload PDF")
uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type="pdf")
    
if uploaded_file is not None:
        st.sidebar.success("PDF file uploaded successfully!")
        with st.spinner('Extracting text from the PDF...'):
            pdf_text = extract_text_from_pdf(uploaded_file)
        
        st.sidebar.subheader("Extracted Text Preview")
        st.sidebar.text_area("Extracted Text", pdf_text[:500], height=200)  # Preview first 500 characters
        
        st.subheader("Ask Questions Based on PDF Content")
        question = st.text_input("Enter your question here:")
        
        if st.button("Get Answer"):
            if question:
                with st.spinner('Generating answer...'):
                    prompt = f"Act as an assistant and answer '{question}' based on the given data. data = {pdf_text}"
                    response = chat(prompt)
                st.success("Answer Generated!")
                st.subheader("Answer")
                st.write(response)
            else:
                st.error("Please enter a question")





