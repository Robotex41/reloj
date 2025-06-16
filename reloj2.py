import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import calendar
import random

# 🎨 Configuración de colores y fuentes
COLOR_FONDO = "#2E3440"         # Color de fondo principal
COLOR_TEXTO = "#ECEFF4"         # Color de texto claro
COLOR_BOTON = "#5E81AC"         # Color para botones
COLOR_DIA_ACTUAL = "#88C0D0"    # Color para resaltar el día actual
FUENTE_RELOJ = ("Helvetica", 36, "bold")  # Fuente para el reloj
FUENTE_NORMAL = ("Segoe UI", 10)          # Fuente normal

# Variables globales
idioma_actual = "español"       # Idioma inicial
brillo_actual = 80              # Nivel de brillo inicial (80%)
alarma_activa = None            # Alarma configurada
recordatorios = []              # Lista para almacenar recordatorios

# Textos traducidos
textos = {
    "español": {
        "titulo": "Reloj Inteligente",
        "salud": "Salud",
        "pasos": "Pasos",
        "ritmo": "Ritmo cardíaco",
        "alarma": "Alarma",
        "config_alarma": "Configurar alarma",
        "ajustes": "Ajustes",
        "idioma": "Idioma",
        "brillo": "Brillo",
        "recordatorios": "Recordatorios",
        "agregar_rec": "Agregar recordatorio",
        "ver_rec": "Ver recordatorios",
        "calendario": "Calendario",
        "salir": "Salir",
        "hora": "Hora:",
        "minuto": "Minuto:",
        "periodo": "AM/PM:",
        "guardar": "Guardar",
        "alarma_guardada": "Alarma guardada para",
        "brillo_ajustado": "Brillo ajustado a",
        "recordatorio": "Recordatorio",
        "texto_rec": "Texto:",
        "fecha_rec": "Fecha:",
        "hora_rec": "Hora:",
        "agregar": "Agregar",
        "eliminar": "Eliminar",
        "modificar": "Modificar",
        "sin_recordatorios": "No hay recordatorios",
        "dia": ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
        "mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
               "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        "seleccion_idioma": "Seleccionar Idioma",
        "español": "Español",
        "inglés": "Inglés",
        "agregar_a_fecha": "Agregar recordatorio para",
        "porcentaje": "%",
        "config_brillo": "Configurar Brillo",
        "am": "AM",
        "pm": "PM"
    },
    "inglés": {
        "titulo": "Smart Watch",
        "salud": "Health",
        "pasos": "Steps",
        "ritmo": "Heart rate",
        "alarma": "Alarm",
        "config_alarma": "Set alarm",
        "ajustes": "Settings",
        "idioma": "Language",
        "brillo": "Brightness",
        "recordatorios": "Reminders",
        "agregar_rec": "Add reminder",
        "ver_rec": "View reminders",
        "calendario": "Calendar",
        "salir": "Exit",
        "hora": "Hour:",
        "minuto": "Minute:",
        "periodo": "AM/PM:",
        "guardar": "Save",
        "alarma_guardada": "Alarm set for",
        "brillo_ajustado": "Brightness adjusted to",
        "recordatorio": "Reminder",
        "texto_rec": "Text:",
        "fecha_rec": "Date:",
        "hora_rec": "Time:",
        "agregar": "Add",
        "eliminar": "Delete",
        "modificar": "Edit",
        "sin_recordatorios": "No reminders",
        "dia": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "mes": ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"],
        "seleccion_idioma": "Select Language",
        "español": "Spanish",
        "inglés": "English",
        "agregar_a_fecha": "Add reminder for",
        "porcentaje": "%",
        "config_brillo": "Configure Brightness",
        "am": "AM",
        "pm": "PM"
    }
}

def obtener_texto(clave):
    """Obtiene el texto traducido según el idioma actual"""
    return textos[idioma_actual][clave]

