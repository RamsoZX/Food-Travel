import tkinter as tk
from tkinter import ttk



class VistaPrincipalDestinos(ttk.Frame):
    def __init__(self, master=None, controlador=None):

        super().__init__(master)

        self.master = master
        self.controlador = controlador

        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)
        self.listbox.bind("<Double-Button-1>", self.seleccionar_evento)

    def actualizar_eventos(self):
        eventos = self.obtener_eventos()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)

    def obtener_evento_seleccionado(self):
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def seleccionar_evento(self, event):
        indice = self.obtener_evento_seleccionado()
        self.controlador.seleccionar_evento(indice)

    def obtener_eventos(self):
        return self.controlador.obtener_eventos()

    def obtener_eventos_proximos(self):
        return self.controlador.obtener_eventos_proximos()

    def obtener_eventos_finalizados(self):
        return self.controlador.obtener_eventos_finalizados()
    
    def regresar(self):
        self.controlador.regresar()