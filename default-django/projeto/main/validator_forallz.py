
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages

def validate_check(request,phone,email,show_message):
        try:
            validate_email(email)
        except:
            if show_message:
                messages.error(request, 'Por favor, digite um email valido.')
            return 0
        try:
            phone=phone.replace("(","")
            phone=phone.replace(")","")
            phone=phone.replace(" ","")
            phone=phone.replace("-","")
            phone=list(phone)
            if phone[0] == "+":
                phone.pop(0)
            if phone[0] != "5" and phone[1] != "5":
                phone.insert(0,"5")
                phone.insert(1,"5")
            if phone[2] == "0":
                phone.pop(2)
            if len(phone)>11:
                phone_str=""
                phone=phone_str.join(phone)
                if len(phone)<14:
                    phone=int(phone)
                    return phone
                else:
                    if show_message:
                        messages.error(request, 'Por favor, digite um telefone valido.')
                    return 0
            else:
                if show_message:
                    messages.error(request, 'Por favor, digite o DDD de sua região.')
                return 0         
        except:
            if show_message:
                messages.error(request, 'Por favor, digite um telefone valido.')
            return 0