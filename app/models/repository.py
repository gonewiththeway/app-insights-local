from pydantic import BaseModel, RootModel
from typing import List, Dict

class RepoItem(BaseModel):
    repo: str

class UserRepos(RootModel):
    root: Dict[str, List[RepoItem]]
