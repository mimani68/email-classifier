from enums.classifier_types import EmailType


def classifierService(email: str):
    return {
        "label": EmailType.SPAM
    }