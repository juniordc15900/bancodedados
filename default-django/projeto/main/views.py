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
import random

def index(request):
    data = {}
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    supp = models.Supplier.objects.order_by("?")
    print(supp)
    try:
        for sup in supp:
            print(sup)
            pk = sup.pk
            if models.Product.objects.all().filter(supplier=sup).count() > 0:
                data['product_list'] = models.Product.objects.all().filter(supplier=models.Supplier.objects.get(pk=pk))
                break
        if request.method == 'POST':
            if 'search_for' in request.POST:
                data['filter'] = request.POST.get("search_text")
                data['filterId'] = '0'
                data['product_list'] = models.Product.objects.filter(name__contains = request.POST.get("search_text"))
                print(data['product_list'])
                return render(request, 'mains/search.html',data)
        data['category_list'] = list()
        if models.Product.objects.all().filter(category='comida').count() > 0:
            data['category_list'].append(models.Product.objects.all().filter(category='comida'))
        if models.Product.objects.all().filter(category='computador').count() > 0:
            data['category_list'].append(models.Product.objects.all().filter(category='computador'))
        if models.Product.objects.all().filter(category='livro').count() > 0:
            data['category_list'].append(models.Product.objects.all().filter(category='livro'))
        if models.Product.objects.all().filter(category='roupa').count() > 0:
            data['category_list'].append(models.Product.objects.all().filter(category='roupa'))
        if models.Product.objects.all().filter(category='movel').count() > 0:
            data['category_list'].append(models.Product.objects.all().filter(category='movel'))
        if models.Product.objects.all().filter(category='outros').count() > 0:
            data['category_list'].append(models.Product.objects.all().filter(category='outros'))
    except:
        print("erro bla bla bla")
    return render(request, 'mains/home1.html',data)

def profileData1(request):
    data = {}
    if request.method == 'POST':
        if 'profile_add_ad' in request.POST:
            addressStreet = request.POST.get("addressStreet")
            addressPostal = request.POST.get("addressPostal")
            addressNumber = request.POST.get("addressNumber")
            addressComplement = request.POST.get("addressComplement")
            addressCity = request.POST.get("addressCity")
            addressState = request.POST.get("addressState")
            addressCountry = request.POST.get("addressCountry")
            try:
                new_address = models.Address(    
                    street = addressStreet,
                    city = addressCity,
                    state = addressState,
                    country = addressCountry,
                    number = addressNumber,
                    complement = addressComplement,
                    cep = addressPostal,
                    client = models.Client.objects.get(email=request.user.email)
                )
                new_address.save()
            except:
                print("Deu erro na criação")
        elif 'profile_add_card' in request.POST:
            cardNumber = request.POST.get("cardNumber")
            cardValidation = request.POST.get("cardValidation")
            cardSecurity = request.POST.get("cardSecurity")
            cardFlag = request.POST.get("cardFlag")
            try:
                new_card = models.Card(
                    client = models.Client.objects.get(email=request.user.email),
                    number = cardNumber,
                    validation = cardValidation,
                    security_code = cardSecurity,
                    flag = cardFlag
                )
                new_card.save()
            except:
                print("Deu erro na criação")
        elif 'profile_save' in request.POST:
            profileEmail = request.POST.get("email")
            profilePassword = request.POST.get("password")
            profileFirstName = request.POST.get("first_name")
            profileLastName = request.POST.get("last_name")
            profileCpf = request.POST.get("cpf")
            profilePhone = request.POST.get("phone")
            try:
                edit_profile = models.Client.objects.get(email=request.user.email)
                edit_profile.first_name = profileFirstName
                edit_profile.last_name = profileLastName
                edit_profile.cpf = profileCpf
                edit_profile.phone = profilePhone
                edit_profile.password = profilePassword
                edit_profile.save(force_update=True)
            except:
                print("Deu erro na edição")
        else:
            print("coecoe")
    data['address_list'] = models.Address.objects.all().filter(client=models.Client.objects.get(email=request.user.email))
    data['card_list'] = models.Card.objects.all().filter(client=models.Client.objects.get(email=request.user.email))
    data['client'] = models.Client.objects.get(email=request.user.email)
    return render(request,'mains/profile.html',data)

