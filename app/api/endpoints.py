from fastapi import APIRouter
from typing import List, Dict

router = APIRouter()

# Mock data
repositories = {
    "user1": ["repo1", "repo2", "repo3"],
    "user2": ["repoA", "repoB"],
    "user3": ["repoX", "repoY", "repoZ"]
}

insights = {
    "repo1": {"stars": 10, "forks": 2, "issues": 5},
    "repo2": {"stars": 20, "forks": 4, "issues": 1},
    "repo3": {"stars": 5, "forks": 1, "issues": 0},
    "repoA": {"stars": 7, "forks": 3, "issues": 2},
    "repoB": {"stars": 15, "forks": 5, "issues": 3},
    "repoX": {"stars": 30, "forks": 10, "issues": 7},
    "repoY": {"stars": 25, "forks": 8, "issues": 6},
    "repoZ": {"stars": 18, "forks": 6, "issues": 4},
}

@router.get("/repositories", response_model=List[str])
def get_repositories(userid: str):
    return repositories.get(userid, [])

@router.get("/insights", response_model=Dict[str, int])
def get_insights(userid: str, repo: str):
    if repo in repositories.get(userid, []):
        return insights.get(repo, {})
    return {}
