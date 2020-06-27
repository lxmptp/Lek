from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import re
import random
from .models import registeredUsers
from registration import models
from .forms import RegisterForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from listForRegistration.models import registeredUsers as User
from django.template.context_processors import csrf
import hashlib
from django.contrib.auth import authenticate
from datetime import date

def random_password():
    length = 8
    passwd = list('1234567890abcdABCD!@#$%^&*()-=_?')
    random.shuffle(passwd)
    passwd = ''.join([random.choice(passwd) for x in range(length)])
    return passwd

def listForRegistrationPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(r'cccc!!!!!!', request.body)
        action_re = re.findall(r'ACCEPT|DELETE', str(request.body)) #Получение имени нажатой кнопки через регулярку
        role = re.findall(r'kommission|secretar', str(request.body)) #Получение роли через регулярку
        i_accept = re.findall(r'ACCEPT+(......*=)', str(request.body))  # Получение id записи через регулярку
        i_delete = re.findall(r'DELETE+(....*=)', str(request.body))  # Получение id записи через регулярку
        object_accept = 0
        object_delete = 0
        print(r'ID Удалить: ', i_delete, 'ID Сохранить', i_accept)
        for a in i_accept:
            i_accept = a
        for d in i_delete:
            i_delete = d
        print(i_delete)
        print(i_accept)
        if i_accept:
            object_accept = i_accept[1:-4]
            object_accept = int(object_accept)
        if i_delete:
            object_delete = i_delete[1:-1]
            object_delete = int(object_delete)
        print(r'ID Удалить: ', object_delete, 'ID Сохранить', object_accept)
        action = ''
        for i in action_re:
            action = i
        for i in role:
            role = i
        print(request.body)
        req = ''
        # В object хранится значение id нажатой кнопки типа int
        # В action хранится значение нажатой кнопки типа str (ACCEPT/DELETE)
        if action=="ACCEPT":
            for i in models.listRegisterRequest.objects.values_list(): # Пробегаем по таблице с заявками
                if i[0] == object_accept:
                    req = list(i)
                    password = random_password()
                    user = User.objects.create_user(username=req[1],
                                                    email=req[2],
                                                    fio=req[3],
                                                    dateb=req[4],
                                                    password=password,
                                                    role=role,
                                                    username_field=req[1],
                                                    is_superuser='None',
                                                    last_login='None',
                                                    first_name='None',
                                                    last_name='None',
                                                    is_staff='False',
                                                    is_active='True',
                                                    date_joined=date.today(),
                                                    )
                    print(password)
                    user.save()
                    models.listRegisterRequest.objects.filter(id=i[0]).delete() #Удаляем заявку

        elif action=="DELETE":
            for i in models.listRegisterRequest.objects.values_list(): # Пробегаем по таблице с заявками
                if i[0] == object_delete:
                    models.listRegisterRequest.objects.filter(id=i[0]).delete() #Удаляем заявку
    else:
        form = RegisterForm()
    listRequest = models.listRegisterRequest.objects.all()
    print(request.user.username)
    return render(request, 'listForRegistration/listForRegistrationPage.html', {'username': request.user.username, 'fio': request.user.fio, 'listRequest': listRequest})

