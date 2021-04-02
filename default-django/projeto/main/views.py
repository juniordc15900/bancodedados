from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from . import models
from django.core.mail import send_mail
from . import validator_forallz

def index(request):
    data = {}
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    return render(request, 'mains/home1.html',data)

def about(request):
    data = {}
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    return render(request,'mains/about1.html',data)

def contact(request):
    data = {}
    data['current_title'] = 'a'
    data['current_description'] = 'b'

    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        title = request.POST.get("title")
        text_message = request.POST.get("text_message")
        phone = validator_forallz.validate_check(request,phone,email,True)
        if(phone):
            new_contact = models.ContactMessage(name=name,email=email,phone=phone,title=title,message=text_message)
            new_contact.save()
            send_mail(title,text_message,'empresaforallz@gmail.com',['empresaforallz@gmail.com'],fail_silently=True)
            messages.info(request, 'Sua mensagem foi enviada com sucesso.')
        else:
            data['name'] = request.POST.get("name")
            data['email'] = request.POST.get("email")
            data['phone'] = request.POST.get("phone")
            data['title'] = request.POST.get("title")
            data['text_message'] = request.POST.get("text_message")

    return render(request,'mains/contact1.html', data)

def document(request,type_model=''):
    data = {}
    document = models.MainDocument.objects.get(title=type_model)
    data['content_html'] = document.content_html
    data['update'] = document.update
    data['current_title'] = 'a'
    data['current_description'] = 'b'

    return render(request, 'mains/document1.html',data)

def error_404(request, *args, **kwargs):
    data={}
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    return render(request,'mains/404page1.html',data)