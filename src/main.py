from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.classifier import router

app = FastAPI(
    title="Email classifier",
    description="API for cycle classification using machine learning",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
