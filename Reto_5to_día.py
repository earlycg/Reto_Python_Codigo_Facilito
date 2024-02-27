# Variables con datos de control:
id_list_usuario = []

tabla = {1: {'Nombre (s)': 'Early Start', 'Apellidos': 'Buelvas Buelvas', 'Numero de teléfono': '3107429977', 'correo_electrónico': 'earlystartcg@gmail.com'}, 2: {'Nombre (s)': 'Key Osorio', 'Apellidos': 'Carrillo Beltran', 'Numero de teléfono': '3240943486', 'correo_electrónico': 'emosolito@mail.com'}}

salir = 'no'

def new_user():
    id_usuario = 3
    
    # Entrada para calcular cuántos usuarios se registrarán previamente:
    cantidad_usuarios = 0
    while cantidad_usuarios != 'exit':
        
        cantidad_usuarios = input('Introduce la cantidad de nuevos usuarios que deseas registrar o digita (exit) para salir:\n>').lower().strip()
        
        if cantidad_usuarios == 'exit':
            break
        elif cantidad_usuarios != 'exit':
            cantidad_usuarios = int(cantidad_usuarios)

    #   Bucle para iterar entrada de datos por cantidad de usuarios.
        for i in range(cantidad_usuarios):
            print(f'Usuario {i + 1} Id {id_usuario}')
# Nombres entrada - Bucle y condicional.
            while True:        
                nombres = input('Ingrese su Nombre(S)\n>').title().strip()
                if 2 <= len(nombres) <= 20 and nombres.replace(" ", "").isalpha():    
                    print("¡Entrada válida!")
                    break
                else:
                    print("La entrada no cumple con los requisitos. Inténtelo nuevamente.")

# Apellidos entrada - Bucle y condicional.
            while True: 
                apellidos = input('Ingrese sus Apellidos\n>').title().strip()
                if 6 <= len(apellidos) <= 25 and apellidos.replace(" ", "").isalpha():
                    print("¡Entrada válida!")
                    break
                else:
                    print("La entrada no cumple con los requisitos. Inténtelo nuevamente.")

# Teléfono entrada - Bucle y condicional
            while True:     
                numero_de_telefono = input('Ingrese su numero telefónico\n>').strip()
                
                if 7 <= len(numero_de_telefono) <= 20 and numero_de_telefono.isdigit():
                    print("¡Entrada válida!")
                    break
                else:
                    print("La entrada no cumple con los requisitos. Inténtelo nuevamente.")

# Correo entrada - Bucle y condicional
            while True: 
                correo_electronico = input('Ingrese su correo electrónico\n>').lower().strip()

            # Verificar longitud y que no contenga espacios
                if 7 <= len(correo_electronico) <= 30 and not correo_electronico.isspace():
                    print("¡Entrada válida!")
                    break
                else:
                    print("La entrada no cumple con los requisitos. Inténtelo nuevamente.")



# Recolección de todos los datos en un Diccionario clave valor.
            usuario = {'Nombre (s)': nombres, 'Apellidos': apellidos, 'Numero de teléfono': numero_de_telefono, 'correo_electrónico': correo_electronico}
            tabla[id_usuario] = usuario  # Uso directo del ID como clave

            print(tabla)  # Tabla final
            id_usuario += 1

