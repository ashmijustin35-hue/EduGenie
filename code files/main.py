Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create FastAPI application
app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)

# Templates folder
templates = Jinja2Templates(directory="templates")

# Static files folder
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Display the EduGenie home page.
    """
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "answer": None
        }
    )


@app.post("/ask", response_class=HTMLResponse)
async def ask_question(
    request: Request,
    question: str = Form(...)
):
    """
    Receive a question from the user and generate
    an educational response.
    """

    answer = generate_answer(question)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "question": question,
            "answer": answer
        }
    )


def generate_answer(question: str) -> str:
    """
    Generate an answer using Google Gemini.

    The Gemini API integration can be connected here.
    """
... 
...     api_key = os.getenv("GEMINI_API_KEY")
... 
...     if not api_key:
...         return (
...             "Gemini API key is not configured. "
...             "Please add GEMINI_API_KEY to your .env file."
...         )
... 
...     try:
...         # Gemini API integration
...         from google import genai
... 
...         client = genai.Client(api_key=api_key)
... 
...         response = client.models.generate_content(
...             model="gemini-2.5-flash",
...             contents=(
...                 "You are EduGenie, a helpful educational learning assistant. "
...                 "Explain the following question clearly and simply for a student:\n\n"
...                 + question
...             )
...         )
... 
...         return response.text
... 
...     except Exception as error:
...         return f"Unable to generate an answer: {error}"
... 
... 
... @app.get("/health")
... async def health_check():
...     """
...     Check whether the EduGenie server is running.
...     """
...     return {
...         "status": "success",
...         "message": "EduGenie is running successfully!"
