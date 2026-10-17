"""Sistema de gestión de una biblioteca"""

# print("Libros disponibles")
print("-----------------------")
libro1 = {
    "titulo" : "El principe",
    "autor" : "Natanael sanches",
    "publicacion" : 1984,
    "copias" : 6,
    "categoria" : "novelas"
}

libro2 = {
    "titulo" : "Los moqueteros",
    "autor" : "Domingo porte",
    "publicacion" : 1897,
    "copias" : 5,
    "categoria" : "infantil"
}

libro3 = {
    "titulo" : "El mal rojo",
    "autor" : "Daniel gomes",
    "publicacion" : 1998,
    "copias" : 3,
    "categoria" : "adultos"
}

libro4 = {
    "titulo" : "las maravillas",
    "autor" : "Ramon jose",
    "publicacion" : 1865,
    "copias" : 8,
    "categoria" : "educativos"
}

libro5 = {
    "titulo" : "la mardicion",
    "autor" : "Manuel rojas",
    "publicacion" : 1999,
    "copias" : 4,
    "categoria" : "juvenil"
}

libros = [libro1, libro2, libro3, libro4, libro5]

# for libro in libros:
#     print("Título:", libro["titulo"])
#     print("Autor:", libro["autor"])
#     print("pubricacion:", libro["publicacion"])
#     print("copias:", libro["copias"])
#     print("categdoria:", libro["categoria"])

#     print("------------------------------")

#Datos del usuario
nombre = input("Deme su nombre: ")
edad = int(input("Deme su edad: "))
print("Bienvenido a la biblioteca,", nombre)

# if edad < 12:
#     print("solo puede ver y pedir libros de la categoría “infantil”")
# elif edad >= 12 and edad <= 17:
#     print("no puede acceder a los de la categoría “adultos”")
# else:
#     print("tiene acceso a todo")

prestados = []
multa_total = 0
MULTA_POR_DIA = 30
DIAS_PERMITIDOS = 7

while True:
    print("--- MENÚ DE LA BIBLIOTECA ---")
    print("1. Ver libros disponibles")
    print("2. Buscar un libro")
    print("3. Pedir prestado un libro")
    print("4. Devolver un libro")
    print("5. Salir")

    opcion = input("seleccione una opcion: ")

    if opcion == "1":
        for libro in libros:
            if libro["copias"] > 0:
                if edad < 12 and libro["categoria"] != "infantil":
                    continue
                if 12 <= edad < 18 and libro["categoria"] == "adultos":
                    continue

                print("Título:", libro["titulo"])
                print("Autor:", libro["autor"])
                print("Publicación:", libro["publicacion"])
                print("Copias:", libro["copias"])
                print("Categoría:", libro["categoria"])
                print("-------------------------------")

                if libro["copias"] == 1:
                    print("¡Solo queda una copia!")

    elif opcion == "2":
        titulo = input("Escribe el título del libro: ").strip()
        encontrado = False

        for libro in libros:
            if libro["titulo"].lower() == titulo.lower():
                encontrado = True

                if edad < 12 and libro["categoria"] != "infantil":
                    print("No tienes permiso para ver este libro.")
                elif 12 <= edad < 18 and libro["categoria"] == "adultos":
                    print("No tienes permiso para ver este libro.")
                else:
                    print("Título:", libro["titulo"])
                    print("Autor:", libro["autor"])
                    print("Publicación:", libro["publicacion"])
                    print("Copias:", libro["copias"])
                    print("Categoría:", libro["categoria"])
                break

        if not encontrado:
            print("El libro no existe.")

    elif opcion == "3":

        if multa_total > 0:
            print("No puedes cojer un libro prestado tienes una multa")
        else:
            titulo = input("¿Qué libro deseas pedir prestado?: ").strip()
            encontrado = False

            for libro in libros:
                if libro["titulo"].lower() == titulo.lower():
                    encontrado = True

                    if libro in prestados:
                        print("Ya tienes ese libro prestado.")
                    elif len(prestados) >= 3:
                        print("No puedes pedir más de 3 libros.")
                    elif libro["copias"] <= 0:
                        print("No hay copias disponibles.")
                    elif edad < 12 and libro["categoria"] != "infantil":
                        print("Solo puedes pedir libros infantiles.")
                    elif 12 <= edad < 18 and libro["categoria"] == "adultos":
                        print("No puedes pedir libros para adultos.")
                    else:
                        prestados.append(libro)
                        libro["copias"] -= 1
                        print("Libro prestado correctamente.")

                        if libro["copias"] == 1:
                            print("¡Solo queda una copia!")
                    break

            if not encontrado:
                print("El libro no existe.")

    elif opcion == "4":
        titulo = input("¿Qué libro deseas devolver?: ")
        encontrado = False

        for libro in prestados.copy():
            if libro["titulo"].lower() == titulo.lower():
                encontrado = True

                while True:
                    try:
                        dias = int(input("¿Cuántos días tuviste el libro?: "))

                        if dias >= 0:
                            break
                        print("Los días no pueden ser negativos.")
                    except ValueError:
                        print("Introduce un número válido.")

                monto_multa = 0

                if dias > DIAS_PERMITIDOS:
                    monto_multa = (dias - DIAS_PERMITIDOS) * MULTA_POR_DIA

                multa_total += monto_multa
                libro["copias"] += 1
                prestados.remove(libro)

                print("Libro devuelto correctamente.")
                print("Multa de esta devolución: RD$", monto_multa)
                print("Multa acumulada: RD$", multa_total)
                break

        if not encontrado:
            print("No tienes ese libro prestado.")

    elif opcion == "5":
        print("--- RESUMEN FINAL ---")
        print("Usuario:", nombre)

        if prestados:
            print("No tienes libros pendientes.")
            for libro in prestados:
                print("-", libro["titulo"])
        else:
            print("No tienes libros pendientes")

        print("Multa total: RD$", multa_total)
        print("Gracias por utilizar la biblioteca.")
        break

    else:
        print("Opción incorrecta. Intenta de nuevo.")
