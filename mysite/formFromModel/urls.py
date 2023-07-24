from django.urls import path
from . import views
from textwrap import indent


urlpatterns = [
    # path('', views.index, name = 'index')

    path('', views.index, name='index' ),
    
]