from django.shortcuts import render
from . import forms
from django.http import *
from django.contrib import messages
from .models import get_user_info_one


def start_page(request):
    if request.method == "GET":
        userform = forms.UserForm()

        return render(request, 'start_page/start_page.html', {'userform': userform})

    elif request.method =="POST":
        userform = forms.UserForm(request.POST)

        userform_email = request.POST.get(str('string_email'))

        userform_date = request.POST.get(str('string_date'))

        userform_phon_number = request.POST.get(str('string_phon_number'))

        user = get_user_info_one()

        user.string_email = request.POST.get('string_email')

        user.string_date = request.POST.get('string_date')

        user.string_text = request.POST.get('string_text')

        user.string_phon_number = request.POST.get('string_phon_number')

        if userform.is_valid():

            messages.success(request,'Валидация прошла успешно')

            user.save()

            return HttpResponse(user)

        else:
            erro_form(request,userform_phon_number,userform_date)
            userform = forms.UserForm()

    else:
        userform = forms.UserForm()


    return render(request, 'start_page/start_page.html', {'userform': userform})


def erro_form(request,userform_phon_number,userform_date):

    if userform_phon_number and userform_date not in '+7' or '-' and '-':
        messages.error(request, 'Дата или номер введены не корректно')

        userform = forms.UserForm()

        return render(request, 'start_page/start_page.html', {'userform': userform})

def all_items(request):
    user_forms_page = get_user_info_one.objects.all()

    if request.method =="POST":

        user_forms_page.delete()

        return render(request, 'start_page/page_post.html', {'user': user_forms_page})

    return render(request, 'start_page/page_post.html', {'user': user_forms_page})