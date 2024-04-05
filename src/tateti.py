from random import choice

JUGADOR1 = 'X'
JUGADOR2 = 'O'
POSICION_LIBRE = " "

def crear_juego(filas, columnas):
	"""..."""

	return {
		"TABLERO": [[POSICION_LIBRE for columna in range(columnas)] for fila in range(filas)],
		"POSICION_JUGADOR1": [],
		"POSICION_JUGADOR2": [],
		"TURNO": choice([JUGADOR1, JUGADOR2])
	}

def verificar_dentro_de_rango(tablero, coordenada_x, coordenada_y):
	"""..."""

	return 0 <= coordenada_x < len(tablero[0]) and 0 <= coordenada_y < len(tablero)

def colocar_pieza(juego, coordenadas):
	"""..."""

	coordenada_x, coordenada_y = coordenadas
	if verificar_dentro_de_rango(juego["TABLERO"], coordenada_x, coordenada_y) and juego["TABLERO"][coordenada_y][coordenada_x] == POSICION_LIBRE:
		juego["TABLERO"][coordenada_y][coordenada_x] = juego["TURNO"]
		if juego["TURNO"] == JUGADOR1:
			juego["POSICION_JUGADOR1"].append((coordenada_x, coordenada_y))
		else:
			juego["POSICION_JUGADOR2"].append((coordenada_x, coordenada_y))
		return True

def cambiar_turno(turno):
	"""..."""

	if turno == JUGADOR1:
		turno = JUGADOR2
	else:
		turno = JUGADOR1
	return turno

def verificar_tablero_lleno(tablero):
	"""..."""

	for fila in range(len(tablero)):
		if POSICION_LIBRE in tablero[fila]:
			return False
	return True

def hay_ganador(tablero):
	"""..."""

	if \
	(tablero[0][0] == tablero[0][1] and tablero[0][0] == tablero[0][2] and tablero[0][0] != ' ') or\
	(tablero[1][0] == tablero[1][1] and tablero[1][0] == tablero[1][2] and tablero[1][0] != ' ') or\
	(tablero[2][0] == tablero[2][1] and tablero[2][0] == tablero[2][2] and tablero[2][0] != ' ') or\
	(tablero[0][0] == tablero[1][0] and tablero[0][0] == tablero[2][0] and tablero[0][0] != ' ') or\
	(tablero[0][1] == tablero[1][1] and tablero[0][1] == tablero[2][1] and tablero[0][1] != ' ') or\
	(tablero[0][2] == tablero[1][2] and tablero[0][2] == tablero[2][2] and tablero[0][2] != ' ') or\
	(tablero[0][0] == tablero[1][1] and tablero[0][0] == tablero[2][2] and tablero[0][0] != ' ') or\
	(tablero[0][2] == tablero[1][1] and tablero[0][2] == tablero[2][0] and tablero[0][2] != ' '):
		return True

def terminar_juego(tablero):
	"""..."""
	
	return hay_ganador(tablero) or verificar_tablero_lleno(tablero)