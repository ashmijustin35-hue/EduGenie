# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is an AI-powered learning assistant developed using Python, FastAPI, HTML, CSS, and the Google Gemini API.

The system helps students ask questions and receive simple, clear, and educational answers using Google's Gemini generative AI model.

---

## 1. Project Overview

EduGenie is designed to provide an interactive learning environment for students.

Students can enter questions through a web interface, and EduGenie sends the question to the Google Gemini API. The generated response is then displayed on the website.

### Main Objectives

- Provide AI-powered educational assistance.
- Allow students to ask questions using a simple web interface.
- Generate easy-to-understand answers.
- Support different learning topics.
- Provide a lightweight and user-friendly application.
- Demonstrate the integration of Google Gemini with FastAPI.

---

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend web framework |
| Google Gemini | AI response generation |
| Jinja2 | HTML templating |
| Pydantic | Data validation |
| Uvicorn | ASGI server |
| HTML | Frontend structure |
| CSS | Frontend styling |
| python-dotenv | Environment configuration |

---

## 3. Features

### AI Question Answering

Students can enter a question and receive an AI-generated educational answer.

### Simple Web Interface

The application provides an easy-to-use interface for students.

### Gemini Integration

EduGenie uses the Google Gemini API to generate responses.

### FastAPI Backend

FastAPI handles requests and connects the frontend with the Gemini AI service.

### Health Check

The application provides a health-check endpoint to verify that the server is running.

---

## 4. Project Structure

```text
EduGenie/
│
├── main.py
├── models.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
