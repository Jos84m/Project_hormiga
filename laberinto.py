class Laberinto:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.matriz = [[None for _ in range(tamaño[1])] for _ in range(tamaño[0])]
    
    def colocar_item(self, x, y, item):
        if 0 <= x < self.tamaño[0] and 0 <= y < self.tamaño[1]:
            self.matriz[x][y] = item
    
    def obtener_item(self, x, y):
        if 0 <= x < self.tamaño[0] and 0 <= y < self.tamaño[1]:
            return self.matriz[x][y]
        return None
    
    def actualizar_estado(self, x, y, nuevo_estado):
        if 0 <= x < self.tamaño[0] and 0 <= y < self.tamaño[1]:
            self.matriz[x][y] = nuevo_estado

class Azucar:
    def __init__(self, puntos=10, imagen='azucar.png'):
        self.puntos = puntos
        self.imagen = imagen

class Vino:
    def __init__(self, nivel_alcohol=5, imagen='vino.png'):
        self.nivel_alcohol = nivel_alcohol
        self.imagen = imagen

class Veneno:
    def __init__(self, daño=5, duracion=3, imagen='veneno.png'):
        self.daño = daño  # Daño que causa al ser consumido
        self.duracion = duracion  # Número de turnos que afecta
        self.imagen = imagen

    def aplicar_efecto(self, jugador):
        print(f'El veneno causa {self.daño} puntos de daño al jugador.')
        jugador.salud -= self.daño  # Suponiendo que el jugador tiene un atributo salud

class Roca:
    def __init__(self, resistencia=10, imagen='roca.png'):
        self.resistencia = resistencia  # Resistencia de la roca
        self.imagen = imagen

    def interactuar(self, jugador):
        print(f'El jugador intenta mover la roca con {self.resistencia} de resistencia.')
        if jugador.fuerza >= self.resistencia:
            print('¡La roca ha sido movida!')
            return True
        else:
            print('No puedes mover la roca, necesitas más fuerza.')
            return False 