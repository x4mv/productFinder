import customtkinter as ctk
import subprocess
import os

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

# Obtener la ruta absoluta al script
rutaArchivo = os.path.abspath(r"c:\Users\IDEAPAD\Desktop\buscador\VisitarPaginas\generarExcel.py")

if os.path.exists(rutaArchivo):
    # El archivo existe, ahora puedes ejecutarlo
    def generarExcel():
        try:
            # Reemplaza "ruta/del/tu_script.py" con la ruta completa de tu script Python
            subprocess.run(["python", rutaArchivo], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el script: {e}")

else:
    print(f"El archivo no existe en la ruta especificada: {rutaArchivo}")
    def generarExcel():
        print("No se puede generar el Excel porque el archivo no existe.")

# Use CTkButton instead of tkinter Button
buttonGenerarExcel = ctk.CTkButton(master=app, text="Generar Excel", command=generarExcel)
buttonGenerarExcel.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

app.mainloop()
