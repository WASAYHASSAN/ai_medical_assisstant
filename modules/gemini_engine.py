import google.generativeai as genai

def load_gemini_pro(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("models/gemini-1.5-flash-latest")

def contains_critical_alert(text):
    critical_keywords = [
        "critical", "urgent", "emergency", "severely", "life-threatening",
        "hospital", "ICU", "immediate medical attention"
    ]
    return any(word in text.lower() for word in critical_keywords)
