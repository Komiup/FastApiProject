from src.api.schemas.schemas_1 import ResponseBase

async def responce_base_router():
    return ResponseBase(message="Hello World")