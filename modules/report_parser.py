import re

def clean_report_text(raw_text):
    """
    Clean unwanted characters, headers, page numbers etc.
    """
    
    cleaned = re.sub(r"\n\s*\n", "\n", raw_text)
    cleaned = re.sub(r"[ \t]+", " ", cleaned)
    cleaned = re.sub(r"Page\s*\d+\s*of\s*\d+", "", cleaned, flags=re.I)
    lines = cleaned.splitlines()
    meaningful_lines = [line.strip() for line in lines if len(line.strip()) > 2]
    final_text = "\n".join(meaningful_lines)

    return final_text


def combine_multiple_reports(report_texts):
    """
    Join multiple cleaned reports into a single block.
    """
    return "\n\n--- End of Report ---\n\n".join([clean_report_text(txt) for txt in report_texts])
