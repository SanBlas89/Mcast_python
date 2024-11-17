# Importo las clases necesarias para crear formularios.
from django import forms
# Importo los modelos para usarlos en los formularios.
from .models import Product, Transaction, Category

# Formulario basado en el modelo 'Category'.
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name'] # Incluyo todos los campos del modelo que necesite.

# Formulario para añadir o editar productos.
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Enter product description'
            }),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
# Formulario para registrar transacciones (entradas/salidas).
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['quantity', 'transaction_type']
