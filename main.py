import tkinter as tk
from tkinter import messagebox
from laberinto import Azucar, Vino, Veneno, Roca, Nada
from hormiga import Hormiga
from algoritmo_genetico import AlgoritmoGenetico

class SimulacionHormiga:
    def __init__(self, ventana):
        self.ventana = ventana
        self.tamano = 0
        self.laberinto = []
        self.hormiga = None

    def crear_laberinto(self):
        # Obtener el tamaño del laberinto desde la entrada de texto
        try:
            self.tamano = int(entrada_tamano.get())
            if self.tamano < 3 or self.tamano > 10:
                raise ValueError("El tamaño debe estar entre 3 y 10.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        
        # Limpiar ventana principal para mostrar el laberinto
        for widget in self.ventana.winfo_children():
            widget.destroy()

        # Crear el grid de botones para el laberinto
        laberinto_frame = tk.Frame(self.ventana)
        laberinto_frame.pack()

        self.laberinto = [[None for _ in range(self.tamano)] for _ in range(self.tamano)]
        
        for i in range(self.tamano):
            for j in range(self.tamano):
                btn = tk.Button(laberinto_frame, text=" ", width=5, height=2, command=lambda i=i, j=j: self.colocar_item(i, j))
                btn.grid(row=i, column=j)
        
        # Botón para iniciar la simulación
        boton_iniciar_simulacion = tk.Button(self.ventana, text="Iniciar Simulación", command=self.iniciar_simulacion)
        boton_iniciar_simulacion.pack()

    def colocar_item(self, i, j):
        # Distribuir ítems en el laberinto
        items = [Azucar(), Vino(), Veneno(), Roca(), Nada()]
        item = items[(i + j) % len(items)]  # Ejemplo simple de distribución de ítems
        self.laberinto[i][j] = item
        messagebox.showinfo("Colocación de ítem", f"Colocaste {item.__class__.__name__} en la casilla ({i}, {j})")

    def iniciar_simulacion(self):
        # Inicializar la hormiga y el algoritmo genético
        self.hormiga = Hormiga(self.laberinto)
        algoritmo = AlgoritmoGenetico(self.hormiga, self.laberinto)
        
        # Aquí se llamará al algoritmo genético para comenzar la simulación
        messagebox.showinfo("Simulación", "¡Comienza la simulación!")
        algoritmo.ejecutar()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Simulación de la Hormiga")

# Crear instancia de la simulación
simulacion = SimulacionHormiga(ventana)

# Entrada para el tamaño del laberinto
tk.Label(ventana, text="Tamaño del laberinto (entre 3 y 10):").pack()
entrada_tamano = tk.Entry(ventana)
entrada_tamano.pack()

# Botón para crear el laberinto
boton_iniciar = tk.Button(ventana, text="Crear Laberinto", command=simulacion.crear_laberinto)
boton_iniciar.pack()

# Iniciar el loop de la ventana
ventana.mainloop()
