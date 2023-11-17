import customtkinter as ctk
import subprocess
import os


ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
app.title("ProductFinder")

ruta_icono = os.path.normpath(r'c:\Users\IDEAPAD\Desktop\buscador\VisitarPaginas\icono_pf.ico')
app.iconbitmap(default=ruta_icono)


# Obtener la ruta absoluta al script
rutaGenerarExcel = os.path.abspath(r"c:\Users\IDEAPAD\Desktop\buscador\VisitarPaginas\generarExcel.py")
rutaLeerExcel = os.path.abspath(r"c:\Users\IDEAPAD\Desktop\buscador\VisitarPaginas\leyendoExcel.py")

if os.path.exists(rutaGenerarExcel):
    # El archivo existe, ahora puedes ejecutarlo
    def generarExcel():
        try:
            # Reemplaza "ruta/del/tu_script.py" con la ruta completa de tu script Python
            subprocess.run(["python", rutaGenerarExcel], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el script: {e}")
    
    def leerExcel():
        try:
            # Reemplaza "ruta/del/tu_script.py" con la ruta completa de tu script Python
            subprocess.run(["python", rutaLeerExcel], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el script: {e}")
    
    

else:
    print(f"El archivo no existe en la ruta especificada: {rutaGenerarExcel}")
    def generarExcel():
        print("No se puede generar el Excel porque el archivo no existe.")



# Use CTkButton instead of tkinter Button
buttonGenerarExcel = ctk.CTkButton(master=app, text="Generar Excel", command=generarExcel)
buttonGenerarExcel.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

app.mainloop()
