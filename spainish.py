#!/usr/bin/python
#coding: utf-8
import random, locale
#crete a list of diffrent words and make them appear random
def words():
	i = 0
	
	objects = ['la lampara', 'la pizarra', 'el pared', 'la siela', 'la ventana' , 'la puerta', 'el techo', 'el suelo', 'la bolígrafo', 'el libro',
	'la messa', 'el profesor'	'el medico', 'el estudiante', 'el ingeniero', 'el peluquero', 'la enfermera', 'la secrtaria', 'el camarero',
	'el sombrero', 'el vino', 'el perro', 'el cafe', 'el jerzz']
	
	english_tran = ['la lampra = light', 'la pizarra = black board', 'el pared = wall', 'la siela = seat', 'la ventana = window', 'la puerta = door',
	'el techo = roof', 	'el suelo = floor', 'el bolígrafo = pen', 'el libro = book', 'el profesor = teacher', 'el medico = doctor', 'el estudiante = student',
	'el ingeniero = engineer', 'el peluquero = barber/haridresser', 'la enfermera = nurse', 'la secrtaria = secrutiry', 'el sombrero = hat', 
	'el vino = wine', 'el perro = dog', 'el cafe = the coffee', 'el jerzz =  sherry', 'el camarero = waiter', 'la mesa = table']
	
	days = ['lunes', 'martes', ' miécoles', 'Jueves', 'viernes', 'scibado', 'Domingo']
	
	food = ['pescado', 'ensalada', 'tortilla de patates', 'paella', 'tapas', 'pollo', 'carne']
	
	connecting_words = ['Essuchar', 'pintar', 'llaver', 'fumar', 'preparar', 'lavar', 'nadar', 'pasear', 'tocar', 'trabja', 'estuiar', 'cuntar', 'beber', 'coaer', 'coser', 'ver', 'leer', 'correr', 'vender', 'repartir', 'abrir', 'compartir', 'cubrir', 'sufair']
	
	conect_engish = ['Essuchar = listen', 'pintar = paint', 'llevar = carry', 'fumar = smoke', 'preparar = prepare', 'lavar = wash', 'nadar = swim',
	'pasear = move', 'tocar = play', 'trabjar = relaxing walk', 'estuiar = study', 'cuntar = sing', 'beber = drink', 'coaer', 'coser = saw', 'ver= seeing', 'leer = read', 'correr = run', 'vender = sell', 'repartir', 'abrir', 'compartir', 'cubrir', 'sufair']
	
	while i < 50:
		print random.choice(days)
		raw_input('')
		print random.choice(food)
		raw_input('')
		print random.choice(connecting_words)
		raw_input('')
		print random.choice(objects)
		raw_input('')
		i = i + 1
def phrases():
	day_of_the_week = ['los Lunes comcmos pescado #mondays eat fish', 'los Martes comemos ensalada #tuesdays eat salad', 'los miercole comemos tortilla and de pattates #wednesdays eat tortia with patatoes',	'los Jueves comemos paella #thursdays eat pella', 'los Viernes comemos tapas #fridays eat tapas', 'los Scibados comemos pollo #saturdays eat chicken', 'los Dimingos comomos carne #sundays eat meat']
	other_phrases = ['el profesor repartir los examenes a los estudiantes #the teacher allocates the exams to the students', 'Juan abre la ventana = yuan opens the window', 'luis y manalo wmparteu un apartamento = lous and manlo work together in the aprtement', 'el hino atre la puerta = the man opens the door', ' marrie cubre la mesa con un mantel = marea covers the table with the a cloth', 'juan es sufre mucho = juan is ill', 'el cafe es barato = the coffe is cheap', 'el jerez es caro = the sherry is expensive', 'joun es alto = joun is tall', 'pedro es bajo = pedro is fat', 'perdro toca la gutarra = pedro plays the gutair', 'la enformera trabaja e el hospital = the nurse works in the hospital', 'ellos cantan una cancion = they sing a song', 'pedro estudia en la universidad = pedro studys at the  university', 'Isebella preparao la comida = isbella prepers the food', 'ana lava la rope = ana cleans the   cloths', 'los ninos nadan en el rio = the boys swim in the river', 'la guente pasea eu el parque = a gental walk in the park', 'los senores essuchan la radio = the senores listen to the radio', 'maria pintain cuadro = maria paint a picture', 'oedro lleva una maleta', 'juan fuma un cigarrio', 'antonio es estudente = antonio is a student', 'manuel es ingeniro = manuel is a engineer', 'pedro es profesor = perdor is a profesor', ' carlos es medico = carlos is a doctor', 'meria es secretaria = meria is a secruitery', 'luis es peuquero = louis is a barber', 'carmen es enfermera = carmen is a nurse', 'miguel es arqutecto = miiguel is a arcitect', 'el sombreo es viejo = the hat is old', 'el libro es nuevo = the book is new', 'el vino es bueno = the wine is good', 'el perro malo = the dog is bad', 'el camarero es delgado = the waiter is thin', 'el medico es gardo = the doctor is fat', 'pedro beben cerveza en el bar = pedro driks beer at the bar', 'maria coge naranjas en el jardin = maria picks oranges in the garden', 'los ninos ven la pelicula en el cine = the boys watch a film in the cinema', 'los ninos leen beccian en la clase = the children read in class together', 'el senor leen deperiodico el salon = the man reads newsparer in the living room', 'los deportistas correr la pista= the athlets run in the race', 'maría vende libros en la librería = maria sells books in the libbary']
	i = 0 
	while i < 100:
		print random.choice(day_of_the_week)
		raw_input('')
		print random.choice(other_phrases)
		raw_input('')
		i = i + 1
def numbers():
	nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
	numbers = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce', 'tuece', 'catorce', 'quince', 'dieciseis', 'diecisiete', 'dieciocho', 'diecineve', 'veinte']
	i = 0
	while i <=50:
		print random.choice(nums)
		raw_input('')
		print random.choice(numbers)
		raw_input('')

def pronouns():
	words = ['Essuchar', 'pintar', 'llaver', 'fumar', 'preparar', 'lavar', 'nadar', 'pasear', 'tocar', 'estuiar', 'cuntar', 'beber', 'coaer', 'coser', 'ver', 'leer', 'correr', 'vender', 'repartir', 'abrir', 'compartir', 'cubrir', 'sufair']
	print 'say/write the diffrent types of people\n'
	i = 0 
	while i <=10:
		words = random.choice(words)
		print 'word is ' + word 	
		print 'yo\n'
		print 'tu\n'
		print 'el, la, ustead\n'
		print 'nostros/nostras\n'
		print 'vosotros/vostras\n'
		print 'ellos, ellas, ustedes\n'
	
	
z = random.randint(1,20)
if z <= 5:
	phrases()
	words()
	numbers()
	pronouns()
elif z >= 10:
	numbers()
	words()
	pronouns()
	phrases()
elif z >=15:
	words()
	pronouns()
	phrases()
	numbers()
else:
	pronouns()
	words()
	numbers()
	phrases() 
