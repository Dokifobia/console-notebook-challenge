# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
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

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"

    def add_note(self, title, text, importance):
        new_code = len(self.notes) + 1
        new_note = Note(new_code, title, text, importance)
        self.notes.append(new_note)
        return new_code