def actualizar_interfaz():
    """Actualiza todos los textos de la interfaz al cambiar de idioma"""
    root.title(obtener_texto("titulo"))
    # Actualizar textos del menú
    menu_salud.entryconfig(0, label=obtener_texto("pasos"))
    menu_salud.entryconfig(1, label=obtener_texto("ritmo"))
    barra_menu.entryconfig(1, label=obtener_texto("alarma"))
    menu_alarma.entryconfig(0, label=obtener_texto("config_alarma"))
    barra_menu.entryconfig(2, label=obtener_texto("ajustes"))
    menu_ajustes.entryconfig(0, label=obtener_texto("idioma"))
    menu_ajustes.entryconfig(1, label=obtener_texto("brillo"))
    barra_menu.entryconfig(3, label=obtener_texto("recordatorios"))
    menu_recordatorios.entryconfig(0, label=obtener_texto("agregar_rec"))
    menu_recordatorios.entryconfig(1, label=obtener_texto("ver_rec"))
    barra_menu.entryconfig(4, label=obtener_texto("calendario"))
    barra_menu.entryconfig(5, label=obtener_texto("salir"))

# Función para actualizar la hora y fecha
def actualizar_tiempo():
    ahora = datetime.now()
    etiqueta_hora.config(text=ahora.strftime("%H:%M:%S"))
    etiqueta_fecha.config(text=ahora.strftime("%d/%m/%Y"))
    
    # Verificar si la alarma debe sonar
    if alarma_activa:
        hora_actual = ahora.strftime("%I:%M %p").lower()
        if hora_actual == alarma_activa.lower():
            messagebox.showinfo("Alarma", "¡Es hora de despertar! ⏰")
    
    root.after(1000, actualizar_tiempo)

# Funciones de salud (simuladas)
def mostrar_pasos():
    pasos = random.randint(3000, 9000)
    messagebox.showinfo(obtener_texto("pasos"), f"{pasos} {obtener_texto('pasos').lower()}")

def mostrar_ritmo_cardiaco():
    ritmo = random.randint(60, 110)
    estado = "Normal"
    if ritmo < 70:
        estado = "Reposo" if idioma_actual == "español" else "Resting"
    elif ritmo > 90:
        estado = "Elevado" if idioma_actual == "español" else "High"
    messagebox.showinfo(obtener_texto("ritmo"), f"{ritmo} bpm - {estado}")

# Funciones de alarma
def configurar_alarma():
    ventana_alarma = tk.Toplevel(root)
    ventana_alarma.title(obtener_texto("config_alarma"))
    ventana_alarma.configure(bg=COLOR_FONDO)

    # Hora (1-12)
    tk.Label(ventana_alarma, text=obtener_texto("hora"), fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=0, column=0)
    spin_hora = tk.Spinbox(ventana_alarma, from_=1, to=12, width=5)
    spin_hora.grid(row=0, column=1)

    # Minutos (0-59)
    tk.Label(ventana_alarma, text=obtener_texto("minuto"), fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=1, column=0)
    spin_minuto = tk.Spinbox(ventana_alarma, from_=0, to=59, width=5, format="%02.0f")
    spin_minuto.grid(row=1, column=1)

    # AM/PM
    tk.Label(ventana_alarma, text=obtener_texto("periodo"), fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=2, column=0)
    var_periodo = tk.StringVar(value=obtener_texto("am"))
    opciones_periodo = [obtener_texto("am"), obtener_texto("pm")]
    menu_periodo = tk.OptionMenu(ventana_alarma, var_periodo, *opciones_periodo)
    menu_periodo.config(bg=COLOR_FONDO, fg=COLOR_TEXTO, highlightthickness=0)
    menu_periodo.grid(row=2, column=1)

    def guardar_alarma():
        global alarma_activa
        hora = spin_hora.get()
        minuto = spin_minuto.get()
        periodo = var_periodo.get()
        
        alarma_activa = f"{int(hora):02}:{int(minuto):02} {periodo}"
        messagebox.showinfo("Alarma", f"{obtener_texto('alarma_guardada')} {alarma_activa}")
        ventana_alarma.destroy()

    btn_guardar = tk.Button(ventana_alarma, text=obtener_texto("guardar"), command=guardar_alarma)
    btn_guardar.grid(row=3, columnspan=2, pady=10)

