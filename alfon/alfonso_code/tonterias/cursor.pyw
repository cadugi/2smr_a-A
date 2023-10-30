import tkinter as tk
import threading
import time
import pygetwindow as gw
from PIL import Image, ImageTk

def create_icon_window():
    window = tk.Tk()
    window.overrideredirect(True)  # Oculta la barra de título y bordes
    window.wm_attributes("-topmost", 1)  # Mantén la ventana siempre en la parte superior
    window.geometry("100x100")
    window.configure(bg='black')  # Establece el fondo a negro
    
    # Carga una imagen y muestra la imagen en la ventana
    img = Image.open("tonterias/luis.ico")  # Reemplaza con la ubicación de tu propia imagen
    img = img.resize((100, 100))
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(window, image=img)
    panel.pack()

    return window

def move_window():
    while True:
        active_window = gw.getActiveWindow()
        if active_window != window:
            window.lift(active_window)
        time.sleep(0.1)

def click_handler(event):
    # Puedes realizar alguna acción aquí si lo deseas
    pass

if __name__ == "__main__":
    window = create_icon_window()
    window.bind("<Button-1>", click_handler)  # Enlaza el evento de clic izquierdo a la función click_handler
    
    # Iniciar un hilo para mover la ventana debajo de otras ventanas
    move_window_thread = threading.Thread(target=move_window)
    move_window_thread.daemon = True
    move_window_thread.start()

    window.mainloop()
