from tkinter import *

# icono = PhotoImage(file="personaje_corazon.png")  # ICONO

window = Tk()  # ESTO CREA UNA VENTANA, CREAMOS UN OBJETO QUE GENERA LA VENTANA
window.geometry("900x300")  # TAMAÑO DE VENTANA
# TITULO DE VENTANA
window.title("Una aplicación sencilla para el amor de mí vida")
#window.iconphoto(True, icono)
window.config(background="yellow")

label = Label(window)
label2 = Label(window)
label3 = Label(window)
label4 = Label(window)
label5 = Label(window)
labels = [label, label2, label3, label4, label5]

txt = ["Te amo con todo mí corazon eres el amor de mí vida ", "Eres mi mitad mi razón de vivir",
       "Te amo demasiado lo eres todo para mí", "Nunca me dejes", "Te amo."]

for i in range(0, 5):

    labels[i].configure(
        fg="red",
        font=("Calibri", 30, "bold"),
        text=txt[i]
    )
    labels[i].pack()

window.mainloop()  # ESTO DEJA VER NUESTRA VENTANA Y RECIBE LOS EVENTOS
