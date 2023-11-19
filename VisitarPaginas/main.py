import customtkinter as ctk
from generarExcel import generar
from leyendoExcel import leer


ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
app.title("ProductFinder")



def ejecutarFunciones():
    leer()
    generar()




# Use CTkButton instead of tkinter Button
buttonGenerarExcel = ctk.CTkButton(master=app, text="Generar Excel", command=ejecutarFunciones)
buttonGenerarExcel.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

app.mainloop()
