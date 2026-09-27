# GPA CGPA Conversational Bot

This is a simple conversational bot that helps students calculate their GPA and CGPA. The bot can take user input for grades and credit hours, perform the necessary calculations, and provide the results.

## How to run it

```bash
cp .env.example .env
```

Replace `GROQ_API_KEY` with your key 

```bash
python3 -m venv .venv
source .venv/bin/activate
```

I developed this project on linux, for windows, use `.\.venv\scripts\activate` to activate the environment.

```bash
pip install -r requirements.txt
```

```bash
python3 agent.py # For Command Line
```

```bash
streamlit run app.py # For GUI part
```