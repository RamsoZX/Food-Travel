class ControladorInicio:
    def __init__(self, app):
        self.app = app

    def mostrar_destinos(self):
        self.app.cambiar_frame(self.app.vista_destinos)

    def buscar_destinos(self):
        self.app.cambiar_frame(self.app.vista_busqueda)

    def destinos_visitados(self):
        self.app.cambiar_frame(self.app.vista_asistidos)