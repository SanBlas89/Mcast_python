from django.db import models

# Defino el modelo Category para representar las categorías de productos
class Category(models.Model):
    # Añado un campo 'name' para almacenar el nombre de la categoría
    name = models.CharField(max_length=100)

    # Defino la representación del objeto como el nombre de la categoría
    def __str__(self):
        return self.name

# Defino el modelo Product para representar los productos en el inventario
class Product(models.Model):
    # Campo para el nombre del producto
    name = models.CharField(max_length=255)
    # Campo para la descripción del producto
    description = models.TextField()
    # Campo para el precio del producto con dos decimales
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Campo para la cantidad de productos disponibles (entero positivo)
    quantity = models.PositiveIntegerField(default=0)
    # Campo para asociar el producto con una categoría. Utilizo una clave foránea.
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    # Defino la representación del objeto como el nombre del producto
    def __str__(self):
        return self.name

# Defino el modelo Transaction para registrar las transacciones de inventario
class Transaction(models.Model):
    # Relaciono una transacción con un producto específico mediante una clave foránea
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='transaction')
    # Registro la fecha y hora en que se realiza la transacción, se agrega automáticamente
    date = models.DateTimeField(auto_now_add=True)
    # Campo para almacenar la cantidad de productos que se están moviendo (entrada o salida)
    quantity = models.IntegerField()
    # Campo para definir si es una transacción de entrada o salida (IN o OUT)
    transaction_type = models.CharField(max_length=20, choices=[('IN', 'Stock In'), ('OUT', 'Stock Out')])

    # Represento la transacción como el nombre del producto, tipo de transacción y la cantidad
    def __str__(self):
        return f"{self.product.name} - {self.transaction_type} - {self.quantity}"
