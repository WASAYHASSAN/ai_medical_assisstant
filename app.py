import streamlit as st
from PIL import Image
import fitz  
import pytesseract

from modules.gemini_engine import load_gemini_pro, contains_critical_alert
from modules.report_parser import combine_multiple_reports

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ------------------------
# Page Setup
# ------------------------
st.set_page_config(page_title="AI Medical Chatbot", layout="wide")
st.title("AI Medical Assistant")
st.markdown("Upload your reports once, then ask follow-up questions just like a real medical consultation.")

# ------------------------
# API Key Handling
# ------------------------
if "api_key" not in st.session_state:
    st.session_state.api_key = st.secrets["gemini"]["api_key"]

if not st.session_state.api_key:
    api_input = st.text_input("Enter your Gemini API Key", type="password")
    if api_input:
        st.session_state.api_key = api_input
        st.success("API Key saved for this session.")
else:
    st.markdown("**API Key is active.** _(Refresh to reset)_")

# ------------------------
# Report Upload
# ------------------------
uploaded_files = st.file_uploader(
    "Upload Medical Reports (PDF or Images)", 
    type=["pdf", "png", "jpg", "jpeg"], 
    accept_multiple_files=True
)

# ------------------------
# Session States
# ------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "report_context" not in st.session_state:
    st.session_state.report_context = ""

# ------------------------
# OCR Function
# ------------------------
def extract_text(file):
    text = ""
    if file.type == "application/pdf":
        doc = fitz.open(stream=file.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
    elif file.type.startswith("image/"):
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
    return text

# ------------------------
# Process Uploaded Reports
# ------------------------
if uploaded_files and not st.session_state.report_context:
    extracted = [extract_text(f) for f in uploaded_files]
    st.session_state.report_context = combine_multiple_reports(extracted)
    st.success("✅ Reports processed successfully.")

# ------------------------
# Chat Display
# ------------------------
for msg in st.session_state.messages:
    role = " Doctor" if msg["role"] == "ai" else "🧍 You"
    st.chat_message(role).markdown(msg["content"])

# ------------------------
# User Chat Input
# ------------------------
user_input = st.chat_input("Ask a medical question or describe symptoms...")

if user_input:
    #user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    #conversation context
    full_prompt = "You are a medical doctor.\n\n"
    full_prompt += "The patient has uploaded the following reports:\n"
    full_prompt += st.session_state.report_context + "\n\n"
    full_prompt += "Conversation:\n"
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            full_prompt += f"Patient: {msg['content']}\n"
        else:
            full_prompt += f"Doctor: {msg['content']}\n"

    #Gemini Pro model
    model = load_gemini_pro(st.session_state.api_key)

    with st.chat_message("Doctor"):
        with st.spinner("Analyzing..."):
            response = model.generate_content(full_prompt)
            reply = response.text
            st.markdown(reply)
            st.session_state.messages.append({"role": "ai", "content": reply})

        #critical alerts
        if contains_critical_alert(reply):
            st.error("This response may contain **critical alerts**. Please consult a real doctor immediately.")
