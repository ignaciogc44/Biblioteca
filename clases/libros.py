class Libro:
    def __init__ (self, titulo, autor, isbn, id_ejemplar):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.id_ejemplar = id_ejemplar
        self.estado = "Disponible"