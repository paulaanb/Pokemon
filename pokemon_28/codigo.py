import random
import LEVEL
import math
import IV
import pokemon_data.csv
#Formulas para la batalla pokemon
def obtener_hp(base):
    resultado_parentesis = (base+IV)*2+((math.sqrt(EV))/4)
    return (resultado_parentesis * LEVEL / 100) + LEVEL+10


def obtener_other_stat(base):
    resultado_parentesis = (base+IV)*2+((math.sqrt(EV))/4)
    return (resultado_parentesis * LEVEL / 100)+5


def obtener_damage(power, ataque, defensa):
    resultado_parentesis_interior = ((2*LEVEL)/5)+2
    numero_aleatorio = random.uniform(0.85, 1.0)
    resultado_parentesis = (
        (resultado_parentesis_interior * power * (ataque/defensa)) / 50) + 2
    return resultado_parentesis * numero_aleatorio

#Leer la lista pokemon
def obtener_diccionario_segun_csv():
    pokemones = {}
    with open(pokemon_data.csv, "r") as archivo:
        for linea in archivo:
            columnas = linea.split(",")
            nombre = columnas[0]
            puntos_de_vida = int(columnas[1])
            puntos_de_ataque = int(columnas[2])
            puntos_de_defensa = int(columnas[3])
            movimientos_posibles = columnas[4].split(";")
            # Ahora que ya lo tenemos parseado, lo agregamos al diccionario
            pokemones[nombre] = {
                "puntos_de_vida": puntos_de_vida,
                "puntos_de_ataque": puntos_de_ataque,
                "puntos_de_defensa": puntos_de_defensa,
                "movimientos_posibles": movimientos_posibles,
            }
    return pokemones

#Calculamos el poder de ataque
from moves import get_move

def solicitar_movimiento(movimientos):
    while True:
        print("Movimientos que puede aprender el pokémon: ")
        for indice, movimiento in enumerate(movimientos):
            print(f"{indice} - {movimiento}")
        indice_movimiento = int(input("Seleccione un ataque a ejecutar: "))
        if indice_movimiento < 0 or indice_movimiento > len(movimientos) - 1:
            print("Número inválido")
            continue

        movimiento = movimientos[indice_movimiento]
        print(f"El ataque seleccionado es: {movimiento}")
        poder_ataque = get_move(normalizar_nombre(movimiento))
        if poder_ataque > 0:
            return poder_ataque
        else:
            print("El ataque tiene un poder de 0. Seleccione otro movimiento")