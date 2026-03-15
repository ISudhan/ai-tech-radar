import requests
import xml.etree.ElementTree as ET

CATEGORIES = [
    "cs.AI",
    "cs.LG",
    "cs.CL",
    "stat.ML"
]


def get_papers():

    papers = []

    for cat in CATEGORIES:

        url = f"http://export.arxiv.org/api/query?search_query=cat:{cat}&start=0&max_results=5"

        r = requests.get(url, timeout=10)

        root = ET.fromstring(r.text)

        ns = {"atom": "http://www.w3.org/2005/Atom"}

        for entry in root.findall("atom:entry", ns):

            title = entry.find("atom:title", ns).text.strip()
            link = entry.find("atom:id", ns).text
            published = entry.find("atom:published", ns).text

            papers.append({
                "title": title,
                "url": link,
                "published": published,
                "category": cat
            })

    # remove duplicates
    unique = {p["url"]: p for p in papers}

    return list(unique.values())