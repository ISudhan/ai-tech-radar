import requests

URL = "https://api.github.com/search/repositories?q=artificial+intelligence&sort=stars&order=desc&per_page=10"


def get_repositories():

    response = requests.get(URL, timeout=10)

    data = response.json()

    repos = []

    for repo in data["items"]:

        repos.append({
            "name": repo["full_name"],
            "url": repo["html_url"],
            "description": repo["description"],
            "language": repo["language"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"]
        })

    return repos
