from fastapi import FastAPI
from src.api.routers import base_router
app = FastAPI()

app.include_router(base_router.router)

