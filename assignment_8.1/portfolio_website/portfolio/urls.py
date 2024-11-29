from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
  path('', views.home_view, name='home'),
  path('projects/', views.project_list_view, name='project_list'),
  path('projects/<slug:slug>/', views.project_detail_view, name='project_detail'),
  path('blog/', views.blog_list_view, name='blog_list'),
  path('contact/', views.contact_view, name='contact'),
  path('resume/', views.resume_view, name='resume'),
  path('search/', views.search_results_view, name='search_results'),
]