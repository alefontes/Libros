class Libro:

    def __init__(self, id: str, image: str, url_image: str, titulo: str, autor: str, id_categoria: str):
        self.id = id
        self.image = image
        self.url_image = url_image
        self.titulo = titulo
        self.autor = autor
        self.id_categoria = int(id_categoria)

    def __str__(self):
        return f"{self.id:12} --- {self.titulo:30} --- {self.autor}"


if __name__ == "__main__":
    libro = Libro('123', "hola.jpg", "imagenesstock.images/hola.jpg", "El Gran Hola", "El Holas", "3")
    print(libro)