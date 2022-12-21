#
# Título:       ¿Más alto o más bajo?
# Descripción:  Se extraen 8 cartas de una baraja de 40 y se muestra la primera.
#               El jugador debe adivinar si el valor de la siguiente carta será
#               más alto o más bajo. Si aicerta gana 20 puntos y si se equivoca
#               o la siguiente carta tiene el mismo valor que la anterior, 
#               pierde 15 puntos

# Módulos auxiliares
import random

# Constantes de la baraja
PALOS = ('Bastos', 'Corazones', 'Espadas', 'Oros')
NOMBRES = ('As', '2', '3', '4', '5', '6', '7', 'Sota', 'Caballo', 'Rey')
NUM_CARTAS = 8

# Toma una carta de un mazo
def toma_carta(mazo):
    carta = mazo.pop() # Toma la carta de arriba
    return carta

# Baraja el mazo
def baraja_mazo(mazo):
    mazo_barajado = mazo.copy() # Copia la baraja inicial
    random.shuffle(mazo_barajado)
    return mazo_barajado

# Código principal
presentacion = '''
¡Te doy la bienvenida a "¿Más alto o más bajo?"!
Escoge si la siguiente carta tendrá un valor más alto o más bajo que la actual.
Si aciertas, ganarás 20 puntos; pero si te equivocas perderás 15 puntos.
Inicias el juego con 50 puntos.\n
'''

print(presentacion)

mazo = []

for palo in PALOS:
    for valor, nombre in enumerate(NOMBRES):
        carta = {'nombre': nombre, 'palo': palo, 'valor': valor + 1}
        mazo.append(carta)

puntos = 50

while True: # Para jugar múltiples partidas    
    mazo_partida = baraja_mazo(mazo)
    carta_actual = toma_carta(mazo_partida)
    carta_actual_nombre = carta_actual['nombre']
    carta_actual_valor = carta_actual['valor']
    carta_actual_palo = carta_actual['palo']
    print(f'La carta inicial es: {carta_actual_nombre} de {carta_actual_palo}, '
          f'cuyo valor asciende a {carta_actual_valor} puntos.')

    for numero_carta in range(0, NUM_CARTAS):
        print('¿La siguiente carta tendrá un valor más alto o más bajo?')
        respuesta = input('Introduce a (más alto) o b (más bajo): ')
        respuesta = respuesta.casefold() # fuerza minúsculas
        carta_siguiente = toma_carta(mazo_partida)
        carta_siguiente_nombre = carta_siguiente['carta']
        carta_siguiente_valor = carta_siguiente['valor']
        carta_siguiente_palo = carta_siguiente['palo']
        print(f'La siguiente carta es: {carta_siguiente_nombre} de {carta_siguiente_palo}, '
              f'cuyo valor asciende a {carta_siguiente_valor} puntos.')

        if respuesta == 'a':
            if carta_siguiente_valor > carta_actual_valor:
                print('¡Acertaste! ¡El valor es mayor!')
                puntos += 20
            else:
                print('¡Fallaste! ¡El valor es menor!')
                puntos -= 15
        elif respuesta == 'b':
            if carta_siguiente_valor < carta_actual_valor:
                print('¡Acertaste! ¡El valor es menor!')
                puntos += 20
            else:
                print('¡Fallaste! ¡El valor es mayor!')
                puntos -= 15
        
        print(f'Tu puntuación es de {puntos} puntos.\n')
        
        carta_actual_nombre = carta_siguiente_nombre
        carta_actual_valor = carta_siguiente_valor # No necesitamos el palo
    
    de_nuevo = input('Para jugar de nuevo, pulsa INTRO. Para terminar, pulsa "S": ')
    if de_nuevo == 'S':
        break

print('¡Hasta la próxima!')