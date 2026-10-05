# 📝 Flask Blog Website

A modern and responsive **Blog Website** built using **Python Flask, HTML, CSS, and Bootstrap 5**.  
The project contains multiple blog categories such as Technology, Lifestyle, and Travel, along with About and Contact pages.

---

## 🚀 Project Overview

This project is a Flask-based blog website designed to provide users with a clean and responsive interface for reading and exploring blog content.

The website includes:

- 🏠 Home Page
- 💻 Technology Page
- 🌿 Lifestyle Page
- ✈️ Travel Page
- 👨‍💻 About Page
- 📩 Contact Page
- 📱 Responsive Design
- 🎨 Bootstrap 5 UI
- 🔗 Flask URL Routing
- 📬 Contact Form

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| HTML5 | Page structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive UI |
| Jinja2 | Flask template rendering |
| JavaScript | Interactive components |

---

## 📂 Project Structure

```text
flask-blog/
│
├── app.py
│
├── templates/
│   ├── home.html
│   ├── technology.html
│   ├── lifestyle.html
│   ├── travel.html
│   ├── about.html
│   └── contact.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│
├── requirements.txt
│
└── README.md
```

---

## ✨ Features

### 🏠 Home Page

The home page provides an overview of the blog and contains:

- Featured blog
- Latest articles
- Blog categories
- Popular articles
- Newsletter section
- Responsive navigation

### 💻 Technology

The Technology section contains technology-related blog posts covering topics such as:

- Web Development
- Python
- Artificial Intelligence
- Software Development
- Programming

### 🌿 Lifestyle

The Lifestyle section contains articles related to:

- Health & Wellness
- Productivity
- Personal Development
- Daily Lifestyle
- Fitness

### ✈️ Travel

The Travel section provides travel-related content including:

- Travel destinations
- Travel guides
- Adventure
- Tourism
- Travel tips

### 👨‍💻 About

The About page provides information about the blog and its purpose.

### 📩 Contact

The Contact page provides:

- Contact information
- Contact form
- Name field
- Email field
- Subject field
- Message field
- FAQ section

---

## 🔗 Flask Routing

The application uses Flask routes to navigate between pages.

```python
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/technology")
def technology():
    return render_template("technology.html")


@app.route("/lifestyle")
def lifestyle():
    return render_template("lifestyle.html")


@app.route("/travel")
def travel():
    return render_template("travel.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
```

---

## 🔄 Flask Template Navigation

Instead of directly linking HTML files, Flask's `url_for()` function is used.

Example:

```html
<a href="{{ url_for('home') }}">Home</a>

<a href="{{ url_for('technology') }}">Technology</a>

<a href="{{ url_for('lifestyle') }}">Lifestyle</a>

<a href="{{ url_for('travel') }}">Travel</a>

<a href="{{ url_for('about') }}">About</a>

<a href="{{ url_for('contact') }}">Contact</a>
```

This allows Flask to correctly handle page routing.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask-blog.git
```

### 2. Navigate to the Project

```bash
cd flask-blog
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run the Flask application:

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000/
```

Open the URL in your browser.

---

## 📦 Requirements

Example `requirements.txt`:

```text
Flask
```

You can generate the requirements file using:

```bash
pip freeze > requirements.txt
```

---

## 📄 Available Pages

| Page | URL |
|---|---|
| Home | `/` |
| Technology | `/technology` |
| Lifestyle | `/lifestyle` |
| Travel | `/travel` |
| About | `/about` |
| Contact | `/contact` |

---

## 📱 Responsive Design

The website is designed using **Bootstrap 5**, making it responsive across:

- 💻 Desktop
- 💻 Laptop
- 📱 Mobile
- 📲 Tablet

Bootstrap's grid system and responsive components are used to maintain a consistent layout across different screen sizes.

---

## 📬 Contact Form

The contact form can be handled using Flask.

Example:

```python
@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        print(name, email, subject, message)

        return "Message sent successfully!"

    return render_template("contact.html")
```

For production, the form can later be connected to a database or email service.

---

## 🔮 Future Enhancements

The project can be extended with:

- 🔐 User Authentication
- 👤 User Registration & Login
- ✍️ Create Blog Posts
- 📝 Edit & Delete Posts
- 💬 Comments
- ❤️ Like System
- 🔎 Blog Search
- 🏷️ Tags & Categories
- 🗄️ MySQL Database
- 👨‍💼 Admin Dashboard
- 📧 Email Notifications
- 🌐 REST API
- ☁️ Cloud Deployment

---

## ☁️ Deployment

This project uses Flask/Python on the backend.

For a complete Flask application, it should be deployed on a platform that supports Python/Flask applications.

For example:

- Render
- Railway
- PythonAnywhere
- Fly.io

**Netlify** can be used if the project is converted into a static website, but the Flask backend and Python routes will not run as a normal Netlify static deployment.

---

## 👨‍💻 Author

**Ashish Gupta**

Python / Flask Developer

### Skills

- Python
- Flask
- Django
- React
- HTML
- CSS
- Bootstrap
- JavaScript
- MySQL
- Git & GitHub

---

## 📜 License

This project is created for learning and development purposes.

You are free to modify and improve the project according to your requirements.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
