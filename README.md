# 📝 PDF Reader with Question Answering

Welcome to the **PDF Reader with Question Answering** project! This app allows you to upload a PDF, extract its text, and ask questions based on the content of the PDF. Powered by **Groq's Llama-3-70b** model, the application uses AI to provide accurate answers related to the uploaded document.

## 🌟 Key Features  
- 📄 **PDF Text Extraction**: Upload a PDF and automatically extract the text from its pages.  
- 🤖 **AI-Powered Q&A**: Ask questions based on the extracted text and get AI-driven answers using the **Groq API** and **Llama-3-70b model**.  
- 🧑‍💻 **Interactive UI**: Built with **Streamlit**, allowing you to upload files and interact with the assistant effortlessly.  

## 🚀 Getting Started  

### Prerequisites  
- Python 3.8+  
- Groq API key  
- Installed Python packages (listed in `requirements.txt`)  

### Installation  
```bash  
git clone https://github.com/your-username/pdf-reader-qa.git  
cd pdf-reader-qa  
pip install -r requirements.txt  
```  

### Environment Variables  
Create a `.env` file in the root directory with the following variables:  
```bash  
GROQ_API_KEY=your_groq_api_key  
```  

## 🏗️ Project Structure  
```bash  
├── app.py              # Main Streamlit application  
├── requirements.txt    # Python dependencies  
├── .env                # Environment variables (not included in repo)  
├── README.md           # Project documentation  
```  

## 🛠️ Tech Stack  
- **Python** (Backend logic)  
- **Streamlit** (Frontend UI)  
- **Aspose.PDF** (For PDF text extraction)  
- **Groq API** (LLM-powered responses)  

## ✍️ Usage Instructions  
1. Launch the app by running:  
```bash  
streamlit run app.py  
```  
2. Upload a PDF file using the sidebar.  
3. View the extracted text preview in the sidebar.  
4. Enter your question based on the PDF content.  
5. Get the AI-generated answer to your question!  

## 📬 Contact  
Maintained by **VIVEK RAIKWAR**.

 For any queries or collaborations, feel free to connect!
