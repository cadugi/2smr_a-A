import tkinter as tk

# Inicializar el contador
contador = 1

# Función para incrementar el valor
def incrementar(event=None):
    valor_actual = int(label_valor.cget("text"))
    label_valor.config(text=str(valor_actual + 1))
    actualizar_color(valor_actual + 1)

# Función para decrementar el valor
def decrementar(event=None):
    valor_actual = int(label_valor.cget("text"))
    label_valor.config(text=str(valor_actual - 1))
    actualizar_color(valor_actual - 1)

# Función para actualizar el color del texto
def actualizar_color(valor):
    if valor % 100 == 0:
        label_valor.config(fg='gold')  # Cambiar el color a dorado
    else:
        label_valor.config(fg='black')  # Restaurar el color normal

# Función para alternar la ventana en primer plano
def alternar_primero_plano():
    if ventana.attributes('-topmost'):
        ventana.attributes('-topmost', 0)
        boton_primero_plano.config(text="Fijo")
    else:
        ventana.attributes('-topmost', 1)
        boton_primero_plano.config(text="No Fijo")

# Función para guardar el número máximo en un archivo de registro
def guardar_maximo():
    global contador  # Utilizar la variable contador global
    valor_actual = int(label_valor.cget("text"))
    registro = f"{valor_actual} Vales dichos por el profe en la clase {contador}\n"
    with open("registro_valores_maximos.txt", "a") as archivo:
        archivo.write(registro)
    contador += 1  # Incrementar el contador

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sumador con Teclado y Entrada Manual")

# Etiqueta para mostrar el valor
label_valor = tk.Label(ventana, text="0", font=("Arial", 24), fg='black')  # Color de fuente inicial negro
label_valor.pack(pady=20, side=tk.LEFT)

# Etiqueta para "Valores Deseados"
etiqueta_valores_deseados = tk.Label(ventana, text="Vales", font=("consolas", 12))
etiqueta_valores_deseados.pack(padx=10, side=tk.LEFT)

# Botones para sumar y restar (simulando flechas)
boton_sumar = tk.Button(ventana, text="↑", font=("consolas", 12), command=incrementar)
boton_restar = tk.Button(ventana, text="↓", font=("Consolas", 12), command=decrementar)

boton_sumar.pack(side=tk.LEFT, padx=10)
boton_restar.pack(side=tk.LEFT)

# Configurar eventos de teclado
ventana.bind("+", incrementar)  # Presionar "+" para incrementar
ventana.bind("-", decrementar)  # Presionar "-" para decrementar

# Botón para alternar el primer plano
boton_primero_plano = tk.Button(ventana, text="Fijo", font=("Consolas", 12), command=alternar_primero_plano)
boton_primero_plano.pack(pady=10)

# Botón para guardar el número máximo en un archivo de registro
boton_guardar_maximo = tk.Button(ventana, text="Guardar Máximo", font=("Consolas", 12), command=guardar_maximo)
boton_guardar_maximo.pack(pady=10)

# Etiqueta "Creado por cadugi" en la parte inferior izquierda
etiqueta_creado_por = tk.Label(ventana, text="Creado por cadugi", font=("Consolas", 5))
etiqueta_creado_por.pack(side=tk.LEFT, anchor="sw", padx=5)

# Ejecutar la aplicación
ventana.mainloop()
