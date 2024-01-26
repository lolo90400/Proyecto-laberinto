import os
from readchar import readkey
import random

class juego:
    def __init__(self, laberinto, posicion_inicial,posicion_final):
        self.laberinto = laberinto
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
        



    def crear_laberinto (self):
        filas = self.laberinto
        matriz = [list(fila) for fila in filas] 
        return matriz


    def mostrar_pantalla(self,matriz):
        os.system('cls' if os.name == 'nt' else 'clear')
        for fila in matriz:
            print("".join(fila))


    def main_loop(self):
        mapa = self.crear_laberinto()
        px,py = self.posicion_inicial
        
        while (px,py) != self.posicion_final:
            self.mostrar_pantalla(mapa)
            mapa[py][px] = 'P'
            
            print("Presione una tecla de direccion para mover al jugador y Q para salir")
            tecla_oprimida = readkey() 
            if tecla_oprimida == 'q':
                break
            elif tecla_oprimida == 'w':
                if py -1 >= 0 and  mapa[py-1][px] != '#':
                    mapa[py][px]  = '.'
                    mapa[py-1][px] = 'P'
                    py -= 1

            elif tecla_oprimida == 's':
                if py +1 < len(mapa) and  mapa[py+1][px] != '#':
                    mapa[py][px]  = '.'
                    mapa[py+1][px] = 'P'
                    py += 1
                
            elif tecla_oprimida == 'a':
                if px -1 >= 0 and  mapa[py][px-1] != '#':
                    mapa[py][px]  = '.'
                    mapa[py][px-1] = 'P'
                    px -= 1

            elif tecla_oprimida == 'd':
                if px +1 < len(mapa) and  mapa[py][px+1] != '#':
                    mapa[py][px]  = '.'
                    mapa[py][px+1] = 'P'
                    px += 1
            
        self.mostrar_pantalla(mapa)

        if (px,py) == self.posicion_final:
            print('Felicidades has terminado el juego' )


class JuegoArchivo(juego):
    def __init__(self, path_a_mapas):
        # Obtener la lista de archivos de mapas
        archivos_mapas = os.listdir(path_a_mapas)
        # Elegir un archivo al azar
        nombre_archivo = random.choice(archivos_mapas)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        # Leer el archivo seleccionado
        with open(path_completo, 'r') as file:
            contenido = file.read()

        # Extraer las posiciones iniciales y finales del archivo
        lineas = contenido.split('\n')
        inicio_x, inicio_y, fin_x, fin_y = map(int, lineas[0].split())
        posicion_inicial = (inicio_x, inicio_y)
        posicion_final = (fin_x, fin_y)

        # Llamar al constructor de la clase base
        super().__init__(lineas[1:22], posicion_inicial, posicion_final)

    # Iniciar el juego desde un archivo
juego_archivo = JuegoArchivo("mapas")
juego_archivo.main_loop()
    
