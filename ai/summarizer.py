import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "false"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
)

def summarize(data):
    try:
        prompt = f"""Summarize the following AI tech updates into a concise radar report:

News:
{data['news']}

Papers:
{data['papers']}

Repos:
{data['repos']}
"""
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception:
        return f"""
AI Tech Radar

News:
{data['news']}

Papers:
{data['papers']}

Repos:
{data['repos']}
"""