# Funciones de calendario
def mostrar_calendario_completo():
    ventana_cal = tk.Toplevel(root)
    ventana_cal.title(obtener_texto("calendario"))
    ventana_cal.configure(bg=COLOR_FONDO)
    
    notebook = ttk.Notebook(ventana_cal)
    notebook.pack(pady=10, padx=10, fill="both", expand=True)
    
    año_actual = datetime.now().year
    dia_actual = datetime.now().day
    mes_actual = datetime.now().month
    
    for mes in range(1, 13):
        frame_mes = tk.Frame(notebook, bg=COLOR_FONDO)
        notebook.add(frame_mes, text=obtener_texto("mes")[mes-1])
        
        cal = calendar.monthcalendar(año_actual, mes)
        
        # Encabezado con días de la semana
        for i, dia in enumerate(obtener_texto("dia")):
            tk.Label(frame_mes, text=dia[:3], font=FUENTE_NORMAL, 
                    fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=0, column=i, padx=5)
        
        # Días del mes
        for semana_num, semana in enumerate(cal):
            for dia_num, dia in enumerate(semana):
                if dia != 0:
                    bg_color = COLOR_DIA_ACTUAL if (dia == dia_actual and mes == mes_actual) else COLOR_FONDO
                    
                    btn_dia = tk.Button(frame_mes, text=str(dia), width=4, 
                                      bg=bg_color, fg=COLOR_TEXTO,
                                      command=lambda d=dia, m=mes: agregar_rec_desde_calendario(d, m, año_actual))
                    btn_dia.grid(row=semana_num+1, column=dia_num, pady=2)

def agregar_rec_desde_calendario(dia, mes, año):
    """Abre la ventana para agregar recordatorio con la fecha seleccionada"""
    fecha_seleccionada = f"{dia:02d}/{mes:02d}/{año}"
    ventana_rec = tk.Toplevel(root)
    ventana_rec.title(f"{obtener_texto('agregar_a_fecha')} {fecha_seleccionada}")
    ventana_rec.configure(bg=COLOR_FONDO)

    tk.Label(ventana_rec, text=obtener_texto("texto_rec"), fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=0, column=0)
    entry_texto = tk.Entry(ventana_rec, width=30)
    entry_texto.grid(row=0, column=1)

    tk.Label(ventana_rec, text=obtener_texto("fecha_rec"), fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=1, column=0)
    entry_fecha = tk.Entry(ventana_rec, width=10)
    entry_fecha.insert(0, fecha_seleccionada)
    entry_fecha.grid(row=1, column=1)

    tk.Label(ventana_rec, text=obtener_texto("hora_rec"), fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=2, column=0)
    entry_hora = tk.Entry(ventana_rec, width=10)
    entry_hora.insert(0, datetime.now().strftime("%H:%M"))
    entry_hora.grid(row=2, column=1)

    def guardar_recordatorio():
        texto = entry_texto.get()
        fecha = entry_fecha.get()
        hora = entry_hora.get()
        
        if texto and fecha and hora:
            recordatorios.append({
                "texto": texto,
                "fecha": fecha,
                "hora": hora
            })
            messagebox.showinfo(obtener_texto("recordatorio"), obtener_texto("recordatorio") + " agregado!")
            ventana_rec.destroy()
            ver_recordatorios()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos")

    tk.Button(ventana_rec, text=obtener_texto("agregar"), command=guardar_recordatorio).grid(row=3, columnspan=2, pady=10)

