from pathlib import Path
import logging
from datetime import datetime 

from src.models import MeetingTranscript
from src.config import Config

logger = logging.getLogger(__name__)


def load_transcript() -> MeetingTranscript:
    """
    Loads the meeting transcript from the input directory.

    Finds the first .txt file in the input directory, reads its content,
    and creates a MeetingTranscript object with the file's name as the title.

    Returns:
        MeetingTranscript: Object containing the transcript data

    Raises:
        FileNotFoundError: If no .txt file is found in the input directory
    """
    logger.info("Loading meeting transcript from input directory...")
    try:
        file_path = next(Config.INPUT_DIR.glob("*.txt"), None)
        if file_path is None:
            raise FileNotFoundError("No transcript file found in input directory")
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            file_name = Path(file_path).stem
            return MeetingTranscript(
                title=file_name,
                date=datetime.now().strftime('%Y-%m-%d'),
                participants=[],
                raw_text=content
            )

    except FileNotFoundError as e:
        logger.error(f"Error loading transcript: {e}")
        raise 

def get_output_path() -> Path:
    """
    Generates a timestamped output file path inside the output directory.

    Creates the output directory if it doesn't exist. The filename includes
    the current date and time for uniqueness.

    Returns:
        Path: Full path to the output file
    """
    output_dir = Config.OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return output_dir / f"output_{timestamp}.docx"



