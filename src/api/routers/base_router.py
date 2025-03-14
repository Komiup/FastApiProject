from fastapi import APIRouter
from src.api.schemas.schemas_1 import ResponseBase
from src.api.services.service_1 import responce_base_router

router = APIRouter()


@router.get("/", response_model=ResponseBase)
async def read_root():
    result = await responce_base_router()
    return result
