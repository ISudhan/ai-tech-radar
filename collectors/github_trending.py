import requests

def get_repos():

    url = "https://api.github.com/search/repositories"

    params = {
        "q": "machine learning",
        "sort": "stars",
        "order": "desc",
        "per_page": 5
    }

    response = requests.get(url, params=params)
    data = response.json()

    repos = []

    for repo in data["items"]:
        repos.append(repo["full_name"])

    return repos