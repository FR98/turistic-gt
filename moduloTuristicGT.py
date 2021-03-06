#Autores:
#Maria Fernanda Remis 18024
#Gabriela Garza 18101
#Filiberto Morales 18321
#Andy Castillo 18040
#Francisco Rosal 18676
#25/04/18
#Modulo TuristicGT

import pymongo
#Se crea la conexion con el cliente de Mongo
conexion = pymongo.MongoClient()
#Se establece la base de datos ccon la que se trabaja
db = conexion["turisticgt"]
#Se establecen las colecciones con las que se trabajaran
coleccionLugares = db.lugares
coleccionUsuarios = db.usuariosAdminTuristic
coleccionRecomendaciones = db.recomendaciones

def autenticarCuenta(bdColeccion, user, password):
	#Autenticacion de ingreso
	objeto = bdColeccion.find({'Usuario':str(user)})
	for i in objeto:
		for j in i:
			if j == "Contrasena":
				if i[j] == password:
					return True
				else:
					return False

def iniciarAdminDB():
	#Para db inicial
	usuario = {
		'Nombre': "Admin N", 
		'Apellido': "Admin A", 
		'Usuario': "Admin", 
		'Contrasena': "admin123"
	}
	coleccionUsuarios.insert(usuario)
	return ""

def iniciarRecomendacionesDB():
	#Para db inicial
	lugar = {
			'Departamento': "Guatemala",
			'Categoria': "Restaurante",
			'Nombre': "Pollo Pinulito",
			'Direccion': "Zona 15",
			'Telefono': 12345678,
			'Web': "",
			'Horario': "9:00 a.m. a 8:00 p.m.",
			'Descripcion': "Ofrecen pollo en diferentes presentaciones.",
			'Comentarios':[{
				'Comentario': "Deliciosa comida",
				'Puntuacion': 5
				}
			]
	}
	coleccionRecomendaciones.insert(lugar)
	return ""

def verLugares(categoria, departamento):
	#Muestra los lugares de un departamento y de una categoria
	listaLugares = ""
	for i in coleccionLugares.find({'Departamento':str(departamento)}):
		if i['Categoria'] == categoria:
			listaLugares += str(i['Nombre'])+"\n"
	return listaLugares

def mostrarRecomendaciones():
	#Muestra los lugares de las recomendaciones
	listaLugares = ""
	for i in coleccionRecomendaciones.find():
		listaLugares += str(i['Nombre'])+"\n"
	if listaLugares == "":
		return "Sin recomendaciones"
	else:
		return listaLugares

def mostrarInfoLugar(lugar):
	#Muestra la info de un lugar
	info = ""
	for i in coleccionLugares.find({'Nombre':str(lugar)}):
		info += "\tNombre: "+str(i['Nombre'])+"\n"
		info += "\tDescripcion: "+str(i['Descripcion'])+"\n"
		info += "\tDireccion: "+str(i['Direccion'])+"\n"
		info += "\tTelefono: "+str(i['Telefono'])+"\n"
		info += "\tWeb: "+str(i['Web'])+"\n"
		info += "\tHorario: "+str(i['Horario'])+"\n"
		info += "\n\tCOMENTARIOS\n"
		for j in i['Comentarios']:
			info += "\nComentario: \n\t"+str(j['Comentario'])+"\n"
			info += "Puntuacion: \n\t"+str(j['Puntuacion'])+"/5 estrellas"+"\n"
	return info

def mostrarInfoLugarRecomend(lugar):
	#Muestra la info de un lugar recomendado
	info = ""
	for i in coleccionRecomendaciones.find({'Nombre':str(lugar)}):
		info += "\tNombre: "+str(i['Nombre'])+"\n"
		info += "\tDescripcion: "+str(i['Descripcion'])+"\n"
		info += "\tDireccion: "+str(i['Direccion'])+"\n"
		info += "\tTelefono: "+str(i['Telefono'])+"\n"
		info += "\tWeb: "+str(i['Web'])+"\n"
		info += "\tHorario: "+str(i['Horario'])+"\n"
		info += "\n\tCOMENTARIOS\n"
		for j in i['Comentarios']:
			info += "\nComentario: \n\t"+str(j['Comentario'])+"\n"
			info += "Puntuacion: \n\t"+str(j['Puntuacion'])+"/5 estrellas"+"\n"
	return info

