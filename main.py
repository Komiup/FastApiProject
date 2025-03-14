from fastapi import FastAPI

app = FastAPI()

# Определяем маршрут (эндпоинт) по адресу "/"
@app.get("/")
async def read_root():
    return {"message": "Привет, FastAPI!"}
