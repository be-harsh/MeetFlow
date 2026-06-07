import unittest
import sys
import os
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models import MeetingTranscript, MeetingOutput, ActionItem, Risk
from src.utils import load_transcript, get_output_path


class TestModels(unittest.TestCase):
    def test_meeting_transcript_creation(self):
        transcript = MeetingTranscript(
            title="Test Meeting",
            date="2026-05-25",
            participants=["Alice", "Bob"],
            raw_text="This is a test transcript"
        )
        self.assertEqual(transcript.title, "Test Meeting")
        self.assertEqual(len(transcript.participants), 2)

    def test_action_item_creation(self):
        item = ActionItem(
            task="Finish backend",
            owner="Bob",
            deadline="Friday",
            priority="High"
        )
        self.assertEqual(item.task, "Finish backend")
        self.assertEqual(item.owner, "Bob")

    def test_risk_creation(self):
        risk = Risk(
            description="API delay",
            severity="Medium"
        )
        self.assertEqual(risk.description, "API delay")

    def test_meeting_output_creation(self):
        output = MeetingOutput(
            summary="Test summary",
            key_points=["Point 1", "Point 2"],
            action_items=[ActionItem(task="Task 1")],
            risks=[Risk(description="Risk 1")],
            decisions=["Decision 1"]
        )
        self.assertEqual(output.summary, "Test summary")
        self.assertEqual(len(output.key_points), 2)


class TestUtils(unittest.TestCase):
    def test_get_output_path(self):
        path = get_output_path()
        self.assertTrue(str(path).endswith(".docx"))
        self.assertTrue("output_" in str(path))


if __name__ == "__main__":
    unittest.main()
