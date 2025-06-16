import tkinter 
from datetime import datetime
ventana = tkinter.Tk()
ventana.geometry("400x300")
def actualizar_hora():
    ahora = datetime.now().strftime("%H:%M:%S")
    etiqueta_hora.config(text=ahora)
    root.after(1000, actualizar_hora)



ventana.mainloop()