def show_user():

    while True: # Menu inicio y Validación
        option = input(f"""
    Ingresa un numero (#).
    (1) Para consultar por el ID del usuario.
    (2) Para consultar por el Nombre del usuario.
    (3) Para consultar por el Apellidos del usuario.
    (4) Para consultar por el Teléfono del usuario.
    (5) Para consultar por el Correo del usuario.
    (exit) Para Salir X:\n> """).lower().strip()

        if option == 'exit':
            print('Fin de la consulta.')
            break  # Salir del bucle while
        else:
            option = int(option)
            try:
                match option:
                    case 1: # Por ID
                        inp_id = input('Digite el ID del usuario a encontrar:\n>')
                        id = int(inp_id)
                        if id in tabla:  # condicional para verificar si el Id ingresado se encuentra en la lista                                                
                            cosulta = tabla[id]
                            print(f"{id}: {cosulta}")
                        else:
                            print(f'El ID #{inp_id} no se encuentra en nuestra base de datos.')                            
                    case 2:
                        inp_nombre = input('Digite el nombre(s) del usuario a encontrar:\n>')
                        if inp_nombre in tabla:  # condicional para verificar si el nombre ingresado se encuentra en la lista                                                
                            cosulta = tabla['Nombre (s)']
                            print(f"{inp_nombre}: {cosulta}")
                        else:
                            print(f'El ID #{inp_nombre} no se encuentra en nuestra base de datos.')
                    case 3:
                        apellidos = input('Digite los apellidos del usuario a encontrar:\n>')
                    case 4:
                        telefono = input('Digite el telefono del usuario a encontrar:\n>')
                    case 5:
                        correo = input('Digite el correo del usuario a encontrar:\n>')
                    case _:
                            print(f"La opción {option} no es válida. Las opciones válidas son 1, 2, 3, 4, 5 o 'exit'")
            except ValueError:
                print(f"Ingresa un número válido o (exit) Para Salir.\n{option} No es una entrada valida.")

def edit_user():
    ID_a_modificador = 0
    while ID_a_modificador != 'exit':
        ID_a_modificador = input(f'ingrese el ID del usuario que desea modificar o (exit) para salir').lower().strip()
        if ID_a_modificador == 'exit':
            break
        else:
            ID_a_modificador = int(ID_a_modificador)
            
            if ID_a_modificador in tabla:  # condicional para verificar si el Id ingresado se encuentra en la lista                                                
                cosulta = tabla[ID_a_modificador]
                print(f"{ID_a_modificador}: {cosulta}")
            else:
                print(f'El ID #{ID_a_modificador} no se encuentra en nuestra base de datos.')   

        inp_comparador = input('Digite con un numero el campo que desea modificar (1) si es Nombres, (2) si es Apellidos, (3) si es Numero de Teléfono, (4) si es Correo Electrónico o (EXIT) si deseas salir: ').lower().strip()

        if inp_comparador == 'exit':
            break

        inp_comparador = int(inp_comparador)

        if inp_comparador in [1, 2, 3, 4]:
            campo_modificar = list(usuario_encontrado.keys())[inp_comparador - 1]
            nuevo_valor = input(f'Actualice el campo "{campo_modificar}" del usuario {usuario_encontrado}: ')
            tabla[id_consulta][campo_modificar] = nuevo_valor
            print('¡Campo actualizado!')
            print(tabla[id_consulta])
        else:
            print('Entrada no válida. Por favor, ingrese una opción válida.')

def delete_user():
    id_a_eliminar = input('Ingresa el ID del usuario que deseas eliminar:\n>')
    id_a_eliminar = int(id_a_eliminar)
    usuario_eliminado = tabla.pop(id_a_eliminar)

    print(f'ID {id_a_eliminar}')
    print(f'El valor eliminado es: {usuario_eliminado}')

def list_user():
    pass

# Menu Inicial:
while True: # Menu inicio y Validación
    option = input(f"""
Ingresa un numero (#).
(1) Para ingresar un nuevo usuario.
(2) Para ver un usuario.
(3) Para editar un usuario.
(4) Para eliminar usuario.
(5) Para listar un usuario.
(exit) Para Salir X.
> """).lower().strip()

    if option == 'exit':
        print('Fin del programa, hasta pronto!')
        break  # Salir del bucle while
    else:
        try:
            option = int(option)

            match option:
                case 1:
                    new_user()
                case 2:
                    show_user()
                case 3:
                    edit_user()
                case 4:
                    delete_user()
                case 5:
                    list_user()
                case _:
                    print(f"La opción {option} no es válida. Las opciones válidas son 1, 2, 3, 4, 5 o 'exit'")
        except ValueError:
            print(f"Ingresa un número válido o (exit) Para Salir.\n{option} No es una entrada valida.")
