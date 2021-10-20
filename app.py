from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="REST API with FastAPI and MongoDB",
    description="Rest API using fastAPI and MongoDB",
    version="0.0.1"
)

app.include_router(user)
