import tkinter as tk
from PIL import Image, ImageTk
import pystray
import sys
import threading
import time

# Función para cerrar la aplicación
def exit_action(icon, item):
    icon.stop()
    sys.exit()

# Función para mover la imagen
def move_image():
    while True:
        x, y = pyautogui.position()
        window.geometry(f"100x100+{x-50}+{y-50}")
        time.sleep(0.01)  # Ajusta este valor para controlar el retraso

root = tk.Tk()
root.overrideredirect(True)  # Oculta la barra de título y bordes
root.wm_attributes("-topmost", 1)  # Mantén la ventana siempre en la parte superior
root.withdraw()  # Oculta la ventana principal

# Usa una ventana sin bordes
window = tk.Toplevel(root)
window.overrideredirect(True)
window.wm_attributes("-topmost", 1)
window.geometry("100x100")

canvas = tk.Canvas(window, width=100, height=100, bg='black')  # Establece un fondo negro
canvas.pack()

image = Image.open("C:/Users/a.carrero.AULA_2SMR/Documents/python/tonterias/icono/1.png")  # Reemplaza con la ubicación de tu propia imagen PNG
image = image.resize((100, 100))
image = ImageTk.PhotoImage(image)
image_id = canvas.create_image(50, 50, image=image)

# Inicia un hilo para mover la ventana con la imagen
move_thread = threading.Thread(target=move_image)
move_thread.daemon = True
move_thread.start()

# Crea un ícono en la bandeja del sistema
menu = pystray.Menu(pystray.MenuItem('Salir', exit_action))
icon = pystray.Icon("name", image, menu)
icon.run()

root.mainloop()
