# login.py

import tkinter as tk
from tkinter import messagebox
import json

class InicioSesionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de Sesión")
        self.geometry("300x350")

        self.cargar_usuarios()

        self.etiqueta_usuario = tk.Label(self, text="Usuario:")
        self.etiqueta_usuario.pack(pady=5)
        self.entrada_usuario = tk.Entry(self)
        self.entrada_usuario.pack(pady=5)

        self.etiqueta_contrasena = tk.Label(self, text="Contraseña:")
        self.etiqueta_contrasena.pack(pady=5)
        self.entrada_contrasena = tk.Entry(self, show="*")
        self.entrada_contrasena.pack(pady=5)

        self.boton_iniciar_sesion = tk.Button(self, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_iniciar_sesion.pack(pady=10)

        self.boton_registrar = tk.Button(self, text="Registrar Usuario", command=self.abrir_ventana_registro)
        self.boton_registrar.pack(pady=5)

    def cargar_usuarios(self):
        archivo_usuarios = "usuarios.json"
        try:
            with open(archivo_usuarios, "r") as file:
                self.usuarios = json.load(file)
        except FileNotFoundError:
            self.usuarios = {}

    def iniciar_sesion(self):
        usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()

        if usuario in self.usuarios and self.usuarios[usuario] == contrasena:
            self.entrada_usuario.delete(0, tk.END)
            self.entrada_contrasena.delete(0, tk.END)
            self.ocultar()
            self.mostrar_menu()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def ocultar(self):
        self.withdraw()

    def mostrar_menu(self):
        from menu import Aplicacion
        aplicacion = Aplicacion()
        aplicacion.mainloop()
        

    def abrir_ventana_registro(self):
        ventana_registro = VentanaRegistro(self, self.usuarios)

class VentanaRegistro(tk.Toplevel):
    def __init__(self, parent, usuarios):
        super().__init__(parent)
        self.title("Registro de Usuario")
        self.geometry("400x450")

        self.usuarios = usuarios

        self.etiqueta_nombre = tk.Label(self, text="Nombre:")
        self.etiqueta_nombre.pack(pady=5)
        self.entrada_nombre = tk.Entry(self)
        self.entrada_nombre.pack(pady=5)

        self.etiqueta_apellido = tk.Label(self, text="Apellido:")
        self.etiqueta_apellido.pack(pady=5)
        self.entrada_apellido = tk.Entry(self)
        self.entrada_apellido.pack(pady=5)

        self.etiqueta_fecha_nacimiento = tk.Label(self, text="Fecha de Nacimiento:")
        self.etiqueta_fecha_nacimiento.pack(pady=5)
        self.entrada_fecha_nacimiento = tk.Entry(self)
        self.entrada_fecha_nacimiento.pack(pady=5)

        self.etiqueta_email = tk.Label(self, text="Email:")
        self.etiqueta_email.pack(pady=5)
        self.entrada_email = tk.Entry(self)
        self.entrada_email.pack(pady=5)

        self.etiqueta_usuario = tk.Label(self, text="Usuario:")
        self.etiqueta_usuario.pack(pady=5)
        self.entrada_usuario = tk.Entry(self)
        self.entrada_usuario.pack(pady=5)

        self.etiqueta_contrasena = tk.Label(self, text="Contraseña:")
        self.etiqueta_contrasena.pack(pady=5)
        self.entrada_contrasena = tk.Entry(self, show="*")
        self.entrada_contrasena.pack(pady=5)

        self.boton_registrar = tk.Button(self, text="Registrar", command=self.registrar_usuario)
        self.boton_registrar.pack(pady=10)

    def registrar_usuario(self):
        nombre = self.entrada_nombre.get()
        apellido = self.entrada_apellido.get()
        fecha_nacimiento = self.entrada_fecha_nacimiento.get()
        email = self.entrada_email.get()
        usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()

        if usuario in self.usuarios:
            messagebox.showerror("Error", "El usuario ya existe. Intente con otro usuario.")
        else:
            self.usuarios[usuario] = contrasena
            with open("usuarios.json", "w") as file:
                json.dump(self.usuarios, file)
            messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente.")
            self.destroy()
