import re

def clean_prompt(prompt):
    return re.sub(r"[^\w\s]", "", prompt).strip().lower()
