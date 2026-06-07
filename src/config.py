import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


class Config:
    """
    Configuration settings for the Smart Meeting Notes Processor.

    This class holds all static configuration values used across the application,
    including file paths, API settings, and model configurations.

    Attributes:
        BASE_DIR: Root directory of the src package
        INPUT_DIR: Directory where meeting transcripts are stored
        OUTPUT_DIR: Directory where generated reports are saved
        MODEL_NAME: Name of the Gemini model to use
        GEMINI_API_KEY: API key for Gemini (loaded from .env)
        GEMINI_API_URL: Full URL for the Gemini API endpoint
        GEMINI_API_TIMEOUT: Maximum time to wait for API response
        SLEEP_TIME: Delay after API calls (for rate limiting)
    """
    BASE_DIR = Path(__file__).resolve().parent
    INPUT_DIR = BASE_DIR.parent / "input"
    OUTPUT_DIR = BASE_DIR.parent / "output"
    MODEL_NAME = "gemini-2.5-flash"
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"
    GEMINI_API_TIMEOUT = 60
    SLEEP_TIME = 5
