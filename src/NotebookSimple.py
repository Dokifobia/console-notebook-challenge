from datetime import datetime

class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

class Notebook:
    def __init__(self):
        self.notes = []
