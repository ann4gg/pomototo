from enum import Enum


class Fase(Enum):
    CONCENTRACION = "concentracion"
    DESCANSO = "descanso"


class Estado(Enum):
    DETENIDO = "detenido"
    CORRIENDO = "corriendo"
    PAUSADO = "pausado"