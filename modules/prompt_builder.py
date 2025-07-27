def build_medical_prompt(report_text, symptoms):
    prompt = f"""
You are an experienced and careful medical doctor.

You are provided:
1. Medical report(s): (these may contain blood test values, scans, summaries, or handwritten text)
------------------------
{report_text}
------------------------

2. Patient's described symptoms:
------------------------
{symptoms}
------------------------

TASK:
- Analyze the reports and symptoms carefully.
- Give a detailed and professional medical summary.
- Mention abnormalities, possible diagnosis, and connections between lab findings and symptoms.
- Include advice or recommendations.
- Do NOT display as a table. Just speak like a doctor would talk to a patient.
"""

    return prompt
