from dataclasses import dataclass, field
from typing import List


@dataclass
class ActionItem:
    """
    Represents a single action item extracted from a meeting transcript.

    Attributes:
        task: Description of the task to be completed
        owner: Person responsible for the task
        deadline: Date/time when the task should be completed
        priority: Priority level of the task (e.g., High, Medium, Low)
    """
    task: str
    owner: str = ""
    deadline: str = ""
    priority: str = ""


@dataclass
class Risk:
    """
    Represents a single risk identified during a meeting.

    Attributes:
        description: Description of the risk
        severity: Severity level of the risk (e.g., High, Medium, Low)
    """
    description: str
    severity: str = ""


@dataclass
class MeetingOutput:
    """
    Represents the full structured output after processing a meeting transcript.

    This class contains all the analyzed information from the meeting, ready
    to be formatted into a report.

    Attributes:
        summary: Brief 2-3 sentence summary of the meeting
        key_points: List of important discussion points
        action_items: List of actionable tasks from the meeting
        risks: List of identified risks
        decisions: List of decisions made during the meeting
    """
    summary: str = ""
    key_points: List[str] = field(default_factory=list)
    action_items: List[ActionItem] = field(default_factory=list)
    risks: List[Risk] = field(default_factory=list)
    decisions: List[str] = field(default_factory=list)


@dataclass
class MeetingTranscript:
    """
    Represents the raw input meeting transcript.

    Attributes:
        title: Title of the meeting (usually from the filename)
        date: Date the transcript was processed
        participants: List of meeting attendees
        raw_text: Full unprocessed text of the meeting transcript
    """
    title: str
    date: str
    participants: List[str] = field(default_factory=list)
    raw_text: str = ""
