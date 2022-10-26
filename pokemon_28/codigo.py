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