import json


class Evento:
    def __init__(self, id, nombre, ingrediente, tipo, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen):
        self.id = id
        self.nombre = nombre
        self.ingrediente = ingrediente
        self.tipo = tipo
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

    @classmethod
    def cargar_eventos(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**evento) for evento in data]
