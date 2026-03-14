import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "false"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
)

def summarize(data):

    prompt = f"""
Create a short AI developer briefing.

Top AI News:
{data['news']}

Important ML Papers:
{data['papers']}

Trending GitHub Repositories:
{data['repos']}

Use bullet points.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text