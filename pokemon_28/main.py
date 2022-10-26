from codigo1 import *
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