# 🚀 Personal Portfolio Website (Flask)

A dynamic personal portfolio website built using **Flask** to showcase
experience, projects, technical skills, and provide a downloadable
resume.

This project demonstrates backend fundamentals, structured data
rendering, environment configuration, and clean full-stack organization
using Python and Flask.

------------------------------------------------------------------------

## 🌟 Features

-   Dynamic profile configuration using environment variables
-   Experience, education, and projects rendered via structured data
-   Resume download endpoint (`/resume`)
-   Clean separation of templates and static assets
-   Lightweight and deployment-ready structure

------------------------------------------------------------------------

## 🛠 Tech Stack

-   **Backend:** Python, Flask
-   **Frontend:** HTML, CSS, JavaScript
-   **Templating Engine:** Jinja2
-   **Configuration:** Environment Variables
-   **Static Asset Management:** Flask static directory

------------------------------------------------------------------------

## 📂 Project Structure

    portfolio-site/
    │
    ├── app.py
    ├── templates/
    │   ├── base.html
    │   └── index.html
    │
    ├── static/
    │   ├── css/
    │   ├── js/
    │   ├── img/
    │   └── Om_Pathak_Resume.pdf
    │
    └── README.md

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create Virtual Environment (Recommended)

``` bash
python -m venv venv
```

Activate virtual environment:

-   **Windows**

``` bash
venv\Scripts\activate
```

-   **Mac/Linux**

``` bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

``` bash
pip install flask
```

### 4️⃣ Run the Application

``` bash
python app.py
```

Visit in browser:

http://127.0.0.1:5000/

------------------------------------------------------------------------

## 🔧 Environment Variable Customization (Optional)

You can customize profile details without modifying code.

### Mac/Linux:

``` bash
export PROFILE_NAME="Your Name"
export PROFILE_EMAIL="your@email.com"
export PROFILE_GITHUB="https://github.com/yourusername"
```

### Windows:

``` bash
set PROFILE_NAME=Your Name
```

------------------------------------------------------------------------

## 📄 Resume Download

The resume is served from the static folder via:

http://127.0.0.1:5000/resume

------------------------------------------------------------------------

## 🎯 What This Project Demonstrates

-   Backend routing using Flask
-   Template rendering with dynamic data
-   Static file serving
-   Structured project organization
-   Resume asset handling
-   Deployment-ready Python application structure

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Docker containerization
-   Cloud deployment (AWS / Render / Railway)
-   Contact form with email integration
-   Database-backed project storage
-   CI/CD integration

------------------------------------------------------------------------

## 👨‍💻 Author

**Om Pathak**\
MS Computer Science (Expected 2026)\
New York, USA\
Email: ompathak61@gmail.com

------------------------------------------------------------------------

⭐ If you found this useful, feel free to fork or star the repository!
