from .socios import Socio
from .libros import Libro

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.socios = {}

    def registrar_socio(self, nombre, dni, telefono):

        if dni in self.socios:
            return False, "El socio ya existe"

        socio = Socio(nombre, dni, telefono)

        self.socios[dni] = socio

        return True, "Socio registrado correctamente"

    def registrar_libro (self, titulo, autor, isbn, id_ejemplar):

        if id_ejemplar in self.libros:
            return False, "El ID de ese ejemplar ya esta registrado"
        
        libro = Libro(titulo, autor, isbn, id_ejemplar)

        self.libros[id_ejemplar] = libro

        return True, "Libro registrado correctamente"

    def prestar_libro (self, dni, id_ejemplar):

        if dni not in self.socios:
            return False, "El socio no existe"

        if id_ejemplar not in self.libros:
            return False, "El ejemplar no existe"
        
        socio = self.socios[dni]
        libro = self.libros[id_ejemplar]

        if libro.estado != "Disponible":
            return False, "El libro no está disponible"
        
        libro.estado = "Prestado"
        socio.libros_prestados.append(libro)

        return True, "Préstamo registrado correctamente"

    def devolver_libro (self, dni, id_ejemplar):

        if dni not in self.socios:
            return False, "El socio no existe"

        if id_ejemplar not in self.libros:
            return False, "El ejemplar no existe"
        
        socio = self.socios[dni]
        libro = self.libros[id_ejemplar]

        if libro.estado != "Prestado":
            return False, "El libro no figura como prestado"
        
        if libro not in socio.libros_prestados:
            return False, "El socio no tiene prestado ese libro"
        
        libro.estado = "Disponible"
        socio.libros_prestados.remove(libro)

        return True, "Devolución registrada correctamente"

    def buscar_socio(self, dni):
        if dni in self.socios:
            return self.socios[dni]
        return None

    def buscar_libro(self, id_ejemplar):
        if id_ejemplar in self.libros:
            return self.libros[id_ejemplar]
        return None