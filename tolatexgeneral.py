#!/usr/bin/env python
# -*- coding: utf-8 -*-

##=====================================================================================##
## Autor: Daniel López Coto															   ##
## Programa: Conversor de tablas a formato LaTeX									   ##
##=====================================================================================##

import numpy as np

##-----------------------##
### OPCIONES DE LECTURA ###
##-----------------------##

## Abrimos el archivo a leer ##

# Pedimos que metan el nombre del archivo y extensión

print ('Enter the name and the ' \
		'extension of the file')
a = raw_input()					# variable str donde se guarda el archivo a abrir

f = open(a,'r')					# abrimos el archivo con permisos de lectura

lines = f.readlines()			# leemos el archivo por lineas y lo guardamos en 'lines'

rows = len(lines)				# vemos el número de filas del archivo

s = lines[1].split()			# separamos las "palabras" para contar el número de
								# columnas
cols = len(s)					# almacenamos el numero de columnas

x = np.empty((rows,cols))		# creamos una "lista de listas" (matriz) vacía donde
								# almacenaremos los valores de cada fila y columna 
								# respectivamente.

# Con este bucle lo que hacemos es, en line separar cada "palabra" de la fila i-ésima y 
# asignarla a la variable "line", que será una lista de un número de columnas igual al 
# valor de "cols". Luego añadimos al elemento i,j de la lista x, el valor de line[j].

for i in range(rows):
	line = lines[i].split()
	for j in range(cols):
		x[i][j] = float(line[j])

##-------------------------##
### OPCIONES DE ESCRITURA ###
##-------------------------##

## Creamos el archivo donde guardamos la tabla. ##

print ('Enter the name of the file you want to save with the extension.')

b = raw_input()					# mete el nombre del archivo a guardar

out = open(b,'w')				# crea el archivo de nombre 'b' con permisos de escritura

if rows < 11:
	# Escribe en dos columnas |x|y|
	for i in range(rows):
		j = 0					# inicializamos el contador para el bucle while
		while j != cols:
			out.write("$")
			out.write(str(x[i][j]))		# dato
			out.write(" \\pm ")
			out.write(str(x[i][j+1]))	# error dato
			out.write("$")
			j += 2
			if j == cols:
				break
			else:
				out.write(" & ")
		out.write("\\\\")				# salto de linea (en formato latex)
		out.write("\n")
else:
	# Escribe en cuatro columnas |x|y|x|y|
	if (rows%2 == 0):
		for i in range(rows/2):
			j = 0
			while j != cols:
				out.write("$")
				out.write(str(x[i][j]))				# dato
				out.write(" \\pm ")
				out.write(str(x[i][j+1]))			# error dato
				out.write("$ & $")
				out.write(str(x[i+rows/2][j]))		# dato
				out.write(" \\pm ")
				out.write(str(x[i+rows/2][j+1]))	# error dato
				out.write("$")
				j += 2
				if j == cols:
					break
				else:
					out.write(" & ")
			out.write("\\\\")						# salto de linea (en formato latex)
			out.write("\n")
	else:
		for i in range(rows/2):
			j = 0
			while j != cols:
				out.write("$")
				out.write(str(x[i][j]))				# dato
				out.write(" \\pm ")
				out.write(str(x[i][j+1]))			# error dato
				out.write("$ & $")
				out.write(str(x[i+rows/2+1][j]))	# dato
				out.write(" \\pm ")
				out.write(str(x[i+rows/2+1][j+1]))	# error dato
				out.write("$")
				j += 2								# Aumentamos el contador.
				if j == cols:						# Si j = cols, sale del bucle
					break							# si no, escribe el caracter
				else:								# separador de columna.
					out.write(" & ")
			out.write("\\\\")						# salto de linea (en formato latex)
			out.write("\n")

## Cerramos los archivos de lectura y escritura ##

f.close()					# Cerramos el archivo de lectura
out.close()					# Cerramos el archivo de escritura
