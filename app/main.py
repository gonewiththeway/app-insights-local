from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(
    title="Insights App",
    description="An API to fetch user repositories and get insights about specific repositories.",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "url": "https://yourwebsite.com",
        "email": "yourname@example.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Include the endpoints from the endpoints module
app.include_router(endpoints.router, prefix="/api", tags=["Repositories"])
