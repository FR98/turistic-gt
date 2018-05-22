#Autores:
#Maria Fernanda Remis 18024
#Gabriela Garza 18101
#Filiberto Morales 18321
#Andy Castillo 18040
#Francisco Rosal 18676
#25/04/18
#Aplicacion TuristicGT

#Se importan modulos
import pymongo
import moduloTuristicGT
import moduloParaDB

#Se crea la conexion con el cliente de Mongo
conexion = pymongo.MongoClient()
#Se establece la base de datos ccon la que se trabaja
db = conexion["turisticgt"]
#Se establecen las colecciones con las que se trabajaran
coleccionLugares = db.lugares
coleccionUsuarios = db.usuariosAdminTuristic
coleccionRecomendaciones = db.recomendaciones

#Ciclo para agregar datos iniciales a base de datos
preguntaDB = "nada"
while (preguntaDB != "si") and (preguntaDB != "no"):
    preguntaDB = input("Es primera vez que inicia este programa en su dispositivo? (si/no) ")
    if preguntaDB == "si":
            confirmar="nada"
            while confirmar!= "si" and confirmar !="no":
                confirmar = input("Esta seguro? Cambiaran sus datos guardados (si/no) ")
                if confirmar == "si":
                        moduloTuristicGT.iniciarAdminDB()
                        moduloParaDB.iniciarLugaresDB()
                elif confirmar == "no":
                        print("Se cancelo la subida de datos")
                else:
                        print("Opcion invalida")
    elif preguntaDB == "no":
        print("Se procedera con el programa como con regularidad")
    else:
        print("Opcion invalida")

menuPantallaInicio = "0"
#Ciclo principal
while menuPantallaInicio != "3":
    #Se llama funcion que imprime menu principal
    print(moduloTuristicGT.menuInicio())
    menuPantallaInicio = input("Opcion: ")
