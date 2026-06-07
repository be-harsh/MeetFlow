# MeetFlow 🗒️→📄 

**Turn messy meeting notes into professional Word reports instantly using Google Gemini AI.** 

No more spending 30 minutes writing meeting summaries. Paste your raw transcript, run one command, get a clean structured Word document. 

--- 

## What It Does 

MeetFlow reads a messy meeting transcript from a text file, sends it to Google Gemini AI, and generates a professional Word document report containing: 

- Meeting summary 
- Key points discussed 
- Action items table with owner, deadline, and priority 
- Risk register with severity levels 
- Decisions made 

## Project Structure 
```
meetflow/ 
├── src/ 
│   ├── __init__.py          # Package initialization 
│   ├── config.py            # API config and file paths 
│   ├── models.py            # Dataclasses for structured data 
│   ├── gemini_client.py     # Gemini API integration 
│   ├── docx_generator.py    # Word document generator 
│   └── utils.py             # File handling helpers 
├── tests/ 
│   └── test_processor.py    # Pytest test suite 
├── input/                   # Place your .txt transcript here 
├── output/                  # Generated Word reports saved here 
├── .env                     # Your Gemini API key goes here 
├── requirements.txt 
└── main.py                  # Run this 
```

## Installation 

1. Clone or download this project 
2. Install dependencies: 
```bash 
pip install -r requirements.txt 
```

3. Create a `.env` file in the project root and add your Gemini API key: 
```
GEMINI_API_KEY=your_api_key_here 
```

## Usage 

1. Add your meeting transcript as a `.txt` file inside the `input/` folder 
2. Run the tool: 
```bash 
python main.py 
```
3. Open your generated report from the `output/` folder 

## Example Input 
```
Team meeting 5th June. 
John will prepare the pitch deck by Friday. 
Sarah flagged that the API integration might delay launch. 
We decided to push the release date to July 15th. 
Budget approval still pending from management. 
```

## Example Output 

A professional Word document with structured tables for action items and risks, bullet points for key decisions, and a clean summary section. 

## Tech Stack 

- Python 3.8+ 
- Google Gemini API (gemini-2.5-flash) 
- python-docx 
- requests 
- python-dotenv 

## Requirements 

Get a free Gemini API key from `https://aistudio.google.com`
