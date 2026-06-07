import logging
from src.utils import load_transcript, get_output_path
from src.docx_generator import generate_document
from src.gemini_client import call_gemini, parse_response, build_prompt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def main() -> None:
    """Main entry point for MeetFlow meeting processor."""
    
    try:
        print("MeetFlow - Processing your meeting notes...")
        transcript = load_transcript()
        prompt = build_prompt(transcript.raw_text)
        response = call_gemini(prompt)
        meeting = parse_response(response)
        if meeting:
            output_path = get_output_path()
            generate_document(meeting, output_path)
            logger.info(f"Meeting report generated successfully: {output_path}")
            print(f"Done! Report saved to: {output_path}")
    except Exception as e:
        logger.error(f"Failed to process meeting: {e}")
        raise

if __name__ == "__main__":
    main()

