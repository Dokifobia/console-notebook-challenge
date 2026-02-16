from datetime import datetime

class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

class Notebook:
    def __init__(self):
        self.notes = []

    def __init__(self, code, title, text, importance):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()
        self.tags = []

