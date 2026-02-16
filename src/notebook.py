# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime

class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

class Notebook:
    def __init__(self):
        self.notes = []