# Funciones de recordatorios
def ver_recordatorios():
    ventana_rec = tk.Toplevel(root)
    ventana_rec.title(obtener_texto("recordatorios"))
    ventana_rec.configure(bg=COLOR_FONDO)
    
    if not recordatorios:
        tk.Label(ventana_rec, text=obtener_texto("sin_recordatorios"), 
                fg=COLOR_TEXTO, bg=COLOR_FONDO).pack()
        return
    
    frame = tk.Frame(ventana_rec, bg=COLOR_FONDO)
    frame.pack(fill=tk.BOTH, expand=True)
    
    canvas = tk.Canvas(frame, bg=COLOR_FONDO, highlightthickness=0)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=COLOR_FONDO)
    
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    for i, rec in enumerate(recordatorios):
        tk.Label(scrollable_frame, 
                text=f"{rec['fecha']} {rec['hora']}: {rec['texto']}",
                fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=i, column=0, sticky="w")
        
        btn_frame = tk.Frame(scrollable_frame, bg=COLOR_FONDO)
        btn_frame.grid(row=i, column=1, padx=5)
        
        tk.Button(btn_frame, text=obtener_texto("modificar"), 
                command=lambda r=rec: modificar_recordatorio(r)).pack(side=tk.LEFT)
        tk.Button(btn_frame, text=obtener_texto("eliminar"), 
                command=lambda r=rec: eliminar_recordatorio(r)).pack(side=tk.LEFT)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def modificar_recordatorio(recordatorio):
    ventana_rec = tk.Toplevel(root)
    ventana_rec.title(obtener_texto("modificar"))
    ventana_rec.configure(bg=COLOR_FONDO)

    tk.Label(ventana_rec, text=obtener_texto("texto_rec"), fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=0, column=0)
    entry_texto = tk.Entry(ventana_rec, width=30)
    entry_texto.insert(0, recordatorio["texto"])
    entry_texto.grid(row=0, column=1)

    tk.Label(ventana_rec, text=obtener_texto("fecha_rec"), fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=1, column=0)
    entry_fecha = tk.Entry(ventana_rec, width=10)
    entry_fecha.insert(0, recordatorio["fecha"])
    entry_fecha.grid(row=1, column=1)

    tk.Label(ventana_rec, text=obtener_texto("hora_rec"), fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=2, column=0)
    entry_hora = tk.Entry(ventana_rec, width=10)
    entry_hora.insert(0, recordatorio["hora"])
    entry_hora.grid(row=2, column=1)

    def actualizar_recordatorio():
        recordatorio["texto"] = entry_texto.get()
        recordatorio["fecha"] = entry_fecha.get()
        recordatorio["hora"] = entry_hora.get()
        messagebox.showinfo(obtener_texto("recordatorio"), obtener_texto("recordatorio") + " actualizado!")
        ventana_rec.destroy()
        ver_recordatorios()

    tk.Button(ventana_rec, text=obtener_texto("guardar"), command=actualizar_recordatorio).grid(row=3, columnspan=2, pady=10)

def eliminar_recordatorio(recordatorio):
    confirmacion = messagebox.askyesno("Confirmar", "¿Eliminar este recordatorio?")
    if confirmacion:
        recordatorios.remove(recordatorio)
        ver_recordatorios()

# Funciones de ajustes
def cambiar_idioma(nuevo_idioma):
    global idioma_actual
    idioma_actual = nuevo_idioma
    actualizar_interfaz()
    messagebox.showinfo(obtener_texto("ajustes"), f"Idioma cambiado a {obtener_texto(idioma_actual)}")

def mostrar_selector_idioma():
    ventana_idioma = tk.Toplevel(root)
    ventana_idioma.title(obtener_texto("seleccion_idioma"))
    ventana_idioma.configure(bg=COLOR_FONDO)
    
    tk.Label(ventana_idioma, text=obtener_texto("seleccion_idioma"),
            fg=COLOR_TEXTO, bg=COLOR_FONDO).pack(pady=10)
    
    frame_botones = tk.Frame(ventana_idioma, bg=COLOR_FONDO)
    frame_botones.pack()
    
    tk.Button(frame_botones, text="Español", 
             command=lambda: cambiar_idioma("español")).pack(side=tk.LEFT, padx=10)
    tk.Button(frame_botones, text="English", 
             command=lambda: cambiar_idioma("inglés")).pack(side=tk.LEFT, padx=10)

