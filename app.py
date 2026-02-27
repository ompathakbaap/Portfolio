from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Optional: set these via environment variables for easy customization
PROFILE = {
    "name": os.getenv("PROFILE_NAME", "Om Pathak"),
    "title": os.getenv("PROFILE_TITLE", "Software Engineer • Full‑Stack (React/Node) • MS CS Candidate"),
    "location": os.getenv("PROFILE_LOCATION", "Bethpage, New York"),
    "email": os.getenv("PROFILE_EMAIL", "ompathak61@gmail.com"),
    "phone": os.getenv("PROFILE_PHONE", "+1 (929) 240‑3270"),
    "github": os.getenv("PROFILE_GITHUB", "https://github.com/your-username"),
    "linkedin": os.getenv("PROFILE_LINKEDIN", "https://www.linkedin.com/in/your-handle/"),
}

DATA = {
    "summary": (
        "Aspiring Software Engineer with 1+ year of hands‑on experience building responsive, "
        "performance‑focused web applications. Strong in React, Node.js, and MySQL, with a solid "
        "computer science foundation (DSA, OS, architecture) and growing focus on Python & AI."
    ),
    "highlights": [
        {"k": "45%", "v": "Faster page loads via optimization"},
        {"k": "7+", "v": "Collaborated with multi‑dev teams"},
        {"k": "1+ yr", "v": "Industry experience in web dev"},
        {"k": "3.5", "v": "MS GPA (LIU, ongoing)"},
    ],
    "experience": [
        {
            "role": "Software Development Engineer",
            "company": "Apex Sports",
            "where": "Ahmedabad, India",
            "dates": "Jul 2023 – Aug 2024",
            "bullets": [
                "Designed and developed front‑end components for an e‑commerce platform using React, improving visual polish and usability.",
                "Partnered with UI/UX teams to translate requirements into scalable, responsive interfaces.",
                "Applied performance best practices, reducing page load time by ~45%.",
                "Tested and debugged across browsers/devices to ensure consistent behavior."
            ],
            "tags": ["React", "Frontend", "Performance", "Testing"],
        },
        {
            "role": "Software Engineer Intern",
            "company": "DAS Infomedia",
            "where": "Ahmedabad, India",
            "dates": "Jan 2023 – May 2023",
            "bullets": [
                "Built a hospital management system using React, Node.js, and MySQL to streamline operations and improve patient workflows.",
                "Collaborated with a 7‑person dev team to deliver user‑friendly interfaces, improving efficiency by ~27%.",
                "Integrated secure backend services in Node.js; reduced data retrieval time by ~33%.",
                "Performed thorough testing/debugging, decreasing system errors and improving stability."
            ],
            "tags": ["React", "Node.js", "MySQL", "APIs"],
        },
    ],
    "projects": [
        {
            "name": "Streaming Website (University Project)",
            "desc": "A fully functional streaming web app designed, implemented, and tested with a focus on UX and reliability.",
            "stack": ["Web App", "UI/UX", "Testing"],
            "link": "https://github.com/your-username/streaming-project"
        },
        {
            "name": "Autonomous Drone (AI Project)",
            "desc": "Designed and implemented an autonomous drone as part of an AI course project, strengthening applied problem‑solving skills.",
            "stack": ["Python", "AI", "Robotics"],
            "link": "https://github.com/your-username/autonomous-drone"
        },
        {
            "name": "Hospital Management System",
            "desc": "Full‑stack system with React + Node.js + MySQL to improve hospital operations and patient management.",
            "stack": ["React", "Node.js", "MySQL"],
            "link": "https://github.com/your-username/hospital-management"
        },
        {
            "name": "E‑commerce Frontend Components",
            "desc": "Reusable, responsive React components with performance improvements and cross‑browser support.",
            "stack": ["React", "Performance", "Responsive UI"],
            "link": "https://github.com/your-username/ecommerce-ui"
        },
    ],
    "skills": {
        "Languages": ["Python", "JavaScript", "C", "C++", "C#"],
        "Frameworks": ["React", "Node.js", "Flask (this site)"],
        "CS Core": ["Data Structures", "Algorithms", "Operating Systems", "Computer Architecture"],
        "Engineering": ["Debugging", "Agile Development", "Software Development Lifecycle", "Technical Documentation"],
    },
    "education": [
        {
            "degree": "M.S. in Computer Science (Expected May 2026)",
            "school": "Long Island University, Brooklyn, NY",
            "details": [
                "GPA: 3.5 • Coursework: Data Structures, Operating Systems, Computer Architecture",
                "Applied Python and AI in complex problem‑solving projects",
            ],
        },
        {
            "degree": "B.Tech in Computer Science (May 2023)",
            "school": "Silver Oak University, Ahmedabad, India",
            "details": [
                "CGPA: 9.1 • Strong foundation in algorithms, data structures, and software engineering",
                "Built a complete streaming website as a capstone‑style project",
            ],
        },
    ],
}

@app.route("/")
def index():
    return render_template("index.html", profile=PROFILE, data=DATA)

@app.route("/resume")
def resume():
    # Resume is served from static/Om_Pathak_Resume.pdf
    return send_from_directory(os.path.join(app.root_path, "static"), "Om_Pathak_Resume.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
