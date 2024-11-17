from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Transaction
from .forms import ProductForm, TransactionForm, CategoryForm

def home(request):
    return render(request, 'home.html')

# Aquí estoy definiendo una vista para listar todas las categorías.
# Cuando el usuario accede a esta vista, obtiene un listado de todas las categorías que he creado.
def category_list(request):
    categories = Category.objects.all()  # Aquí obtengo todas las categorías de la base de datos.
    return render(request, 'inventory/category_list.html', {'categories': categories})  # Luego las envío al template.

# Esta vista me permite añadir una nueva categoría.
# Es útil porque quiero que el usuario pueda crear categorías antes de añadir productos.
def category_add(request):
    if request.method == 'POST':  # Si el usuario está enviando datos con un formulario (usando POST)
        form = CategoryForm(request.POST)  # Cargo los datos en el formulario de categoría.
        if form.is_valid():  # Aquí estoy comprobando si los datos del formulario son correctos.
            form.save()  # Si todo está bien, guardo la nueva categoría en la base de datos.
            return redirect('inventory:category_list')  # Redirijo al usuario a la lista de categorías.
    else:
        form = CategoryForm()  # Si no se está enviando el formulario, solo muestro el formulario vacío.
    return render(request, 'inventory/category_form.html', {'form': form})  # Aquí envío el formulario al template.

# Esta vista muestra todos los productos que tengo en la base de datos.
def product_list(request):
    products = Product.objects.all()  # Obtengo todos los productos para mostrarlos.
    return render(request, 'inventory/product_list.html', {'products': products})  # Los paso al template para renderizar.

# Esta función muestra los detalles de un producto en específico.
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)  # Obtengo un producto específico basado en su ID.
    return render(request, 'inventory/product_detail.html', {'product': product})  # Envío este producto al template.

# Aquí estoy creando una función para añadir un nuevo producto.
def product_add(request):
    if request.method == 'POST':  # Si se envía el formulario con método POST
        form = ProductForm(request.POST)  # Cargo los datos en el formulario de productos.
        if form.is_valid():  # Verifico que los datos sean válidos.
            form.save()  # Si todo está correcto, guardo el producto en la base de datos.
            return redirect('inventory:product_list')  # Después, redirijo a la lista de productos.
    else:
        form = ProductForm()  # Si no hay datos enviados, solo muestro un formulario vacío.
    return render(request, 'inventory/product_form.html', {'form': form})  # Envío este formulario al template para que el usuario lo llene.

# Vista para editar un producto existente.
def product_edit(request, product_id):
    # Obtengo el producto a editar o muestro un 404 si no existe.
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        # Si se envió un formulario, lo valido.
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            # Guardo los cambios si son válidos.
            form.save()
            return redirect('inventory:product_list')
    else:
        # Si es una solicitud GET, muestro el formulario con datos actuales.
        form = ProductForm(instance=product)
    return render(request, 'inventory/product_form.html', {'form': form})

# Vista para eliminar un producto.
def product_delete(request, product_id):
    # Obtengo el producto a eliminar o muestro un 404 si no existe.
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        # Si se confirma la eliminación, elimino el producto.
        product.delete()
        return redirect('inventory:product_list')
    # Muestro una página de confirmación antes de eliminar.
    return render(request, 'inventory/product_confirm_delete.html', {'product': product})


def transaction_create(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.product = product
            transaction.save()
            if transaction.transaction_type == 'IN':
                product.quantity += transaction.quantity
            elif transaction.transaction_type == 'OUT':
                product.quantity -= transaction.quantity
            product.save()
            return redirect('inventory:product_detail', product_id=product.id)
    else:
        form = TransactionForm()
    return render(request, 'inventory/transaction_form.html', {'form':form, 'product': product})