#
#   CONSULTA
#
    if menuPantallaInicio == "1":
        #Consulta
        menuConsulta = "0"
        #Ciclo menu consulta
        while menuConsulta != "3":
            #Se llama funcion que imprime menu consulta
            print(moduloTuristicGT.menuConsulta())
            menuConsulta = input("Opcion: ")
            if menuConsulta == "1":
                #
                #DEPARTAMENTOS
                #
                menuCategorias = "0"
                #Ciclo menu categorias
                while menuCategorias != "3":
                    departamento = input("\nIngrese un departamento: ")
                    if departamento == "Alta Verapaz" or departamento =="Baja Verapaz" or departamento =="Chimaltenango" or departamento =="Chiquimula" or departamento =="Peten" or departamento =="El Progreso" or departamento =="Quiche" or departamento =="Escuintla" or departamento =="Guatemala" or departamento =="Huehuetenango" or departamento =="Izabal" or departamento =="Jalapa" or departamento =="Jutiapa" or departamento =="Quetzaltenango" or departamento =="Retalhuleu" or departamento =="Sacatepequez" or departamento =="San Marcos" or departamento =="Santa Rosa" or departamento =="Solola" or departamento =="Suchitepequez" or departamento =="Totonicapan" or departamento =="Zacapa":
                    #Se llama funcion que imprime menu categorias
                            print(moduloTuristicGT.menuCategorias(departamento))
                            menuCategorias = input("Opcion: ")
                            if (menuCategorias == "1") or (menuCategorias == "2"):
                                #
                                #SELECCIONAR LUGAR
                                #
                                if menuCategorias == "1":
                                    #RESTAURANTES
                                    print("\nRESTAURANTES EN "+str(departamento.upper()+" (BD):"))
                                    print("Ingrese 1 para regresar")
                                    #Funcion mostrar los restaurantes del departamento en la bd
                                    categoria = "Restaurante"
                                    print(moduloTuristicGT.verLugares(categoria, departamento))
                                    lugarElecto = input("Ingrese el nombre del restaurante de su eleccion: ")
                                else:
                                    #ENTRETENIMIENTO
                                    print("\nENTRETENIMIENTO EN "+str(departamento.upper()+" (BD):"))
                                    print("Ingrese 1 para regresar")
                                    #Funcion mostrar los lugares de entretenimiento del departamento en la bd
                                    categoria = "Entretenimiento"
                                    print(moduloTuristicGT.verLugares(categoria, departamento))
                                    lugarElecto = input("Ingrese el nombre del lugar de su eleccion: ")
                                #
                                #MOSTRAR INFORMACION DEL LUGAR
                                #
                                if lugarElecto == "1":
                                    #Regresar
                                    print("")
                                elif lugarElecto != "1":
                                    #Se muestra la info del lugar electo
                                    print("\nINFORMACION DEL LUGAR "+str(lugarElecto.upper())+":")
                                    #Funcion de mostrar la info del lugar
                                    print(moduloTuristicGT.mostrarInfoLugar(lugarElecto))
                                    menuComentarios = "0"
                                    #Ciclo menu comentarios
                                    while (menuComentarios != "1") and (menuComentarios != "2"):
                                        #Se llama funcion que imprime menu comentarios
                                        print(moduloTuristicGT.menuComentarios())
                                        menuComentarios = input("Opcion: ")
                                        if menuComentarios == "1":
                                            print("\nSU COMENTARIO:")
                                            coment = input("Ingrese su comentario: ")
                                            puntuacion = input("Ingrese la puntuacion del lugar (sobre 5): ")
                                            try:
                                                    float(puntuacion)
                                                    puntuacion=float(puntuacion)
                                                    if puntuacion >= 0 and puntuacion <6:
                                                    #Se crea diccionario comentario
                                                            comentario = {
                                                                        'Comentario': coment,
                                                                        'Puntuacion': puntuacion
                                                                        }
                                                            opcionesComentario = "0"
                                                            #Ciclo opciones comentario
                                                            while (opcionesComentario != "1") and (opcionesComentario != "2"):
                                                                #Se llama funcion que imprime las opciones de comentario
                                                                print(moduloTuristicGT.opcionesComentario())
                                                                opcionesComentario = input("Opcion: ")
                                                                if opcionesComentario == "1":
                                                                    #Se inserta el comentario en la base de datos
                                                                    for i in coleccionLugares.find({'Nombre':str(lugarElecto)}):
                                                                        comentarios = i['Comentarios']
                                                                        comentarios.append(comentario)
                                                                        coleccionLugares.update_one({"Nombre":lugarElecto},{"$set":{"Comentarios": comentarios}})
                                                                    print("Enviado correctamente")
                                                                elif opcionesComentario == "2":
                                                                    print("El envio se cancelo correctamente")
                                                                else:
                                                                    print("Opcion Invalida")
                                                    else:
                                                        print("Califique de 0 a 5")
                                            except:
                                                    print("Escriba un numero")

                                        elif menuComentarios == "2":
                                            #Regresar
                                            print("")
                                        else:
                                            print("Opcion Invalida")
                                            
                            elif menuCategorias == "3":
                                #Regresar
                                print("")
                            else:
                                print("Opcion Invalida")
                    else:
                        print("Departamento invalido")

            elif menuConsulta == "2":
                #
                #RECOMENDAR
                #
                print("")
                departamento = input("Ingrese un departamento: ")
                if departamento == "Alta Verapaz" or departamento =="Baja Verapaz" or departamento =="Chimaltenango" or departamento =="Chiquimula" or departamento =="Peten" or departamento =="El Progreso" or departamento =="Quiche" or departamento =="Escuintla" or departamento =="Guatemala" or departamento =="Huehuetenango" or departamento =="Izabal" or departamento =="Jalapa" or departamento =="Jutiapa" or departamento =="Quetzaltenango" or departamento =="Retalhuleu" or departamento =="Sacatepequez" or departamento =="San Marcos" or departamento =="Santa Rosa" or departamento =="Solola" or departamento =="Suchitepequez" or departamento =="Totonicapan" or departamento =="Zacapa":
                        categoria = input("Ingrese Restaurante o Entretenimiento: ")
                        if categoria== "Restaurante" or categoria== "Entretenimiento":
                                nombre = input("Ingrese el nombre del lugar: ")
                                direccion = input("Ingrese la direccion: ")
                                telefono = input("Ingrese el telefono del lugar: ")
                                if len(telefono)==8:
                                    try:
                                        int(telefono) 
                                        web = input("Ingrese la pagina web: ")
                                        horario = input("Ingrese el horario de servicio: ")
                                        descripcion = input("Ingrese la descripcion del lugar: ")
                                        comentario = input("Ingrese un comentario del lugar: ")
                                        puntuacion = input("Ingrese la puntuacion del lugar (sobre 5): ")
                                        
                                        try:
                                            float(puntuacion)
                                            puntuacion=float(puntuacion)
                                            if puntuacion >= 0 and puntuacion <6:
                                                #Se crea diccionario del lugar con funcion
                                                lugar = moduloTuristicGT.crearDiccLugar(departamento, categoria, nombre, direccion, telefono, web, horario, descripcion, comentario, puntuacion)

                                                opcionesRecomendar = "0"
                                                    #Ciclo opciones recomendar
                                                while (opcionesRecomendar != "1") and (opcionesRecomendar != "2"):
                                                    #Se llama funcion que imprime las opciones de recomendar
                                                    print(moduloTuristicGT.opcionesRecomendar())
                                                    opcionesRecomendar = input("Opcion: ")
                                                    if opcionesRecomendar == "1":
                                                    #Se inserta el lugar en la base de datos de recomendaciones
                                                        coleccionRecomendaciones.insert(lugar)
                                                        print("Enviado correctamente.")
                                                    elif opcionesRecomendar == "2":
                                                        print("El envio se cancelo.")
                                                    else:
                                                        print("Opcion Invalida.")
                                            else:
                                                print("Califique de 0 a 5")
                                        except:
                                            print("No es numero")
                                    except:
                                        print("Escriba solo numeros")
                                else:
                                    print("El telefono debe tener 8 digitos")
                        else:
                            print("Categoria invalida")
                else:
                    print("Departamento invalido")
                
            elif menuConsulta == "3":
                #Regresar al menu principal
                print("")
            else:
                print("Opcion Invalida")
