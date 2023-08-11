import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class VistaInicio(ttk.Frame):

    def __init__(self, master=None, controlador=None):

        super().__init__(master)
        
        self.master = master
        self.controlador = controlador

        fuente_titulo = Font(size=16, weight="bold")
        titulo = ttk.Label(self, text="Bienvenido a Foodie Travel", font=fuente_titulo, foreground='#0097e8')
        titulo.pack(padx=10, pady=15)

        fuente_descripcion = Font(size=12)
        descripcion = ttk.Label(self, text=" Explora el mundo a través del sabor con Foodie Travel: Encuentra, Saborea, Descubre.!", font=fuente_descripcion, wraplength=250, foreground='#df00dd')
        descripcion.pack(padx=10, pady=15)

        frame_botones = ttk.Frame(self)

        boton_explorar = ttk.Button(frame_botones, text="Explorar destinos", command=self.mostrar_destinos)
        boton_explorar.grid(row=0, column=0, pady=5)

        boton_buscar = ttk.Button(frame_botones, text="Buscar destinos", command=self.buscar_destinos)
        boton_buscar.grid(row=1, column=0, pady=5)

        boton_asistidos = ttk.Button(frame_botones, text="Destinos visitados", command=self.destinos_visitados)
        boton_asistidos.grid(row=2, column=0, pady=5)

        frame_botones.pack(padx=10, pady=15)

    def mostrar_destinos(self):
        self.controlador.mostrar_destinos()

    def buscar_destinos(self):
        self.controlador.buscar_destinos()

    def destinos_visitados(self):
        self.controlador.destinos_visitados()