def profileData2(request):
    data={}
    if request.method == 'POST':
        if 'profile_add_pro' in request.POST:
            productName = request.POST.get("productName")
            productImage = request.POST.get("productImage")
            productId = request.POST.get("productId")
            productPrice = request.POST.get("productPrice")
            productQuant = request.POST.get("productQuant")
            productCategory = request.POST.get("productCategory")
            print("2")
            
            try:
                new_product = models.Product(    
                    name = productName,
                    image = productImage,
                    id_product = productId,
                    price = productPrice,
                    quantity= productQuant,
                    category= productCategory,
                    supplier = models.Supplier.objects.get(email=request.user.email)
                )
                new_product.save()
            except:
                print("Deu erro na criação")        
        if 'profile_edit_pro' in request.POST:
            productName = request.POST.get("productName")
            productId = request.POST.get("productId")
            productPrice = request.POST.get("productPrice")
            productQuant = request.POST.get("productQuant")
            
            try:
                new_product = models.Product(    
                    name = productName,
                    image = productImage,
                    id_product = productId,
                    price = productPrice,
                    quantity= productQuant,
                    supplier = models.Supplier.objects.get(email=request.user.email)
                )
                new_product.save()
            except:
                print("Deu erro na criação")
        elif 'profile_save' in request.POST:
            profileEmail = request.POST.get("email")
            profilePassword = request.POST.get("password")
            profileCnpj = request.POST.get("cnpj")
            profileRazao = request.POST.get("razao")
            profilePhone = request.POST.get("phone")
            try:
                edit_profile = models.Supplier.objects.get(email=request.user.email)
                edit_profile.cnpj = profileCnpj
                edit_profile.razao = profileRazao
                edit_profile.phone = profilePhone
                edit_profile.password = profilePassword
                edit_profile.save(force_update=True)
            except:
                print("Deu erro na edição")
        else:
            print("coecoe")
    data['product_list'] = models.Product.objects.all().filter(supplier=models.Supplier.objects.get(email=request.user.email))
    data['supplier'] = models.Supplier.objects.get(email=request.user.email)
    return render(request,'mains/profile.html',data)


def search(request, filter=None):
    data = {}
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    if request.method == 'POST':
        if 'search_for' in request.POST:
            data['filter'] = request.POST.get("search_text")
            data['filterId'] = '0'
            data['product_list'] = models.Product.objects.filter(name__contains = request.POST.get("search_text"))
            print(data['product_list'])
            return render(request, 'mains/search.html',data)
    data['product_list'] = list()
    product_list = models.Product.objects.all().filter()
    if filter == 'f1000':
        data['filter'] = "Produtos de 1000 reais ou mais"
        for product in product_list:
            if int(product.price) >= 1000:
                data['product_list'].append(product)
    elif filter == 'f500':
        data['filter'] = "Produtos de 999 reais até 500 reais"
        for product in product_list:
            if int(product.price) >= 500 and int(product.price) <= 999:
                data['product_list'].append(product)
    elif filter == 'f100':
        data['filter'] = "Produtos de 499 reais até 100 reais"
        for product in product_list:
            if int(int(product.price)) >= 100 and int(product.price) <= 499:
                data['product_list'].append(product)
    elif filter == 'f99':
        data['filter'] = "Produtos de 99 reais ou menos"
        for product in product_list:
            if int(product.price) < 100:
                data['product_list'].append(product)
    return render(request, 'mains/search.html',data)


def delete(request,delete_type,delete_pk):
    data = {}
    if(delete_type == 'address'):
        role=1
        delete_address = models.Address.objects.get(pk=delete_pk)
        if(delete_address.client == models.Client.objects.get(email=request.user.email)):
            delete_address.delete()
    elif(delete_type == 'card'):
        role=1
        delete_card = models.Card.objects.get(pk=delete_pk)
        if(delete_card.client == models.Client.objects.get(email=request.user.email)):
            delete_card.delete()
    elif(delete_type == 'product'):
        role=2
        delete_product = models.Product.objects.get(pk=delete_pk)
        if(delete_product.supplier == models.Supplier.objects.get(email=request.user.email)):
            delete_product.delete()
    elif(delete_type == 'sellProduct'):
        delete_product = models.SellProduct.objects.get(pk=delete_pk)
        delete_product.delete()
        render(request,'mains/carrinho.html',data)
        return redirect('carrinho')
    else:
        print("Erro no sistema.")
    

    render(request,'mains/profile.html',data)
    if role==1:
        return redirect('profileData1')
    if role==2:
        return redirect('profileData2')

