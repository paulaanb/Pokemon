#Ponemos el codigo de manera dinamica y recursiva
from moves import get_move
import math
import random

LEVEL = 100  # nivel constante
IV = 31  # nivel constante
EV = 250  # nivel constante
ARCHIVO_POKEMON_DATA = "pokemon_data.csv"


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


# Regresa el nombre sin espacios y en minúscula
def normalizar_nombre(nombre):
    return nombre.lower().replace(" ", "")


def obtener_diccionario_segun_csv():
    pokemones = {}
    with open(ARCHIVO_POKEMON_DATA, "r") as archivo:
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


def main():
    pokemones = obtener_diccionario_segun_csv()
    print("Bienvenido al simulador")
    nombre_primer_pokemon = normalizar_nombre(
        input("Ingrese el nombre del primer Pokémon: "))
    if nombre_primer_pokemon not in pokemones:
        print("El Pokémon no existe")
        return
    primer_pokemon = pokemones[nombre_primer_pokemon]
    nombre_capitalizado = nombre_primer_pokemon.capitalize()
    print("Nombre del Pokémon seleccionado: " + nombre_capitalizado)
    print("Estadísticas base del Pokémon:")
    print(f"- HP = {primer_pokemon.get('puntos_de_vida')}")
    print(f"- Ataque = {primer_pokemon.get('puntos_de_ataque')}")
    print(f"- Defensa = {primer_pokemon.get('puntos_de_defensa')}")
    movimientos_primer_pokemon = primer_pokemon.get("movimientos_posibles")
    poder_ataque = solicitar_movimiento(movimientos_primer_pokemon)
    print(f"Poder de ataque es: {poder_ataque}")
    hp_nivel_100 = obtener_hp(primer_pokemon.get("puntos_de_vida"))
    atk_nivel_100 = obtener_other_stat(primer_pokemon.get("puntos_de_ataque"))
    def_nivel_100 = obtener_other_stat(primer_pokemon.get("puntos_de_defensa"))
    print(f"El hp al nivel 100 de {nombre_capitalizado} es {hp_nivel_100}")
    print(f"El atk al nivel 100 de {nombre_capitalizado} es {atk_nivel_100}")
    print(f"El def al nivel 100 de {nombre_capitalizado} es {def_nivel_100}")
    nombre_segundo_pokemon = normalizar_nombre(
        input("Ingrese el nombre a atacar Pokémon: "))
    if nombre_segundo_pokemon not in pokemones:
        print("El Pokémon no existe")
        return
    nombre_segundo_pokemon_capitalizado = nombre_segundo_pokemon.capitalize()
    print(
        f"Nombre del Pokémon seleccionado: {nombre_segundo_pokemon_capitalizado}")
    segundo_pokemon = pokemones.get(nombre_segundo_pokemon)
    hp_nivel_100_segundo_pokemon = obtener_hp(
        segundo_pokemon.get("puntos_de_vida"))
    print(
        f"El hp al nivel 100 de {nombre_segundo_pokemon_capitalizado} es {hp_nivel_100_segundo_pokemon}")
    def_nivel_100_segundo_pokemon = obtener_other_stat(
        segundo_pokemon.get("puntos_de_defensa"))
    damage = obtener_damage(poder_ataque, atk_nivel_100,
                            def_nivel_100_segundo_pokemon)
    print(
        f"El daño realizó {nombre_capitalizado} a {nombre_segundo_pokemon_capitalizado} fue de: {damage}")
    nuevo_hp = hp_nivel_100_segundo_pokemon - damage
    print(f"{nombre_segundo_pokemon_capitalizado} quedó con un HP de: {nuevo_hp}")


main()