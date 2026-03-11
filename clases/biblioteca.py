from .clientes import Cliente
from .libros import Libro

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.clientes = {}

    def registrar_cliente(self, nombre, dni, telefono):

        if dni in self.clientes:
            return False, "El cliente ya existe"

        cliente = Cliente(nombre, dni, telefono)

        self.clientes[dni] = cliente

        return True, "Cliente registrado correctamente"

    def registrar_libro (self, titulo, autor, isbn, id_ejemplar):

        if id_ejemplar in self.libros:
            return False, "El ID de ese ejemplar ya esta registrado"
        
        libro = Libro(titulo, autor, isbn, id_ejemplar)

        self.libros[id_ejemplar] = libro

        return True, "Libro registrado correctamente"

    def prestar_libro (self, dni, id_ejemplar):

        if dni not in self.clientes:
            return False, "El cliente no existe"

        if id_ejemplar not in self.libros:
            return False, "El ejemplar no existe"
        
        cliente = self.clientes[dni]
        libro = self.libros[id_ejemplar]

        if libro.estado != "Disponible":
            return False, "El libro no está disponible"
        
        libro.estado = "Prestado"
        cliente.libros_prestados.append(libro)

        return True, "Préstamo registrado correctamente"

    def devolver_libro (self, dni, id_ejemplar):

        if dni not in self.clientes:
            return False, "El cliente no existe"

        if id_ejemplar not in self.libros:
            return False, "El ejemplar no existe"
        
        cliente = self.clientes[dni]
        libro = self.libros[id_ejemplar]

        if libro.estado != "Prestado":
            return False, "El libro no figura como prestado"
        
        if libro not in cliente.libros_prestados:
            return False, "El cliente no tiene prestado ese libro"
        
        libro.estado = "Disponible"
        cliente.libros_prestados.remove(libro)

        return True, "Devolución registrada correctamente"

    def buscar_cliente(self, dni):
        if dni in self.clientes:
            return self.clientes[dni]
        return None

    def buscar_libro(self, id_ejemplar):
        if id_ejemplar in self.libros:
            return self.libros[id_ejemplar]
        return None