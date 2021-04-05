from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from . import models
from django.core.mail import send_mail
from . import validator_forallz
from django.contrib.auth.models import User
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
from django.contrib.auth import authenticate as dj_authenticate

def index(request):
    data = {}
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    return render(request, 'mains/home1.html',data)

def profileData(request):
    data = {}
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    if request.method == 'POST':
        print("test")
    return render(request,'mains/profile.html',data)

def logout(request):
    data = {}
    dj_logout(request)
    render(request,'mains/login.html',data)
    return redirect('login')

def login(request):
    data = {}
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = dj_authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                dj_login(request, user)
                return render(request,'mains/home1.html',data)
            else:
                data["message"] = "Sua conta foi desativada."
        else:
            data["message"] = "Seu usuario e senha não batem."
    return render(request,'mains/login.html',data)

def registerClient(request):
    data = {}
    data['current_title'] = 'a'
    data['current_description'] = 'b'

    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        cpf = request.POST.get("cpf")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            repeat_username = User.objects.get(username__exact=email)
        except:
            repeat_username = None
        print(repeat_username)
        if repeat_username == None:
            new_client = models.Client(
                first_name=first_name,
                last_name=last_name,
                email=email,
                cpf=cpf,
                password=password,
            )
            new_client.save()
            django_user = User.objects.create_user(password = password, first_name=first_name, last_name=last_name, username=email, email=email)
            django_user.save()
            dj_login(request,django_user)
            return render(request,'mains/home1.html', data)
        else:
            print("Essa conta já existe")
            data['message'] = "O e-mail "+email+" já está cadastrado, por favor escolha algum outro!"
    return render(request,'mains/cadastra-cliente.html', data)

def registerSupplier(request):
    data = {}
    data['current_title'] = 'a'
    data['current_description'] = 'b'

    if request.method == 'POST':
        cnpj = request.POST.get("cnpj")
        razao = request.POST.get("razao")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repeat_username = User.objects.get(username__exact=email)
        if not repeat_username:
            new_supplier = models.Supplier(
                cnpj=cnpj,
                razao=razao,
                email=email,
                password=password,
            )
            new_supplier.save()
            django_user = User(password = password, username=email, email=email)
            django_user.save()
            dj_login(request,django_user)
        else:
            print("Essa conta já existe")
            data['message'] = "O e-mail "+email+" já está cadastrado, por favor escolha algum outro!"

    return render(request,'mains/cadastra-fornecedor.html', data)

def productPage(request):
    data = {}
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    return render(request, 'mains/product-page.html',data)

def document(request,type_model=''):
    data = {}
    document = models.MainDocument.objects.get(title=type_model)
    data['content_html'] = document.content_html
    data['update'] = document.update
    data['current_title'] = 'a'
    data['current_description'] = 'b'

    return render(request, 'mains/document1.html',data)