def edit(request,edit_pk):
    data = {}
    edit_product = models.Product.objects.get(pk=edit_pk)
    data['product'] = edit_product
    data['supplier'] = edit_product.supplier
    if request.method == 'POST':
        if 'profile_edit_pro' in request.POST:
            productName = request.POST.get("productName")
            productPrice = request.POST.get("productPrice")
            productQuant = request.POST.get("productQuant")
            productCategory = request.POST.get("productCategory")
            try:
                edit_product.name = productName
                edit_product.price = productPrice
                edit_product.quantity= productQuant
                edit_product.category= productCategory
                edit_product.save()
                render(request,'mains/profile.html',data)
                return redirect('profileData2')
            except:
                print("Deu erro na criação")    
    else:
        print("Erro no sistema.")
    return render(request,'mains/profile_edit_pro.html',data)

def productPage(request,product_pk):
    data={}
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    if request.method == 'POST':
        if 'search_for' in request.POST:
            data['filter'] = request.POST.get("search_text")
            data['filterId'] = '0'
            data['product_list'] = models.Product.objects.filter(name__contains = request.POST.get("search_text"))
            print(data['product_list'])
            return render(request, 'mains/search.html',data)
        elif 'cart_add' in request.POST:
            client = models.Client.objects.get(email=request.user.email)
            quantidade = request.POST.get("productQuantity")
            cart = models.Sell.objects.all().filter(client=client).filter(conclude=0)
            if cart.count() > 0:
                sell_obj = cart.first()
                product_list = models.SellProduct.objects.all().filter(sell=sell_obj)
                product=models.Product.objects.get(pk=product_pk)
                has_product = product_list.filter(product=product)
                if has_product.count() > 0:
                    sell_product = has_product.first()
                    sell_product.quantity = float(sell_product.quantity)+float(quantidade)
                    sell_product.value = float(sell_product.value)+(float(quantidade)*float(models.Product.objects.get(pk=product_pk).price))
                    sell_product.save()
                else:
                    produto_vendido = models.SellProduct(
                        product=product, 
                        quantity=quantidade, 
                        supplier=models.Product.objects.get(pk=product_pk).supplier,
                        sell=sell_obj,
                        value=float(quantidade)*float(models.Product.objects.get(pk=product_pk).price),
                        real_value=(float(quantidade)*float(models.Product.objects.get(pk=product_pk).price))-(float(quantidade)*float(models.Product.objects.get(pk=product_pk).price)*0.01)
                    )
                    produto_vendido.save()
            else:
                sell_obj = models.Sell(client=client)
                sell_obj.save()
                produto_vendido = models.SellProduct(
                    product=models.Product.objects.get(pk=product_pk), 
                    quantity=quantidade, 
                    supplier=models.Product.objects.get(pk=product_pk).supplier,
                    sell=sell_obj,
                    value=float(quantidade)*float(models.Product.objects.get(pk=product_pk).price),
                    real_value=(float(quantidade)*float(models.Product.objects.get(pk=product_pk).price))-(float(quantidade)*float(models.Product.objects.get(pk=product_pk).price)*0.01)
                )
                produto_vendido.save()            
            product_list = models.SellProduct.objects.all().filter(sell=sell_obj)
            data['carrinho'] = product_list
            return render(request,'mains/carrinho.html',data)

    product = models.Product.objects.get(pk=product_pk)
    data['product'] = product
    data['productx10'] = int(product.price) / 10
    return render(request,'mains/product-page.html',data)

def finaliza(request):
    data={}
    client = models.Client.objects.get(email=request.user.email)
    sell_obj = models.Sell.objects.all().filter(client=client).filter(conclude=0).first()
    product_list = models.SellProduct.objects.all().filter(sell=sell_obj)
    for product_sell in product_list:
        if product_sell.quantity > product_sell.product.quantity or product_sell.quantity < 0:
            data['message'] = "Desculpe mas o produto "+str(product_sell.product.name)+" não tem essa quantidade no estoque"
            delete_product = models.SellProduct.objects.get(pk=product_sell.pk)
            delete_product.delete()
            return render(request,'mains/finaliza.html',data)
    for product_sell in product_list:
        product_sell.product.quantity = product_sell.product.quantity - product_sell.quantity
        product_sell.product.save()
    sell_obj.conclude = 1
    sell_obj.save()
    data['message'] = "Sua compra foi efetuada com sucesso!"
    return render(request,'mains/finaliza.html',data)

