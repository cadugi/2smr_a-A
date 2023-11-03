import tkinter as tk
from tkinter import simpledialog, messagebox
from fractions import Fraction

def cifrar_mensaje():
    M = int(simpledialog.askstring("Cifrar Mensaje", "Ingresa el mensaje a cifrar (M, del emisor):"))
    k = Fraction(simpledialog.askstring("Cifrar Mensaje", "Ingresa el valor de k (del emisor):"))
    n = int(simpledialog.askstring("Cifrar Mensaje", "Ingresa el valor de n (del receptor):"))
    C = pow(M, k.numerator, n)
    messagebox.showinfo("Resultado", f"Mensaje cifrado (C): {C}")

def descifrar_mensaje():
    C = int(simpledialog.askstring("Descifrar Mensaje", "Ingresa el mensaje cifrado (C, del receptor):"))
    j = Fraction(simpledialog.askstring("Descifrar Mensaje", "Ingresa el valor de j (del receptor):"))
    n = int(simpledialog.askstring("Descifrar Mensaje", "Ingresa el valor de n (del receptor):"))

    if j.denominator != 1:
        messagebox.showerror("Error", "j debe ser un número entero.")
        return

    j = j.numerator
    M = pow(C, j, n)
    messagebox.showinfo("Resultado", f"Mensaje descifrado (M): {M}")

def calcular_clave_privada():
    x = Fraction(simpledialog.askstring("Calcular Clave Privada", "Ingresa el valor de x (del receptor):"))
    z = Fraction(simpledialog.askstring("Calcular Clave Privada", "Ingresa el valor de z (del receptor):"))
    k = Fraction(simpledialog.askstring("Calcular Clave Privada", "Ingresa el valor de k (del receptor):"))

    j = None
    while j is None or j.denominator != 1:
        x += 1
        j = (1 + x * z) / k

    j = j.numerator
    messagebox.showinfo("Resultado", f"Clave privada (j): {j}")

def mostrar_menu_operaciones():
    operaciones_menu = tk.Tk()
    operaciones_menu.title("Seleccionar Operación")

    cifrar_button = tk.Button(operaciones_menu, text="Cifrar Mensaje", command=cifrar_mensaje)
    descifrar_button = tk.Button(operaciones_menu, text="Descifrar Mensaje", command=descifrar_mensaje)
    calcular_button = tk.Button(operaciones_menu, text="Calcular Clave Privada", command=calcular_clave_privada)

    cifrar_button.pack()
    descifrar_button.pack()
    calcular_button.pack()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cifrado y Descifrado")

# Botón para seleccionar operaciones
boton_operaciones = tk.Button(ventana, text="Seleccionar Operación", command=mostrar_menu_operaciones)
boton_operaciones.pack()

# Ejecutar la ventana
ventana.mainloop()
