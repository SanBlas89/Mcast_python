from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  image = models.ImageField(upload_to='projects/')
  link = models.URLField(blank=True, null=True)
  technologies = models.CharField(max_length=200)
  slug = models.SlugField(unique=True)

  def __str__(self):
      return self.title

class BlogPost(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  date_posted = models.DateTimeField(auto_now_add=True)
  category = models.CharField(max_length=100, blank=True)

  def __str__(self):
      return self.title

class Contact(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  message = models.TextField()
  date_sent = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return f"{self.name} - {self.email}"