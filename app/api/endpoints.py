from fastapi import APIRouter, HTTPException
from typing import List, Dict

router = APIRouter()

# Mock data
repositories = {
    "user1": [{"repo": "repo1"}, {"repo": "repo2"}, {"repo": "repo3"}],
    "user2": [{"repo": "repoA"}, {"repo": "repoB"}],
    "user3": [{"repo": "repoX"}, {"repo": "repoY"}, {"repo": "repoZ"}]
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

@router.get("/repositories", response_model=List[str], summary="Get Repositories", description="Retrieve a list of repositories for a given user.")
def get_repositories(userid: str):
    """
    Fetches a list of repositories for the specified user.
    - **userid**: The ID of the user.
    """
    if userid not in repositories:
        raise HTTPException(status_code=404, detail="User not found")
    return repositories.get(userid, [])

@router.get("/insights", response_model=Dict[str, int], summary="Get Repository Insights", description="Retrieve insights about a specific repository for a given user.")
def get_insights(userid: str, repo: str):
    """
    Fetches insights for a specific repository.
    - **userid**: The ID of the user.
    - **repo**: The name of the repository.
    """
    if userid not in repositories or repo not in repositories[userid]:
        raise HTTPException(status_code=404, detail="Repository not found for the user")
    return insights.get(repo, {})
