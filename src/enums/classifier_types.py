from enum import Enum

class EmailType(Enum):
    SUPPORT = "SUPPORT"
    INQUIRIES = "INQUIRIES"
    SUPPLIERS = "SUPPLIERS"
    SPAM = "SPAM"