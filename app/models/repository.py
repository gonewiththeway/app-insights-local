from pydantic import BaseModel
from typing import List

class RepoItem(BaseModel):
    title: str
    value: str

class UserRepos(BaseModel):
    user: List[RepoItem]
