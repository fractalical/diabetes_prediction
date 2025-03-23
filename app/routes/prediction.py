from fastapi import APIRouter, Form
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import HTMLResponse
from app.services.prediction_service import prediction_service

templates = Jinja2Templates(directory="app/templates")
prediction_router = APIRouter(prefix="/prediction", tags=["prediction"])


@prediction_router.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@prediction_router.post("/", response_class=HTMLResponse)
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
    features = {
        "Pregnancies": Pregnancies,
        "PlasmaGlucose": PlasmaGlucose,
        "DiastolicBloodPressure": DiastolicBloodPressure,
        "TricepsThickness": TricepsThickness,
        "SerumInsulin": SerumInsulin,
        "BMI": BMI,
        "DiabetesPedigree": DiabetesPedigree,
        "Age": Age
    }
    print(features)
    
    prediction_result = prediction_service.predict(features)
    
    probability = prediction_result["probability"]
    has_diabetes = prediction_result["has_diabetes"]
    
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request, 
            "show_modal": True,
            "has_diabetes": has_diabetes,
            "probability": probability
        }
    )
