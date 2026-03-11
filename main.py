from clases.biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    while True:
        print("--- Menú Biblioteca ---")
        print("1. Registrar socio")
        print("2. Registrar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar socio")
        print("6. Buscar libro")
        print("7. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Nombre del socio: ")
            dni = input("DNI del socio: ")
            telefono = input("Telefono del socio: ")
            _, mensaje = biblioteca.registrar_socio(nombre, dni, telefono)
            print(mensaje)
                
        elif opcion == "2":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            isbn = input("Código ISBN del libro: ")
            id_ejemplar = input("ID del ejemplar del libro: ")
            _, mensaje = biblioteca.registrar_libro(titulo, autor, isbn, id_ejemplar)
            print(mensaje)

        elif opcion == "3":
            dni = input("Ingrese DNI del socio: ")
            id_ejemplar = input("Ingrese ID del ejemplar del libro: ")
            _, mensaje = biblioteca.prestar_libro(dni, id_ejemplar)
            print(mensaje)

        elif opcion == "4":
            dni = input("Ingrese DNI del socio: ")
            id_ejemplar = input("Ingrese ID del ejemplar del libro: ")
            _, mensaje = biblioteca.devolver_libro(dni, id_ejemplar)
            print(mensaje)           

        elif opcion == "5":
            dni = input("Ingrese DNI del socio: ")
            socio = biblioteca.buscar_socio(dni)
            if socio is None:
                print("Socio no registrado")
            else:
                print(f"Nombre: {socio.nombre}")
                print(f"DNI: {socio.dni}")
                print(f"Teléfono: {socio.telefono}")
                if len(socio.libros_prestados) == 0:
                    print("No tiene libros prestados")
                else:
                    print("Libros prestados: ")
                    for libro in socio.libros_prestados :
                        print(f"- {libro.titulo}")

        elif opcion == "6":
            id_ejemplar = input("Ingrese ID del ejemplar: ")
            libro = biblioteca.buscar_libro(id_ejemplar)
            if libro is None:
                print("Libro no registrado")
            else:
                print(f"Título: {libro.titulo}")
                print(f"Autor: {libro.autor}")
                print(f"ISBN: {libro.isbn}")
                print(f"ID del ejemplar: {libro.id_ejemplar}")
                print(f"Estado: {libro.estado}")

        elif opcion == "7":
            print("Saliendo del sistema")
            break
        else: 
            print("Opción inválida")

main()