#
#INGRESO ADMIN
#
    elif menuPantallaInicio == "2":
        #INGRESO ADMIN
        usuario = input("\nIngrese su usuario: ")
        contrasena = input("Ingrese su contrasena: ")
        menuIngreso = "0"
        #Ciclo menu ingreso admin
        while (menuIngreso != "1") and (menuIngreso != "2"):
            #Se llama funcion que imprime menu ingreso
            print(moduloTuristicGT.menuIngreso())
            menuIngreso = input("Opcion: ")

            if menuIngreso == "1":
                #Autenticacion de ingreso
                autenticado = moduloTuristicGT.autenticarCuenta(coleccionUsuarios, usuario, contrasena)
                if autenticado:
                    while autenticado:
                        #Autenticacion valida
                        print("\n\tBIENVENIDO "+str(usuario.upper()))
                        #Se llama funcion que imprime menu admin
                        print(moduloTuristicGT.menuAdmin())
                        menuAdmin = input("Opcion: ")
                        if menuAdmin == "1":
                            #
                            #DEPARTAMENTOS
                            #
                            menuCategorias = "0"
                            #Ciclo menu categorias
                            while menuCategorias != "3":
                                departamento = input("\nIngrese un departamento: ")
                                #Se llama funcion que imprime menu categorias
                                print(moduloTuristicGT.menuCategorias(departamento))
                                menuCategorias = input("Opcion: ")
                                if (menuCategorias == "1") or (menuCategorias == "2"):
                                    #
                                    #SELECCIONAR LUGAR
                                    #
                                    if menuCategorias == "1":
                                        #RESTAURANTES
                                        print("\nRESTAURANTES EN "+str(departamento.upper()+" (BD):"))
                                        print("Ingrese 1 para regresar")
                                        #Funcion mostrar los restaurantes del departamento en la bd
                                        categoria = "Restaurante"
                                        print(moduloTuristicGT.verLugares(categoria, departamento))
                                        lugarElecto = input("Ingrese el nombre del restaurante de su eleccion: ")
                                    else:
                                        #ENTRETENIMIENTO
                                        print("\nENTRETENIMIENTO EN "+str(departamento.upper()+" (BD):"))
                                        print("Ingrese 1 para regresar")
                                        #Funcion mostrar los lugares de entretenimiento del departamento en la bd
                                        categoria = "Entretenimiento"
                                        print(moduloTuristicGT.verLugares(categoria, departamento))
                                        lugarElecto = input("Ingrese el nombre del lugar de su eleccion: ")
                                    #
                                    #MOSTRAR INFORMACION DEL LUGAR
                                    #
                                    if lugarElecto == "1":
                                        #Regresar
                                        print("")
                                    elif lugarElecto != "1":
                                        #Se muestra la info del lugar electo
                                        print("\nINFORMACION DEL LUGAR "+str(lugarElecto.upper())+":")
                                        #Funcion de mostrar la info del lugar
                                        print(moduloTuristicGT.mostrarInfoLugar(lugarElecto))
                                        
                                elif menuCategorias == "3":
                                    #Regresar
                                    print("")
                                else:
                                    print("Opcion Invalida")

                        elif menuAdmin == "2":
                            #
                            #INGRESAR UN NUEVO LUGAR
                            #
                            print("")
                            departamento = input("Ingrese un departamento: ")
                            categoria = input("Ingrese Restaurante o Entretenimiento: ")
                            nombre = input("Ingrese el nombre del lugar: ")
                            direccion = input("Ingrese la direccion: ")
                            telefono = input("Ingrese el telefono del lugar: ")
                            web = input("Ingrese la pagina web: ")
                            horario = input("Ingrese el horario de servicio: ")
                            descripcion = input("Ingrese la descripcion del lugar: ")
                            comentario = ""
                            puntuacion = ""
                            #Se crea diccionario del lugar con funcion
                            lugar = moduloTuristicGT.crearDiccLugar(departamento, categoria, nombre, direccion, telefono, web, horario, descripcion, comentario, puntuacion)

                            opcionesIngresar = "0"
                            #Ciclo opciones ingresar
                            while (opcionesIngresar != "1") and (opcionesIngresar != "2"):
                                #Se llama funcion que imprime las opciones de ingresar
                                print(moduloTuristicGT.opcionesIngresar())
                                opcionesIngresar = input("Opcion: ")
                                if opcionesIngresar == "1":
                                    #Se inserta el lugar en la base de datos
                                    coleccionLugares.insert(lugar)
                                    print("Ingresado correctamente.")
                                elif opcionesIngresar == "2":
                                    print("El ingreso se cancelo.")
                                else:
                                    print("Opcion Invalida.")

                        elif menuAdmin == "3":
                            #
                            #VER RECOMENDACIONES
