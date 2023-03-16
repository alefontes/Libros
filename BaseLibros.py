from Libro import Libro
import csv
import string

class BaseLibros:

    diccionario = {}

    def agregarLibroTitulo(self, libro):
        titulo = libro.titulo.lower()
        if titulo in self.diccionario:
            self.diccionario[titulo].append(libro)
        else:
            self.diccionario[titulo] = [libro]

        self.texto = titulo
        self.limpiar_texto()
        titulo = self.texto
        #Dividir titulo en palabras
        palabras = titulo.split(" ")
        for palabra in palabras:
            if palabra in self.diccionario and palabra in self.diccionario[palabra]:
                self.diccionario[palabra].append(libro)
            else:
                self.diccionario[palabra] = [libro]

    def __init__(self, archivo: str):
        lista_registros = self.carga_libro_csv(archivo)
        for registro in lista_registros:
            id = registro[0]
            imagen = registro[1]
            url_imagen = registro[2]
            titulo = registro[3]
            autor = registro[4]
            id_categoria = registro[5]
            categoria = registro[6]

            libro = Libro(id, imagen, url_imagen,titulo, autor, id_categoria)

            self.agregarLibroTitulo(libro)

    def desplegar(self):
        for llave, valor  in self.diccionario.items():
            print(f"{llave}\n_________________________________________________________________________________________")
            for libro in valor:
                print(libro)

    def carga_libro_csv(self,archivo: str) -> list:
        with open(archivo, 'r') as a:  # Traer el archivo
            leer = csv.reader(a)  # Lector de csv
            data = []  # Crear lista para la lista de datos
            for n in leer:  # El elemento de lista en el lector
                data.append(n)  # Se agregan las 6 filas a la lista
            clean_data = [[n if n else 'Unknown' for n in lista] for lista in
                          data]  # Se quitan los strings vacios de la lista(que son de algunos autores) y se reemplaza por unknown
        return clean_data

    def limpiar_texto(self):

        puntuacion = string.punctuation
        puntuacion = list(puntuacion)
        maspuntuacion = ['«', '»', '¿', '\x0c', '¡']
        puntuacion.extend(maspuntuacion)

        self.texto = self.texto.replace('\n', ' ')
        for n in puntuacion:
            if n in self.texto:
                self.texto = self.texto.replace(n, ' ')

if __name__ == '__main__':
    lista = "booklist2000.csv"
    base = BaseLibros(lista)
    base.desplegar()
