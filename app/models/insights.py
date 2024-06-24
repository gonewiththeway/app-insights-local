from pydantic import BaseModel

class Insight(BaseModel):
    title: str
    value: str

class InsightsResponse(BaseModel):
    title: str
    subtitle: str
    insights1: Insight
    insights2: Insight
    insights3: Insight
