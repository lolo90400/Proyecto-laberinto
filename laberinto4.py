import os
from readchar import readkey
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

def crear_laberinto (laberinto_str):
    filas = laberinto_str.split("\n")
    matriz = [list(fila) for fila in filas] 
    return matriz


def mostrar_pantalla(matriz):
    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in matriz:
        print("".join(fila))


def main_loop(laberinto_mapa,posicion_inicial, posicion_final):
    mapa = crear_laberinto(laberinto_mapa)
    px,py = posicion_inicial
    
    while (px,py) != posicion_final:
        mostrar_pantalla(mapa)
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
        
    mostrar_pantalla(mapa)

    if (px,py) == posicion_final:
        print('Felicidades has terminado el juego' )


posicion_inicial = (0,0) 
posicion_final = (len(laberinto.split('\n'))-1, len(laberinto.split('\n')[0])-1)

        
main_loop(laberinto,posicion_inicial,posicion_final)
    


