from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse

from dto.classifier import ClassificationRequest, ClassificationResponse
from services.classifier import classifierService

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to Cycle Prediction API"}

@router.get("/liveness", summary="Liveness check", description="Checks if the service is running.")
async def liveness():
    return JSONResponse(content={"status": "ok"})

@router.post("/predict", response_model=ClassificationResponse)
async def predict(input_data: ClassificationRequest):
    try:
        prediction = classifierService(input_data.email)
        return ClassificationResponse(label=prediction['label'])
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    