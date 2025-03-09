from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from app.routes.prediction import prediction_router

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.include_router(prediction_router)
