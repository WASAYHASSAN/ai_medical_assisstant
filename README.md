# 🩺 Medical Report Analyzer Chatbot

A smart, real-time **AI chatbot** that helps users understand and interact with their own **medical reports**. Powered by **Google's Gemini Flash 1.5** and designed with **custom report parsing and prompt engineering**, this system enables natural language conversations with a patient's uploaded medical document.

Whether you're a patient seeking clarity or a doctor looking for quick insights, this app bridges the gap between complex data and clear understanding.

---

## What It Can Do

- **Accepts medical reports** in `.pdf` or `.txt` format
- **Cleans and extracts meaningful content** from messy, unstructured documents
- **Builds intelligent prompts** from the parsed report
- **Queries Gemini Flash 1.5** to provide clear, reliable responses
- Lets users ask natural language questions like:
  - *“What does this report say about my cholesterol?”*
  - *“Do these values indicate diabetes?”*
  - *“Summarize my test results in simple words.”*

---

## ✅ Features

| Feature                             | Description                                      |
|-------------------------------------|--------------------------------------------------|
|  Upload PDF or Text Report        | Medical documents supported (.pdf / .txt)        |
|  Report Cleaning & Preprocessing  | Removes headers, page numbers, junk characters   |
|  Prompt Engineering                | Custom-built prompts with injected report text   |
|  Conversational Q&A               | Ask follow-up questions about your report        |
|  Gemini Flash 1.5 API              | Fast & accurate responses using Google GenAI     |
|  Web App Interface                 | Built using Streamlit for instant accessibility  |

---

##  How It Works

1. **Upload** your medical report.
2. The system **extracts and cleans** the content.
3. A custom **prompt is generated**, combining:
   - User's report text (or summary)
   - User's natural language question
4. The prompt is sent to **Gemini Flash 1.5** via **Google Generative AI API**.
5. The response is shown with clarity, simplicity, and context awareness.

---


