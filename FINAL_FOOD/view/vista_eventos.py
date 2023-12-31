import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from view.vista_principal_eventos import VistaPrincipalEventos


class VistaEventos(VistaPrincipalEventos):
    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        titulo_fuente = Font(size=13, weight="bold")
        titulo = ttk.Label(self, text="Explorar eventos", font=titulo_fuente, foreground='#0097e8')
        titulo.pack(padx=10, pady=5)

        label_frame = ttk.LabelFrame(self)
        label_frame["text"] = "Mostrar"

        OPCIONES = [
            "Todos",
            "Eventos proximos",
            "Eventos finalizados"
        ]

        self.opcion_elegida = tk.IntVar(value=0)

        for index, opcion in enumerate(OPCIONES):
            ttk.Radiobutton(
                label_frame,
                text=opcion,
                value=index,
                variable=self.opcion_elegida,
                command=self.actualizar_eventos
            ).grid(row=0, column=index, padx=3, pady=3)

        label_frame.pack()

        self.listbox.pack()

        self.actualizar_eventos()

        boton_atras = ttk.Button(self, text="Volver", command=self.regresar)
        boton_atras.pack(padx=10, pady=5)

    def _determinar_eventos(self):
        opcion = self.opcion_elegida.get()
        match opcion:
            case 1:
                return self.obtener_eventos_proximos()
            case 2:
                return self.obtener_eventos_finalizados()
            case _:
                return self.obtener_eventos()

    def actualizar_eventos(self):
        eventos = self._determinar_eventos()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)

    def seleccionar_evento(self, event):
        indice = self.obtener_evento_seleccionado()
        eventos = self._determinar_eventos()
        self.controlador.seleccionar_evento(indice, eventos)
