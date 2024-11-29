from unittest import result
from django.shortcuts import redirect, render
from .forms import ContactForm, ProjectSearchForm, ProjectForm, BlogPostForm

def contact_view(request):
  if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('contact_success')
  else:
      form = ContactForm()
  return render(request, 'portfolio/contact.html', {'form': form})

def search_projects(request):
  form = ProjectSearchForm(request.GET)
  if form.is_valid():
      query = form.cleaned_data.get('query')
      category = form.cleaned_data.get('category')
      # Lógica de búsqueda aquí
  return render(request, 'portfolio/search_results.html', 
               {'form': form, 'results': result})

def home_view(request):
  return render(request, 'portfolio/home.html')

def project_list_view(request):
  return render(request, 'portfolio/project_list.html')

def project_detail_view(request, slug):
  return render(request, 'portfolio/project_detail.html')

def blog_list_view(request):
  return render(request, 'portfolio/blog_list.html')

def contact_view(request):
  return render(request, 'portfolio/contact.html')

def resume_view(request):
  return render(request, 'portfolio/resume.html')

def search_results_view(request):
  return render(request, 'portfolio/search_results.html')