def ajustar_brillo():
    ventana_brillo = tk.Toplevel(root)
    ventana_brillo.title(obtener_texto("config_brillo"))
    ventana_brillo.configure(bg=COLOR_FONDO)
    
    tk.Label(ventana_brillo, text=f"{obtener_texto('brillo')}: {brillo_actual}{obtener_texto('porcentaje')}", 
             fg=COLOR_TEXTO, bg=COLOR_FONDO).pack(pady=10)
    
    escala = tk.Scale(ventana_brillo, from_=10, to=100, orient=tk.HORIZONTAL,
                     length=200, bg=COLOR_FONDO, fg=COLOR_TEXTO,
                     highlightthickness=0)
    escala.set(brillo_actual)
    escala.pack()
    
    def guardar_brillo():
        global brillo_actual
        brillo_actual = escala.get()
        ventana_brillo.destroy()
        messagebox.showinfo(obtener_texto("ajustes"), 
                          f"{obtener_texto('brillo_ajustado')} {brillo_actual}{obtener_texto('porcentaje')}")
    
    tk.Button(ventana_brillo, text=obtener_texto("guardar"), command=guardar_brillo).pack(pady=10)

# Configuración de la ventana principal
root = tk.Tk()
root.title(obtener_texto("titulo"))
root.geometry("400x300")
root.configure(bg=COLOR_FONDO)

# Etiquetas de hora y fecha
etiqueta_hora = tk.Label(root, text="", font=FUENTE_RELOJ, fg=COLOR_TEXTO, bg=COLOR_FONDO, pady=10)
etiqueta_hora.pack()
etiqueta_fecha = tk.Label(root, text="", font=FUENTE_NORMAL, fg=COLOR_TEXTO, bg=COLOR_FONDO)
etiqueta_fecha.pack()

# Barra de menú
barra_menu = tk.Menu(root, font=FUENTE_NORMAL, bg=COLOR_FONDO, fg=COLOR_TEXTO, tearoff=0)

# Menú Salud
menu_salud = tk.Menu(barra_menu, tearoff=0, bg=COLOR_FONDO, fg=COLOR_TEXTO)
menu_salud.add_command(label=obtener_texto("pasos"), command=mostrar_pasos)
menu_salud.add_command(label=obtener_texto("ritmo"), command=mostrar_ritmo_cardiaco)
barra_menu.add_cascade(label=obtener_texto("salud"), menu=menu_salud)

# Menú Alarma
menu_alarma = tk.Menu(barra_menu, tearoff=0, bg=COLOR_FONDO, fg=COLOR_TEXTO)
menu_alarma.add_command(label=obtener_texto("config_alarma"), command=configurar_alarma)
barra_menu.add_cascade(label=obtener_texto("alarma"), menu=menu_alarma)

# Menú Ajustes
menu_ajustes = tk.Menu(barra_menu, tearoff=0, bg=COLOR_FONDO, fg=COLOR_TEXTO)
menu_ajustes.add_command(label=obtener_texto("idioma"), command=mostrar_selector_idioma)
menu_ajustes.add_command(label=obtener_texto("brillo"), command=ajustar_brillo)
barra_menu.add_cascade(label=obtener_texto("ajustes"), menu=menu_ajustes)

# Menú Recordatorios
menu_recordatorios = tk.Menu(barra_menu, tearoff=0, bg=COLOR_FONDO, fg=COLOR_TEXTO)
menu_recordatorios.add_command(label=obtener_texto("agregar_rec"), command=lambda: agregar_rec_desde_calendario(
    datetime.now().day, datetime.now().month, datetime.now().year))
menu_recordatorios.add_command(label=obtener_texto("ver_rec"), command=ver_recordatorios)
barra_menu.add_cascade(label=obtener_texto("recordatorios"), menu=menu_recordatorios)

# Menú Calendario
barra_menu.add_command(label=obtener_texto("calendario"), command=mostrar_calendario_completo)

# Menú Salir
barra_menu.add_command(label=obtener_texto("salir"), command=root.quit)

root.config(menu=barra_menu)
actualizar_tiempo()
root.mainloop()
