from src.tateti import *
from graphics.inter_grafica import *

def main():
    """..."""

    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)
    definir_titulo_ventana()
    juego = crear_juego(FILAS_TABLERO, COLUMNAS_TABLERO)

    while not terminar_juego(juego["TABLERO"]):
        gamelib.draw_begin()
        graficar_titulo()
        graficar_tablero(FILAS_TABLERO, COLUMNAS_TABLERO)
        graficar_turno(juego["TURNO"])
        graficar_piezas(juego["POSICION_JUGADOR1"], JUGADOR1, "#00FF00")
        graficar_piezas(juego["POSICION_JUGADOR2"], JUGADOR2, "#FF0000")
        gamelib.draw_end()

        event = gamelib.wait(gamelib.EventType.ButtonPress)
        if colocar_pieza(juego, convertir_pixels_a_coordenadas(event.x, event.y)) and not terminar_juego(juego["TABLERO"]):
            juego["TURNO"] = cambiar_turno(juego["TURNO"])
    
    gamelib.draw_begin()
    if hay_ganador(juego["TABLERO"]):
        graficar_ganador(juego["TURNO"])
    else:
        graficar_empate()
    graficar_boton_volver_a_jugar()
    gamelib.draw_end()

    event = gamelib.wait(gamelib.EventType.ButtonPress)
    if ANCHO_VENTANA * 1/4 <= event.x <= ANCHO_VENTANA * 3/4 and 400 <= event.y <= 450:
        main()
        
gamelib.init(main)