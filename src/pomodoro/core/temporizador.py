from .fases import Fase, Estado


class Temporizador:
    """Lógica pura del pomodoro. No sabe nada de ventanas ni de Tkinter."""

    def __init__(self, minutos_concentracion=25, minutos_descanso=5):
        # Configuración (no cambia mientras corre)
        self.segundos_concentracion = minutos_concentracion * 60
        self.segundos_descanso = minutos_descanso * 60

        # Estado actual
        self.fase = Fase.CONCENTRACION
        self.estado = Estado.DETENIDO
        self.segundos_restantes = self.segundos_concentracion

        # Un único dato acumulado; lo demás se calcula a partir de él
        self.segundos_concentrados = 0

    # ---------- Acciones ----------
    def iniciar(self):
        self.estado = Estado.CORRIENDO

    def pausar(self):
        if self.estado == Estado.CORRIENDO:
            self.estado = Estado.PAUSADO

    def reiniciar(self):
        """Vuelve al inicio de la fase actual."""
        self.estado = Estado.DETENIDO
        self.segundos_restantes = self._duracion_de(self.fase)

    def terminar(self):
        """Salta a la siguiente fase sin esperar a que se acabe el tiempo."""
        self._cambiar_de_fase()

    def ajustar_minutos(self, minutos):
        """Suma minutos si es positivo, resta si es negativo."""
        nuevos = self.segundos_restantes + minutos * 60
        self.segundos_restantes = max(0, nuevos)

    def tick(self):
        """Avanza un segundo. Lo llamará la UI cada segundo.

        Devuelve True si en este tick terminó la fase.
        """
        if self.estado != Estado.CORRIENDO:
            return False

        self.segundos_restantes -= 1
        if self.fase == Fase.CONCENTRACION:
            self.segundos_concentrados += 1

        if self.segundos_restantes <= 0:
            self._cambiar_de_fase()
            return True
        return False

    # ---------- Auxiliares (el guion bajo indica "uso interno") ----------
    def _duracion_de(self, fase):
        if fase == Fase.CONCENTRACION:
            return self.segundos_concentracion
        return self.segundos_descanso

    def _cambiar_de_fase(self):
        if self.fase == Fase.CONCENTRACION:
            self.fase = Fase.DESCANSO
        else:
            self.fase = Fase.CONCENTRACION
        self.segundos_restantes = self._duracion_de(self.fase)
        self.estado = Estado.DETENIDO
        