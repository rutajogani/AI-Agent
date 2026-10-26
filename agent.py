import os
from datatime import datetime

from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider
from ollama import chat

model = OllamaModel(
    "qwen3.5:2b",
    provider = OllamaProvider(base_url = "http://localhost:11434/v1")
)

response = chat(
    model='phonon',
    messages=[{'role': 'user', 'content': 'Hello!'}],
)
print(response.message.content)

NOTES_FILE = "notes.txt"

def get_current_time() -> str: 
    return datetime.now().strftime("%A, %B, %d, %Y at %I:%M  %p")

def calculation(expression: str) -> str: 
    if not set(expression) <= set("0123456789+-*/(). "):
        return "Error : Only Number and + - * / () are allowed"
    try:
        return str(eval(expression))
    except Exception as error:
        return f"Error: {error}"
        
def save_note(note:  str) -> str:
    with open(NOTES_FILE, "a", encoding="utf-8")as file:
        file.write(f"- {note}\n")
    return "Note saved"

def read_notes() -> str:
    if not os.path.exists(NOTES_FILE):
        return "No notes saved yet!"
    with open(NOTES_FILE, encoding="utf-8")as file:
        return file.read()
    