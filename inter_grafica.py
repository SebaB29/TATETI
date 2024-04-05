import gamelib

ALTO_VENTANA, ANCHO_VENTANA = (500, 500)
MARGEN_X, MARGEN_Y = (100, 100)
FILAS_TABLERO, COLUMNAS_TABLERO = (3, 3)
ANCHO_TABLERO, ALTO_TABLERO = ((ANCHO_VENTANA - MARGEN_X * 2), (ALTO_VENTANA - MARGEN_Y * 2))
ANCHO_CELDA, ALTO_CELDA = (ANCHO_TABLERO / COLUMNAS_TABLERO, ALTO_TABLERO / FILAS_TABLERO)

def definir_titulo_ventana():
    """..."""
    gamelib.title("Tic-Tac-Toe")

def graficar_titulo():
    """..."""

    gamelib.draw_text("TIC-TAC-TOE", ANCHO_VENTANA / 2, MARGEN_Y / 2, size=20)

def graficar_tablero(filas, columnas):
    """..."""

    gamelib.draw_rectangle(MARGEN_X, MARGEN_Y, ANCHO_VENTANA - MARGEN_X, ALTO_VENTANA - MARGEN_Y, fill="#000000", outline="#0020FF", width=2)

    # Divide las filas del tablero
    posicion_linea_horizontal =  MARGEN_Y + ALTO_CELDA
    for _ in range(filas - 1):
        gamelib.draw_line(MARGEN_X, posicion_linea_horizontal, ANCHO_VENTANA - MARGEN_X, posicion_linea_horizontal, fill="#0020FF", width=2)
        posicion_linea_horizontal += ALTO_CELDA

    # Divide las columnas del tablero
    posicion_linea_vertical = MARGEN_X + ANCHO_CELDA
    for _ in range(columnas - 1):
        gamelib.draw_line(posicion_linea_vertical, MARGEN_Y, posicion_linea_vertical, ALTO_VENTANA - MARGEN_Y, fill="#0020FF", width=2)
        posicion_linea_vertical += ANCHO_CELDA

def graficar_turno(turno):
    """..."""

    gamelib.draw_text(f"TURNO: {turno}", ANCHO_VENTANA / 2, ALTO_VENTANA - MARGEN_Y / 2, size=20)

def graficar_piezas(coordenadas_piezas, jugador, color):
    """..."""

    for coord_x_pixels, coord_y_pixels in convertir_coordenadas_a_pixels(coordenadas_piezas):
        gamelib.draw_text(jugador, coord_x_pixels + ANCHO_CELDA / 2, coord_y_pixels + ALTO_CELDA / 2, fill=color, size=30)

def graficar_ganador(jugador):
    """..."""

    gamelib.draw_text("GANO", ANCHO_VENTANA / 2, ALTO_VENTANA / 2 - 20, size=30)
    gamelib.draw_text(f"{jugador}", ANCHO_VENTANA / 2, ALTO_VENTANA / 2 + 20, size=30)

def graficar_empate():
    """..."""

    gamelib.draw_text("EMPATE", ANCHO_VENTANA / 2, ALTO_VENTANA / 2 - 20, size=30)

def graficar_boton_volver_a_jugar():
    """..."""

    gamelib.draw_rectangle(ANCHO_VENTANA * 1/4, 400, ANCHO_VENTANA * 3/4, 450, fill="#000000", outline="#FFFFFF")
    gamelib.draw_text("Volver a empezar", ANCHO_VENTANA / 2, 425, size=15)

def convertir_pixels_a_coordenadas(coord_pixels_x, coord_pixels_y):
    """..."""

    return int((coord_pixels_x - MARGEN_X) // ANCHO_CELDA), int((coord_pixels_y - MARGEN_Y) // ALTO_CELDA)

def convertir_coordenadas_a_pixels(coordenadas_jugador):
    """..."""
    
    return [[MARGEN_X + ANCHO_CELDA * columna, MARGEN_Y + ALTO_CELDA * fila] for columna, fila in coordenadas_jugador]