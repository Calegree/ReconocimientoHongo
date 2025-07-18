from fastapi import FastAPI
from src.routers import images

app = FastAPI()
app.include_router(images.router)