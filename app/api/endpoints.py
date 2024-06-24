from fastapi import APIRouter, HTTPException
from typing import List, Dict
from app.models.repository import RepoItem, UserRepos
from app.models.insights import Insight, InsightsResponse

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

@router.get("/repositories", response_model=UserRepos, summary="Get Repositories", description="Retrieve a list of repositories for a given user.")
def get_repositories(userid: str):
    if userid not in repositories:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Transform the list of repository names into the desired format
    repo_list = [{"title": repo, "value": repo} for repo in repositories[userid]]
    
    return {"user": repo_list}

@router.get("/insights", response_model=Dict[str, int], summary="Get Repository Insights", description="Retrieve insights about a specific repository for a given user.")
def get_insights(userid: str, repo: str):
    if userid not in repositories or repo not in repositories[userid]:
        raise HTTPException(status_code=404, detail="Repository not found for the user")
    return insights.get(repo, {})

@router.get("/user-insights", response_model=InsightsResponse, summary="Get User Insights", description="Retrieve insights for a user.")
def get_user_insights():
    return InsightsResponse(
        title="Clara King",
        subtitle="exceeds tech team · Tenure: 1.8 years · Last rating Meet All · Last Promo May 2024",
        insights1=Insight(title="5566", value="Adaptive Cards"),
        insights2=Insight(title="60%", value="Bug Fix Rate"),
        insights3=Insight(title="8 min", value="Response Time")
    )
