from flask import Flask, render_template, request
from resume_parser import extract_text, extract_skills

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume_file = request.files["resume"]
        resume_file.save("uploaded_resume.pdf")
        text = extract_text("uploaded_resume.pdf")
        skills = extract_skills(text)
        return render_template("result.html", skills=skills, text=text[:500]+"...")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
