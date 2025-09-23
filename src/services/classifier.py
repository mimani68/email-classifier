import os
from dotenv import load_dotenv
from transformers import pipeline

from enums.classifier_types import EmailType

load_dotenv()

class ClassifierService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ClassifierService, cls).__new__(cls)
        return cls._instance

    def __init__(self): 
        self.MODEL_NAME = os.getenv("MODEL_NAME", "FacebookAI/roberta-large-mnli")
        self.classifier = pipeline("zero-shot-classification", model=self.MODEL_NAME)
        self.labels = [email_type.value for email_type in EmailType]

    def predict(self, email: str) -> EmailType:
        result = self.classifier(email, candidate_labels=self.labels, multi_label=False)
        predicted_label = result['labels'][0]
        return EmailType(predicted_label)
