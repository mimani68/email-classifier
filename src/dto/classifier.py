from pydantic import BaseModel, Field

from enums.classifier_types import EmailType

class ClassificationResponse(BaseModel):
    label: EmailType = Field(..., description="Unique values which show the right label for each email body")

class ClassificationRequest(BaseModel):
    email: str = Field(..., description="Message body")
