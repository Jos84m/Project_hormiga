import random
from hormiga import Hormiga

class AlgoritmoGenetico:
    def __init__(self, tamaño_poblacion, longitud_secuencia, tasa_mutacion):
        self.tamaño_poblacion = tamaño_poblacion
        self.longitud_secuencia = longitud_secuencia
        self.tasa_mutacion = tasa_mutacion
        self.poblacion = []
    
    def inicializar_poblacion(self):
        for _ in range(self.tamaño_poblacion):
            hormiga = Hormiga(0, 0)
            hormiga.generar_secuencia_genetica(self.longitud_secuencia)
            self.poblacion.append(hormiga)
    
    def seleccionar_padres(self):
        # Selección por torneo
        tamaño_torneo = 5
        padres = []
        for _ in range(2):
            torneo = random.sample(self.poblacion, tamaño_torneo)
            ganador = max(torneo, key=lambda hormiga: hormiga.puntos)
            padres.append(ganador)
        return padres
    
    def cruzar(self, padre1, padre2):
        hijo = Hormiga(0, 0)
        punto_cruce = random.randint(0, self.longitud_secuencia - 1)
        hijo.secuencia_genetica = padre1.secuencia_genetica[:punto_cruce] + padre2.secuencia_genetica[punto_cruce:]
        return hijo
    
    def mutar(self, hormiga):
        hormiga.mutar_secuencia_genetica(self.tasa_mutacion)
    
    def evolucionar(self):
        nueva_poblacion = []
        for _ in range(self.tamaño_poblacion):
            padre1, padre2 = self.seleccionar_padres()
            hijo = self.cruzar(padre1, padre2)
            self.mutar(hijo)
            nueva_poblacion.append(hijo)
        self.poblacion = nueva_poblacion