def esDepartamento(dep):
	#Comprueba que el departamento ingresado sea de Guatemala y exista
	departamentos = ["Alta Verapaz", "Baja Verapaz", "Chimaltenango", "Chiquimula", "Peten", "El Progreso", "Quiche", "Escuintla", "Guatemala", "Huehuetenango", "Izabal", "Jalapa", "Jutiapa", "Quetzaltenango", "Retalhuleu", "Sacatepequez", "San Marcos", "Santa Rosa", "Solola", "Suchitepequez", "Totonicapan", "Zacapa"]
	if dep in departamentos:
		return True
	else:
		return False

def siExiste(lugar):
	#Comprueba la existencia de un lugar en la db
	listaLugares = []
	for i in coleccionLugares.find():
		listaLugares.append(i['Nombre'])

	if lugar in listaLugares:
		return True
	else:
		return False

def siExisteRecomend(lugar):
	#Comprueba la existencia de un lugar recomendado en la db
	listaLugares = []
	for i in coleccionRecomendaciones.find():
		listaLugares.append(i['Nombre'])

	if lugar in listaLugares:
		return True
	else:
		return False

def usuarioNuevoValido(user):
	#Comprueba que el usuario nuevo sea valido
	listaUsuarios = []
	for i in coleccionUsuarios.find():
		listaUsuarios.append(i['Usuario'])

	if user in listaUsuarios:
		return False
	else:
		return True

def crearDiccLugar(departamento, categoria, nombre, direccion, telefono, web, horario, descripcion, comentario, puntuacion):
	#Crea un diccionario de la info de un lugar
	lugar = {
		'Departamento': departamento,
		'Categoria': categoria,
		'Nombre': nombre,
		'Direccion': direccion,
		'Telefono': telefono,
		'Web': web,
		'Horario': horario,
		'Descripcion': descripcion,
		'Comentarios':[{
			'Comentario': comentario,
			'Puntuacion': puntuacion
		}]
	}
	return lugar

def crearDiccUser(nombre, apellido, usuario, contrasena):
	#Crea diccionario de un usuario
	user = {
		'Nombre': nombre,
		'Apellido': apellido,
		'Usuario': usuario,
		'Contrasena': contrasena
	}
	return user

def menuInicio():
	#Menu principal
	return """
	Bienvenido a TuristicGT
		MENU:
	1. Consulta
	2. Ingreso Admin
	3. Salir"""

def menuConsulta():
	#Menu consulta
	return """
		MENU CONSULTA:
	1. Departamentos
	2. Recomendar
	3. Regresar"""

def menuCategorias(dep):
	#Menu categorias
	return """
		MENU DEPARTAMENTO """+str(dep.upper())+""":
	1. Restaurantes
	2. Entretenimiento
	3. Regresar"""

def menuComentarios():
	#Menu comentarios
	return """
	1. Ingresar un comentario
	2. Regresar"""

def opcionesComentario():
	#Opciones comentario
	return """
	1. Enviar
	2. Cancelar"""

def opcionesRecomendar():
	#Opciones recomendar
	return """
	1. Enviar
	2. Cancelar"""

def menuIngreso():
	#Menu ingreso
	return """
	1. Entrar
	2. Cancelar"""

def menuAdmin():
	#Menu admin
	return """
		MENU ADMIN:
	1. Departamentos
	2. Ingresar un nuevo lugar
	3. Ver Recomendaciones
	4. Registrar un nuevo admin
	5. Logout"""

def opcionesIngresar():
	#Opciones ingresar
	return """
	1. Ingresar
	2. Cancelar"""

def opcionesRegistrar():
	#Opciones registrar
	return """
	1. Registrar
	2. Cancelar"""