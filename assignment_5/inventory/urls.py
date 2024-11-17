from django.urls import path
from . import views

# Aquí defino un espacio de nombres (namespace) para las URLs de esta aplicación.
# Esto me ayudará a evitar conflictos si tengo otras aplicaciones con rutas similares.
app_name = 'inventory'

# A continuación, configuro todas las rutas que necesito para mi aplicación.
urlpatterns = [
    
    # Esta ruta me lleva a la lista de todos los productos.
    path('products/', views.product_list, name='product_list'),

    # Aquí configuro la ruta para añadir un nuevo producto.
    path('product/add/', views.product_add, name='product_add'),

    # Esta ruta me permite editar un producto existente.
    # Uso 'product_id' para identificar el producto que quiero editar.
    path('products/edit/<int:product_id>/', views.product_edit, name='product_edit'),

    # Aquí configuro la ruta para eliminar un producto.
    # Uso 'product_id' para saber qué producto necesito borrar.
    path('products/delete/<int:product_id>/', views.product_delete, name='product_delete'),

    # Esta ruta es para ver los detalles de un producto específico.
    # El 'product_id' me ayuda a seleccionar el producto correcto.
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    # Aquí configuro la ruta para crear una transacción (entrada/salida) para un producto específico.
    # Necesito el 'product_id' para asociar la transacción con el producto correcto.
    path('product/<int:product_id>/transaction/', views.transaction_create, name='transaction_create'),

    # Esta ruta me lleva a la lista de todas las categorías que tengo.
    path('categories/', views.category_list, name='category_list'),

    # Por último, configuro la ruta para añadir una nueva categoría.
    path('categories/add/', views.category_add, name='category_add'),
]
