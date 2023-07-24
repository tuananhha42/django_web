from django.shortcuts import render
from . import forms
# Create your views here.

def reform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        if form.is_valid():
            message = ' Thank you'
        else:
            message = 'Data is invaliid, try again'
    else:
        message = 'Input your information to register'
    return render(request, 'signup.html', {'message':message, 'form':form})