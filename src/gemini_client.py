from models import MeetingOutput, ActionItem, Risk
from config import Config
import time
import logging
import requests
import json

logger = logging.getLogger(__name__)


def build_prompt(raw_text: str) -> str:
    """
    Builds a structured prompt for the Gemini API to analyze the meeting transcript.

    Instructs Gemini to return a JSON object with specific fields.

    Args:
        raw_text: The full text of the meeting transcript

    Returns:
        str: Formatted prompt ready to send to the Gemini API
    """
    return f"""You are a professional meeting assistant.
Read this transcript and return ONLY a JSON object. No extra text. No markdown.

The JSON must have exactly these five keys:
- summary: 2-3 sentence summary (string)
- key_points: important points (array of strings)
- action_items: list of tasks, each with task, owner, deadline, priority (array of objects)
- risks: list of risks, each with description, severity (array of objects)
- decisions: final decisions made (array of strings)

Meeting Transcript:
{raw_text}"""


def call_gemini(prompt: str) -> str:
    """
    Calls the Gemini API with the given prompt and returns the response text.

    Includes error handling and rate limiting.

    Args:
        prompt: The prompt to send to the API

    Returns:
        str: Raw text response from the Gemini API

    Raises:
        Exception: If the API call fails for any reason
    """
    try:
        url = f"{Config.GEMINI_API_URL}?key={Config.GEMINI_API_KEY}"
        response = requests.post(url, json={
            "contents": [{"parts": [{"text": prompt}]}]
        })
        response.raise_for_status()
        time.sleep(Config.SLEEP_TIME)
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        logger.error(f"Error calling Gemini: {e}")
        raise


def parse_response(response: str) -> MeetingOutput:
    """
    Parses the JSON response from the Gemini API into a MeetingOutput object.

    Handles any missing fields by providing defaults.

    Args:
        response: Raw JSON string from the API response

    Returns:
        MeetingOutput: Structured meeting data object

    Raises:
        Exception: If JSON parsing fails
    """
    try:
        # Clean response in case Gemini adds markdown code blocks
        clean = response.strip()
        if clean.startswith("```"):
            clean = clean.split("\n", 1)[1]
        if clean.endswith("```"):
            clean = clean.rsplit("```", 1)[0]
        clean = clean.strip()
        data = json.loads(clean)
        action_items = [ActionItem(**item) for item in data.get("action_items", [])]
        risks = [Risk(**item) for item in data.get("risks", [])]
        return MeetingOutput(
            summary=data.get("summary", ""),
            key_points=data.get("key_points", []),
            action_items=action_items,
            risks=risks,
            decisions=data.get("decisions", [])
        )
    except Exception as e:
        logger.error(f"Error parsing response: {e}")
        raise
    