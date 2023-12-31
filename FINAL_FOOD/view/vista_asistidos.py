import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


from view.vista_principal_eventos import VistaPrincipalEventos


class VistaAsistidos(VistaPrincipalEventos):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        titulo_fuente = Font(size=13, weight="bold")
        titulo = ttk.Label(self, text="Eventos Asistidos", font=titulo_fuente,foreground='#0097e8')
        titulo.pack(padx=10, pady=5)

        self.listbox.pack(padx=10, pady=15)

        self.actualizar_eventos()

        boton_atras = ttk.Button(
            self, text="Volver", command=self.regresar
        )
        boton_atras.pack(padx=10, pady=5)