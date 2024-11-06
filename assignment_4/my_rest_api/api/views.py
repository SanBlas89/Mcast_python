from django.shortcuts import render
# Primero, importo los módulos necesarios de Django REST Framework.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer  
# Utilizo el serializer para validar y transformar los datos de libros.

# Establezco una lista vacía como almacenamiento en memoria para simular una base de datos de libros.
books = []

# Ahora, creo la vista para listar y crear libros.
class BookList(APIView):
    # Aquí configuro la función para obtener todos los libros de la lista.
    def get(self, request):
        # Uso el serializer para convertir la lista de libros en formato JSON.
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    # Configuro la función para agregar un nuevo libro.
    def post(self, request):
        # Primero, valido los datos recibidos mediante el serializer.
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():  # Si los datos son válidos, los agrego a la lista de libros.
            books.append(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Si los datos no son válidos, envío un error.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Defino una vista de detalle para manejar operaciones sobre un libro específico usando su ID.
class BookDetail(APIView):
    # Defino la función para obtener un libro específico.
    def get(self, request, id):
        # Busco el libro en la lista usando su ID.
        book = next((b for b in books if b['id'] == id), None)
        if book:
            serializer = BookSerializer(book)
            return Response(serializer.data)
        # Si no encuentro el libro, envío un error 404.
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Configuro la función para actualizar los datos de un libro existente.
    def put(self, request, id):
        book = next((b for b in books if b['id'] == id), None)
        if book:
            # Valido y actualizo los datos del libro si son válidos.
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                book.update(serializer.data)  # Actualizo los datos en la lista en memoria.
                return Response(serializer.data)
            # Envío un error si los datos no son válidos.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envío un error 404 si no encuentro el libro.
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Configuro la función para eliminar un libro por su ID.
    def delete(self, request, id):
        # Uso una nueva asignación para la lista de libros sin el que se elimina.
        global books
        books = [b for b in books if b['id'] != id]  # Elimino el libro usando una lista filtrada.
        return Response(status=status.HTTP_204_NO_CONTENT)  # Envío un código 204 para confirmar la eliminación.
