from fastapi import APIRouter
from pydantic import BaseModel

from src.api.services.service_1 import responce_base_router

router = APIRouter()


@router.get("/", response_model=BaseModel)
async def read_root():
    result = await responce_base_router()
    return result
