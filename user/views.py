from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')
        nickname = request.POST.get('nickname', '')

        if password != password2:
            return render(request, 'user/signup.html', {'error': '패스워드를 확인해주세요!'})
        else:
            if username == '' or password == '':
                return render(request, 'user/signup.html', {'error': '사용자 이름과 패스워드는 필수값입니다.'})

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html', {'error': '사용자가 존재합니다'})
            else:
                UserModel.objects.create_user(username=username, password=password, email=email, nickname=nickname)
                return redirect('/login/')


def log_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/login.html', {'error': '유저이름 혹은 패스워드를 확인해 주세요'})
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/login/')
