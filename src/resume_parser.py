
---

### **File: src/resume_parser.py**
```python
import PyPDF2
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_skills(text):
    doc = nlp(text.lower())
    skills_list = ["python", "java", "c++", "machine learning", "flask", "django", "sql"]
    extracted = [skill for skill in skills_list if skill in text.lower()]
    return extracted
