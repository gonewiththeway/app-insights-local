from fastapi import FastAPI
from app.api import endpoints

app = FastAPI()

# Include the endpoints from the endpoints module
app.include_router(endpoints.router)
