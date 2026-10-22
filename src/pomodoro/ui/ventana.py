import customtkinter as ctk
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("light")   # o "dark", elegí vos

corriendo = False

def al_apretar():

    corriendo = not corriendo
    if corriendo:
        boton.configure(text="Pausar")
    else:
        boton.configure(text="Reanudar")

ventana = ctk.CTk()
ventana.title("Pomototo")
ventana.geometry("400x300")
ventana.resizable(False, False)
texto=ctk.CTkLabel(ventana, text="25:00", font=ctk.CTkFont(size=50))
texto.pack(pady=30)

boton = ctk.CTkButton(ventana, text="Iniciar", command=al_apretar
                      )
boton.pack(pady=20)

ventana.mainloop()