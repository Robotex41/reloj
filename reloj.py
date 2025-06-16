import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# 🎨 Colores y fuente
COLOR_FONDO = "#2E3440"         # gris azulado oscuro (Nord Theme)
COLOR_TEXTO = "#ECEFF4"         # blanco suave
COLOR_SECUNDARIO = "#4C566A"    # gris medio
FUENTE_RELOJ = ("Helvetica", 36, "bold")
FUENTE_MENU = ("Segoe UI", 10)

# Función para actualizar la hora
def actualizar_hora():
    ahora = datetime.now().strftime("%H:%M:%S")
    etiqueta_hora.config(text=ahora)
    root.after(1000, actualizar_hora)

# Funciones del menú
import random
def pasos():
    pasos_hoy = random.randint(3000, 9000)
    messagebox.showinfo("Pasos", f"Hoy caminaste {pasos_hoy} pasos 🏃‍♂️")


import random
def ritmo_cardiaco():
    ritmo = random.randint(60, 110)
    if ritmo < 70:
        estado = "Reposo 🧘"
    elif ritmo < 90:
        estado = "Normal 🚶"
    else:
        estado = "Elevado 🏃‍♂️"
    messagebox.showinfo("Ritmo cardíaco", f"{ritmo} bpm - {estado}")


def configurar_alarma():
    ventana_alarma = tk.Toplevel(root)
    ventana_alarma.title("Configurar Alarma")
    ventana_alarma.configure(bg=COLOR_FONDO)

    tk.Label(ventana_alarma, text="Hora:", fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=0, column=0)
    spin_hora = tk.Spinbox(ventana_alarma, from_=0, to=23, width=5)
    spin_hora.grid(row=0, column=1)

    tk.Label(ventana_alarma, text="Minuto:", fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=1, column=0)
    spin_minuto = tk.Spinbox(ventana_alarma, from_=0, to=59, width=5)
    spin_minuto.grid(row=1, column=1)

    def guardar_alarma():
        hora = spin_hora.get()
        minuto = spin_minuto.get()
        global alarma_hora
        alarma_hora = f"{int(hora):02}:{int(minuto):02}"
        messagebox.showinfo("Alarma", f"Alarma guardada para {alarma_hora}")
        ventana_alarma.destroy()

    btn_guardar = tk.Button(ventana_alarma, text="Guardar", command=guardar_alarma)
    btn_guardar.grid(row=2, columnspan=2, pady=10)

def cambiar_idioma():
    messagebox.showinfo("Ajustes", "Idioma cambiado a Español 🇪🇸")

def ajustar_brillo():
    messagebox.showinfo("Ajustes", "Brillo ajustado al 80% 💡")

def salir():
    root.quit()

# 🪟 Ventana principal
root = tk.Tk()
root.title("Reloj Inteligente")
root.geometry("400x300")
root.configure(bg=COLOR_FONDO)

# 🕒 Etiqueta de la hora
etiqueta_hora = tk.Label(
    root,
    text="",
    font=FUENTE_RELOJ,
    fg=COLOR_TEXTO,
    bg=COLOR_FONDO,
    pady=30
)
etiqueta_hora.pack()

# 🌐 Barra de menú
barra_menu = tk.Menu(root, font=FUENTE_MENU, bg=COLOR_SECUNDARIO, fg=COLOR_TEXTO, tearoff=0)

# Menú Salud
menu_salud = tk.Menu(barra_menu, tearoff=0, bg=COLOR_SECUNDARIO, fg=COLOR_TEXTO, font=FUENTE_MENU)
menu_salud.add_command(label="Pasos", command=pasos)
menu_salud.add_command(label="Ritmo cardíaco", command=ritmo_cardiaco)
barra_menu.add_cascade(label="Salud", menu=menu_salud)

# Menú Alarma
menu_alarma = tk.Menu(barra_menu, tearoff=0, bg=COLOR_SECUNDARIO, fg=COLOR_TEXTO, font=FUENTE_MENU)
menu_alarma.add_command(label="Configurar alarma", command=configurar_alarma)
barra_menu.add_cascade(label="Alarma", menu=menu_alarma)

# Menú Ajustes
menu_ajustes = tk.Menu(barra_menu, tearoff=0, bg=COLOR_SECUNDARIO, fg=COLOR_TEXTO, font=FUENTE_MENU)
menu_ajustes.add_command(label="Cambiar idioma", command=cambiar_idioma)
menu_ajustes.add_command(label="Ajustar brillo", command=ajustar_brillo)
barra_menu.add_cascade(label="Ajustes", menu=menu_ajustes)

# Salir
barra_menu.add_command(label="Salir", command=salir)

# Configurar menú en ventana
root.config(menu=barra_menu)

# Iniciar reloj
actualizar_hora()

# Ejecutar aplicación
root.mainloop()
