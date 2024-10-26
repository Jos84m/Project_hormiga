import random

from laberinto import Azucar, Veneno, Vino

class Hormiga:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.salud = 100
        self.nivel_alcohol = 0
        self.puntos = 0
        self.secuencia_genetica = []
    
    def mover(self, direccion):
        if direccion == 'arriba':
            self.y -= 1
        elif direccion == 'abajo':
            self.y += 1
        elif direccion == 'izquierda':
            self.x -= 1
        elif direccion == 'derecha':
            self.x += 1
    
    def comer(self, item):
        if isinstance(item, Azucar):
            self.puntos += item.puntos
        elif isinstance(item, Vino):
            self.nivel_alcohol += item.nivel_alcohol
        elif isinstance(item, Veneno):
            self.salud = 0
    
    def modificar_salud(self, cantidad):
        self.salud = max(0, min(100, self.salud + cantidad))
    
    def modificar_nivel_alcohol(self, cantidad):
        self.nivel_alcohol = max(0, min(50, self.nivel_alcohol + cantidad))
    
    def generar_secuencia_genetica(self, longitud):
        acciones = ['arriba', 'abajo', 'izquierda', 'derecha', 'comer']
        self.secuencia_genetica = [random.choice(acciones) for _ in range(longitud)]
    
    def mutar_secuencia_genetica(self, tasa_mutacion):
        acciones = ['arriba', 'abajo', 'izquierda', 'derecha', 'comer']
        for i in range(len(self.secuencia_genetica)):
            if random.random() < tasa_mutacion:
                self.secuencia_genetica[i] = random.choice(acciones)