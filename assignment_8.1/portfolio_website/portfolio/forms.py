from django import forms
from .models import Contact, Project, BlogPost

class ContactForm(forms.ModelForm):
    """
    Formulario para el contacto basado en el modelo Contact
    """
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name'
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email'
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Your Message',
            'rows': 4
        })
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def clean_email(self):
        """
        Validación personalizada para el campo email
        """
        email = self.cleaned_data.get('email')
        if not email.strip():
            raise forms.ValidationError('Email is required')
        return email

class ProjectSearchForm(forms.Form):
    """
    Formulario para la búsqueda de proyectos
    """
    query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search projects...'
        })
    )
    
    category = forms.ChoiceField(
        required=False,
        choices=[('', 'All Categories')] + [
            ('web', 'Web Development'),
            ('mobile', 'Mobile Development'),
            ('desktop', 'Desktop Applications'),
            ('other', 'Other')
        ],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

class ProjectForm(forms.ModelForm):
    """
    Formulario para la creación y edición de proyectos
    """
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'technologies', 'link', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Project Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Project Description',
                'rows': 4
            }),
            'technologies': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Technologies Used (comma separated)'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Project URL'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL Slug'
            })
        }

class BlogPostForm(forms.ModelForm):
    """
    Formulario para la creación y edición de posts del blog
    """
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post Title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Post Content',
                'rows': 6
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post Category'
            })
        }

class NewsletterSubscriptionForm(forms.Form):
    """
    Formulario para suscripción al newsletter
    """
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.strip():
            raise forms.ValidationError('Email is required')
        return email

class FileUploadForm(forms.Form):
    """
    Formulario para la carga de archivos (como el CV)
    """
    file = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'form-control'
        })
    )
    
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'File description'
        })
    )

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if file.size > 5*1024*1024:  # 5MB limit
                raise forms.ValidationError('File size must be under 5MB')
            allowed_types = ['application/pdf', 'application/msword',
                           'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
            if file.content_type not in allowed_types:
                raise forms.ValidationError('Only PDF and Word documents are allowed')
        return file