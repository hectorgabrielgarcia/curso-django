from django.shortcuts import render, HttpResponse, redirect
from data import models
from presentation import form
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request,'presentation/home.html')

def contactos(request):
    contactos = models.contactos.objects.all()
    return render(request, 'presentation/contactos.html' , {'contactos':contactos})

def about(request):
    return render(request,'presentation/about.html')

def saludo(request, name = 'saludo'):
    if name == '':
        name = 'Sin datos'    
    return render(request,'presentation/saludo.html', {'name':name})

def browser(request):
    browser = request.META['HTTP_USER_AGENT']
    return HttpResponse('El navegador que esta enviando la petición es: ' + browser)

def add(request):
    projectform = form.projectform()
    if request.method == 'POST':
        projectform = form.projectform(data = request.POST)
        if projectform.is_valid():
            projectform.save()
            return redirect(reverse('add') + '?nombre='+request.POST.get('nombre','') )

    return render(request,'presentation/add.html',{'form':projectform})