########################    #

                            print("Error #404. Pagina en construccion.")
                        elif menuAdmin == "4":
                            #
                            #REGISTRAR UN NUEVO ADMIN
                            #
                            print("")
                            nombre = input("Ingrese el nombre: ")
                            apellido = input("Ingrese el apellido: ")
                            usuario = input("Inngrese el usuario: ")
                            contrasena = input("Ingrese la contrasena: ")
                            user = moduloTuristicGT.crearDiccUser(nombre, apellido, usuario, contrasena)

                            opcionesRegistrar = "0"
                            #Ciclo opciones registrar
                            while (opcionesRegistrar != "1") and (opcionesRegistrar != "2"):
                                #Se llama funcion que imprime las opciones de registrar
                                print(moduloTuristicGT.opcionesRegistrar())
                                opcionesRegistrar = input("Opcion: ")
                                if opcionesRegistrar == "1":
                                    #Se inserta el usuario en la base de datos
                                    coleccionUsuarios.insert(user)
                                    print("Registrado correctamente.")
                                elif opcionesRegistrar == "2":
                                    print("El registro se cancelo.")
                                else:
                                    print("Opcion Invalida.")

                        elif menuAdmin == "5":
                            #Logout
                            autenticado = False
                            print("\n\tHASTA LA PROXIMA "+str(usuario.upper()))
                        else:
                            print("Opcion Invalida")

                else:
                    print("\nUsuario o Contrasena incorrectos.")

            elif menuIngreso == "2":
                print("")
            else:
                print("Opcion Invalida")

    elif menuPantallaInicio == "3":
        #Salir
        print("Adios")
    else:
        print("Opcion invalida")
