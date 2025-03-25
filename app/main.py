from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.prediction import prediction_router

app = FastAPI()

# Монтируем статические файлы
app.mount("/templates", StaticFiles(directory="app/templates"), name="templates")
app.include_router(prediction_router)
