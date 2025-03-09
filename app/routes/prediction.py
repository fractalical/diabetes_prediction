from fastapi import APIRouter, Form
from starlette.requests import Request
from starlette.responses import HTMLResponse

from app.main import templates

prediction_router = APIRouter(prefix="/prediction", tags=["prediction"])


@prediction_router.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@prediction_router.post("/")
async def make_prediction(
    request: Request,
    Pregnancies: int = Form(...),
    PlasmaGlucose: float = Form(...),
    DiastolicBloodPressure: float = Form(...),
    TricepsThickness: float = Form(...),
    SerumInsulin: float = Form(...),
    BMI: float = Form(...),
    DiabetesPedigree: float = Form(...),
    Age: int = Form(...)
):
    result = "12%"
    message = f'Your diabetes prediction: {result}'
    return templates.TemplateResponse("result.html", {"request": request, "message": message})
