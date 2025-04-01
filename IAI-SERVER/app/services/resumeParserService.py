import re
import fitz  # PyMuPDF for PDFs
import docx
import spacy
from spacy.matcher import Matcher
from fastapi import UploadFile
import shutil

nlp = spacy.load("en_core_web_sm")

async def parseResume(resume: UploadFile, upload_dir: str):
    """Extracts text and structured data from a resume file."""
    content = ""
    resume_path = f"{upload_dir}/{resume.filename}"  # Define file path

    # ✅ Read and extract text from resume
    if resume.filename.endswith(".pdf"):
        with fitz.open(stream=resume.file.read(), filetype="pdf") as doc:
            content = " ".join([page.get_text() for page in doc])

    elif resume.filename.endswith(".docx"):
        doc = docx.Document(resume.file)
        content = " ".join([para.text for para in doc.paragraphs])

    else:
        raise ValueError("Unsupported resume format. Use PDF or DOCX.")

    # ✅ Save the resume file
    with open(resume_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    extracted_data = extract_resume_details(content)  # Process extracted text

    return content[:5000], extracted_data, resume_path  # Limit stored text

def extract_resume_details(text):
    """Extracts structured data (name, email, phone, skills, experience, education) from resume text."""
    doc = nlp(text)

    extracted_data = {
        "Name": extract_name(doc),
        "Emails": extract_emails(text),
        "Phones": extract_phones(text),
        "Skills": extract_skills(text),
        "Experience": extract_sections(text, ["Experience", "Work History"]),
        "Education": extract_sections(text, ["Education", "Degrees"]),
    }

    return extracted_data

def extract_emails(text):
    """Extracts email addresses from text."""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

def extract_phones(text):
    phone_pattern = r'''
        \+?\d{1,4}              # Optional international code: + or no +, followed by 1-4 digits
        [\s.-]?                 # Optional separator: space, dot, or hyphen
        \(?\d{1,4}\)?           # Optional area code in parentheses (1-4 digits)
        [\s.-]?                 # Optional separator: space, dot, or hyphen
        \d{1,4}                 # First part of the phone number (1-4 digits)
        [\s.-]?                 # Optional separator: space, dot, or hyphen
        \d{1,4}                 # Second part of the phone number (1-4 digits)
        [\s.-]?                 # Optional separator: space, dot, or hyphen
        \d{1,4}                 # Third part of the phone number (1-4 digits)
        [\s.-]?                 # Optional separator: space, dot, or hyphen
        \d{4,12}                # Final part of the phone number (4-12 digits)
    '''
    phones = re.findall(phone_pattern, text, re.VERBOSE)
    phone_numbers = [phone.strip() for phone in phones if phone.strip()]
    return phone_numbers if phone_numbers else None

def extract_skills(text):
    skill_set = {'python', 'html', 'java', 'react', 'aws', 'machine learning', 'data science', 'sql', 'docker'}
    found_skills = []
    for token in nlp(text):
        if token.text.lower() in skill_set:
            found_skills.append(token.text)
    return list(set(found_skills))

def extract_sections(text, keywords):
    """Identifies sections like Experience, Education in resume text."""
    lines = text.split("\n")
    section_data = []

    for i, line in enumerate(lines):
        for keyword in keywords:
            if keyword.lower() in line.lower():
                section_data.extend(lines[i+1:i+5])  # Capture next few lines

    return "\n".join(section_data).strip()

def extract_name(doc):
    """Extracts name using NLP matcher."""
    matcher = Matcher(nlp.vocab)
    pattern = [{"POS": "PROPN"}, {"POS": "PROPN"}]  # Look for two proper nouns
    matcher.add("NAME", [pattern])

    matches = matcher(doc)
    for match_id, start, end in matches:
        return doc[start:end].text  # First match assumed as name

    return None  # No name found