def history(request):
    data={}
    user = request.user
    if request.method == 'POST':
        if 'search_for' in request.POST:
            data['filter'] = request.POST.get("search_text")
            data['filterId'] = '0'
            data['product_list'] = models.Product.objects.filter(name__contains = request.POST.get("search_text"))
            print(data['product_list'])
            return render(request, 'mains/search.html',data)
    if user.profile.role == '1':
        client = models.Client.objects.get(email=request.user.email)
        buy_list = models.Sell.objects.all().filter(client=client)
        buy_list = models.Sell.objects.all().filter(client=client).filter(conclude=1)
        print(buy_list)
        lista_compras_final = list()
        for buy in buy_list:
            lista_compras = list()
            print(buy)
            sell_list = models.SellProduct.objects.all().filter(sell=buy)
            for sell in sell_list:
                lista_compras.append(sell)
            lista_compras_final.append(lista_compras)
        data['buy_list'] = lista_compras_final
    else:
        supplier = models.Supplier.objects.get(email=request.user.email)
        sell_list = models.SellProduct.objects.all().filter(supplier=supplier)
        data['sell_list'] = sell_list
    return render(request,'mains/history.html',data)


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
        if 'search_for' in request.POST:
            data['filter'] = request.POST.get("search_text")
            data['filterId'] = '0'
            data['product_list'] = models.Product.objects.filter(name__contains = request.POST.get("search_text"))
            print(data['product_list'])
            return render(request, 'mains/search.html',data)
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = dj_authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                dj_login(request, user)
                render(request,'mains/home1.html',data)
                return redirect('home')
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
        if 'search_for' in request.POST:
            data['filter'] = request.POST.get("search_text")
            data['filterId'] = '0'
            data['product_list'] = models.Product.objects.filter(name__contains = request.POST.get("search_text"))
            print(data['product_list'])
            return render(request, 'mains/search.html',data)
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
            django_user.profile.role = 1
            django_user.save()
            dj_login(request,django_user)
            render(request,'mains/home1.html', data)
            return redirect('home')
        else:
            print("Essa conta já existe")
            data['message'] = "O e-mail "+email+" já está cadastrado, por favor escolha algum outro!"
    return render(request,'mains/cadastra-cliente.html', data)

def registerSupplier(request):
    data = {}
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    if request.method == 'POST':
        if 'search_for' in request.POST:
            data['filter'] = request.POST.get("search_text")
            data['filterId'] = '0'
            data['product_list'] = models.Product.objects.filter(name__contains = request.POST.get("search_text"))
            print(data['product_list'])
            return render(request, 'mains/search.html',data)
    if request.method == 'POST':
        cnpj = request.POST.get("cnpj")
        razao = request.POST.get("razao")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            repeat_username = User.objects.get(username__exact=email)
        except:
            repeat_username = None
        if repeat_username == None:
            new_supplier = models.Supplier(
                cnpj=cnpj,
                razao=razao,
                email=email,
                password=password,
            )
            new_supplier.save()
            django_user = User.objects.create_user(password = password,username=email, email=email)
            django_user.profile.role = 2
            django_user.save()
            dj_login(request,django_user)
            render(request,'mains/home1.html', data)
            return redirect('home')
        else:
            print("Essa conta já existe")
            data['message'] = "O e-mail "+email+" já está cadastrado, por favor escolha algum outro!"

    return render(request, 'mains/cadastra-fornecedor.html',data)


def carrinho(request):
    data = {}
    if request.method == 'POST':
        if 'search_for' in request.POST:
            data['filter'] = request.POST.get("search_text")
            data['filterId'] = '0'
            data['product_list'] = models.Product.objects.filter(name__contains = request.POST.get("search_text"))
            print(data['product_list'])
            return render(request, 'mains/search.html',data)
    client = models.Client.objects.get(email=request.user.email)
    sell_obj = models.Sell.objects.all().filter(client=client).filter(conclude=0).first()
    product_list = models.SellProduct.objects.all().filter(sell=sell_obj)
    data['carrinho'] = product_list
    return render(request,'mains/carrinho.html', data)

def document(request,type_model=''):
    data = {}
    data['current_title'] = 'a'
    data['current_description'] = 'b'
    if request.method == 'POST':
        if 'search_for' in request.POST:
            data['filter'] = request.POST.get("search_text")
            data['filterId'] = '0'
            data['product_list'] = models.Product.objects.filter(name__contains = request.POST.get("search_text"))
            print(data['product_list'])
            return render(request, 'mains/search.html',data)
    document = models.MainDocument.objects.get(title=type_model)
    data['content_html'] = document.content_html
    data['update'] = document.update
    data['current_title'] = 'a'
    data['current_description'] = 'b'

    return render(request, 'mains/document1.html',data)