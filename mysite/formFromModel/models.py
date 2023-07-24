from django.db import models
from pyexpat import model
from django import forms
from django.forms import ModelForm, Textarea
# Create your models here.

TITLE_CHOICES=(
    ('MR', 'Mr'),
    ('MRS', 'Mrs'),
    ('MS', 'Ms')
)

class Author(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date =  models.DateField()

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ManyToManyField(Author)

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title','birth_date')
        widgets = {'name':Textarea(attrs={'cols':80,'rows':20}),
            'birth_date': forms.DateInput(format=('%m/%d/%Y'),
                attrs = {'class':'form-control','placeholder':'Select a date', 'type':'date'}),
                   }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author']
