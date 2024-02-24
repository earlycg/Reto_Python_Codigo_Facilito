cantidad_usuarios = int(input('Cuantos nuevos usuarios quieres registrar:\n>'))

min_caracteres = 5
max_caracteres = 50
max_Tel = 10
id_usuario = 0
id_list_usuario = []

for i in range(cantidad_usuarios):
    print(f'Usuario {i + 1}')
    
    
        
    while True:        
        nombres = input('Ingrese su Nombre(S)\n>')

        if min_caracteres <= len(nombres) <= max_caracteres:
            print("¡Entrada válida!")
            break
        else:
            print("La entrada no cumple con los requisitos. Inténtelo nuevamente.")

    while True: 
        apellidos = input('Ingrese sus Apellidos\n>')
        
        if min_caracteres <= len(apellidos) <= max_caracteres:
            print("¡Entrada válida!")
            break
        else:
            print("La entrada no cumple con los requisitos. Inténtelo nuevamente.")
            
    while True:     
        numero_de_telefono = input('Ingrese su numero telefónico\n>')
        
        if min_caracteres <= len(numero_de_telefono) <= max_Tel:
            print("¡Entrada válida!")
            break
        else:
            print("La entrada no cumple con los requisitos. Inténtelo nuevamente.")
        
    while True: 
        correo_electronico = input('Ingrese su correo electrónico\n>')
        
        if min_caracteres <= len(correo_electronico) <= max_caracteres:
            print("¡Entrada válida!")
            
            break
            
        else:
            print("La entrada no cumple con los requisitos. Inténtelo nuevamente.")
    
    id_usuario += 1
    
    id_name = f'id|{id_usuario}| {nombres} {apellidos} | {numero_de_telefono} | {correo_electronico}'
    
    
    id_list_usuario.append(id_name)
    
    
    # Imprimir la información del usuario después de validar todas las entradas
    print(f'\nNombre: {nombres} \nApellidos: {apellidos} \nNumero de teléfono: {numero_de_telefono} \nCorreo electrónico: {correo_electronico}\n')

for elemento in (id_list_usuario):
    print(elemento)
