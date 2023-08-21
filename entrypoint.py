from fastapi import FastAPI
from uvicorn import run

from main import app  # Import the FastAPI app instance from main.py

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
