import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models import MeetingTranscript, MeetingOutput, ActionItem, Risk
from src.utils import get_output_path


def test_action_item_creation():
    item = ActionItem(task="Finish backend", owner="Bob", deadline="Friday", priority="high")
    assert item.task == "Finish backend"
    assert item.owner == "Bob"


def test_risk_creation():
    risk = Risk(description="API delay", severity="medium")
    assert risk.description == "API delay"
    assert risk.severity == "medium"


def test_meeting_output_defaults():
    output = MeetingOutput()
    assert output.summary == ""
    assert output.action_items == []
    assert output.risks == []


def test_meeting_transcript_creation():
    transcript = MeetingTranscript(title="Test", date="2026-06-07", raw_text="Some notes")
    assert transcript.title == "Test"
    assert transcript.participants == []


def test_get_output_path():
    path = get_output_path()
    assert str(path).endswith(".docx")
    assert "output_" in str(path)