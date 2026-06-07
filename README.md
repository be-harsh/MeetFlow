# MeetFlow - Meeting Minutes Generator

A Python tool that uses Google Gemini AI to automatically generate professional meeting minutes from transcript files.

## Features

- Reads meeting transcripts from text files
- Uses Google Gemini AI to analyze and generate structured minutes
- Exports minutes as DOCX files
- Structured output including:
  - Meeting summary
  - Key points
  - Action items
  - Decisions made

## Project Structure

```
meetflow/
├── src/
│   ├── __init__.py
│   ├── config.py          # Configuration management
│   ├── models.py          # Data models
│   ├── gemini_client.py   # Gemini API integration
│   ├── docx_generator.py  # DOCX file generation
│   └── utils.py           # Utility functions
├── tests/
│   └── test_processor.py
├── input/                 # Place transcript files here
├── output/                # Generated minutes saved here
├── .env                   # Environment variables
├── README.md
└── main.py
```

## Installation

1. Clone or download this project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. Place your meeting transcript files (`.txt` format) in the `input/` directory
2. Run the application:
   ```bash
   python main.py
   ```
3. Generated meeting minutes will be saved in the `output/` directory as DOCX files

## Requirements

- Python 3.8+
- Google Gemini API key
