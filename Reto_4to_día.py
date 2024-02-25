# Entrada para calcular cuántos usuarios se registrarán previamente:
cantidad_usuarios = input('Introduce la cantidad de nuevos usuarios quieres registrar o digita (exit) para salir:\n>').lower()


# Variables con datos de control:
min_caracteres = 5
max_caracteres = 50
max_Tel = 10
id_usuario = 0
id_list_usuario = []
tabla = {}
salir = 'no'

if cantidad_usuarios != 'exit':
    cantidad_usuarios = int(cantidad_usuarios)

#   Bucle para iterar entrada de datos por cantidad de usuarios.
    for i in range(cantidad_usuarios):
        print(f'Usuario {i + 1}')
        
    # Bucle y condicional para la entrada del nombre + regulación de max y min de caracteres ingresados.
        while True:        
            nombres = input('Ingrese su Nombre(S)\n>')
            if min_caracteres <= len(nombres) <= max_caracteres:
                print("¡Entrada válida!")
                break
            else:
                print("La entrada no cumple con los requisitos. Inténtelo nuevamente.")
        
        # Bucle y condicional para la entrada del apellidos + regulación de max y min de caracteres ingresados
        while True: 
            apellidos = input('Ingrese sus Apellidos\n>')
            
            if min_caracteres <= len(apellidos) <= max_caracteres:
                print("¡Entrada válida!")
                break
            else:
                print("La entrada no cumple con los requisitos. Inténtelo nuevamente.")
        
        # Bucle y condicional para la entrada del teléfono + regulación de max y min de caracteres ingresados
        while True:     
            numero_de_telefono = input('Ingrese su numero telefónico\n>')
            
            if min_caracteres <= len(numero_de_telefono) <= max_Tel:
                print("¡Entrada válida!")
                break
            else:
                print("La entrada no cumple con los requisitos. Inténtelo nuevamente.")

        # Bucle y condicional para la entrada del correo electrónico + regulación de max y min de caracteres ingresados
        while True: 
            correo_electronico = input('Ingrese su correo electrónico\n>')

            if min_caracteres <= len(correo_electronico) <= max_caracteres:
                print("¡Entrada válida!")
                break
            else:
                print("La entrada no cumple con los requisitos. Inténtelo nuevamente.")

        # Suma para control de bucle
        id_usuario += 1

        # recolección de todos los datos en un Diccionario clave valor.
        usuario = {'Nombre (s)': nombres, 'Apellidos': apellidos, 'Numero de teléfono': numero_de_telefono, 'correo_electrónico': correo_electronico}
        tabla[id_usuario] = usuario  # Uso directo del ID como clave

        print(tabla)  # Tabla final

#   Modulo de consulta de ID o modificación de usuario:
    id_consulta = int(input('Ingrese el Numero ID del usuario a consultar o modificar: '))  # Variable y entrada de usuario

    if id_consulta in tabla:  # condicional para verificar si el Id ingresado se encuentra en la lista
        usuario_encontrado = tabla[id_consulta]
        nombre_de_usurio = tabla[id_consulta]['Nombre (s)']
        print(f'El ID #{id_consulta} pertenece al usuario: {nombre_de_usurio}\n{usuario_encontrado}\nDesea modificarlo?\n:> ')

#   Modificar información de la base de datos
        while salir == 'no':
            acceso_a_modificador = input(f'Digita 1 si deseas modificar la información de {nombre_de_usurio} o "EXIT" si deseas salir: ').lower()

            if acceso_a_modificador == 'exit':
                break
            elif acceso_a_modificador == '1':
                inp_comparador = input('Digite con un numero el campo que desea modificar (1) si es Nombres, (2) si es Apellidos, (3) si es Numero de Teléfono, (4) si es Correo Electrónico o (EXIT) si deseas salir: ').lower()

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
            else:
                print('Entrada no válida. Por favor, ingrese una opción válida.')
    else:
        print(f'El ID #{id_consulta} no se encuentra en nuestra base de datos.')
else:
    print('Programa finalizado')
