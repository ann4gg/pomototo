import customtkinter as ctk
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("light")   # o "dark", elegí vos

ventana = ctk.CTk()
ventana.title("Pomototo")
ventana.geometry("400x300")
ventana.resizable(False, False)

ventana.mainloop()