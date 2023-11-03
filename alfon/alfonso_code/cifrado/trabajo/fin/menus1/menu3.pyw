import tkinter as tk
from tkinter import simpledialog, messagebox

def cifrar_mensaje():
    M = int(simpledialog.askstring("Cifrar Mensaje", "Ingresa el mensaje a cifrar (M, del emisor):"))
    k = int(simpledialog.askstring("Cifrar Mensaje", "Ingresa el valor de k (del emisor):"))
    n = int(simpledialog.askstring("Cifrar Mensaje", "Ingresa el valor de n (del receptor):"))
    C = pow(M, k, n)
    messagebox.showinfo("Resultado", f"Mensaje cifrado (C): {C}")

def descifrar_mensaje():
    C = int(simpledialog.askstring("Descifrar Mensaje", "Ingresa el mensaje cifrado (C, del receptor):"))
    j = int(simpledialog.askstring("Descifrar Mensaje", "Ingresa el valor de j (del receptor):"))
    n = int(simpledialog.askstring("Descifrar Mensaje", "Ingresa el valor de n (del receptor):"))
    M = pow(C, j, n)
    messagebox.showinfo("Resultado", f"Mensaje descifrado (M): {M}")

def calcular_clave_privada():
    x = int(simpledialog.askstring("Calcular Clave Privada", "Ingresa el valor de x (del receptor):"))
    z = int(simpledialog.askstring("Calcular Clave Privada", "Ingresa el valor de z (del receptor):"))
    k = int(simpledialog.askstring("Calcular Clave Privada", "Ingresa el valor de k (del receptor):"))
    j = None
    while j is None or j % k != 0:
        x += 1
        j = (1 + x * z) // k
    messagebox.showinfo("Resultado", f"Clave privada (j): {j}")

def mostrar_menu_operaciones():
    operaciones_menu = tk.Tk()
    operaciones_menu.title("Seleccionar Operación")

    # Configurar tearoff para evitar la solapa en el menú
    operaciones_menu.option_add('*tearOff', False)

    operaciones_menu_bar = tk.Menu(operaciones_menu)
    operaciones_menu['menu'] = operaciones_menu_bar

    cifrar_button = tk.Button(operaciones_menu, text="Cifrar Mensaje", command=cifrar_mensaje, width=20, height=2)
    descifrar_button = tk.Button(operaciones_menu, text="Descifrar Mensaje", command=descifrar_mensaje, width=20, height=2)
    calcular_button = tk.Button(operaciones_menu, text="Calcular Clave Privada", command=calcular_clave_privada, width=20, height=2)

    cifrar_button.pack()
    descifrar_button.pack()
    calcular_button.pack()

    operaciones_menu.mainloop()

# Mostrar el menú de operaciones automáticamente al iniciar la aplicación
mostrar_menu_operaciones()
