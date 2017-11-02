
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from api.cms.forms import LoginForm,Register

@login_required
def cms_index(request):
    return render(request,'cms_index.html')

def cms_login(request):
    if request.method == 'GET':
        return render(request,'cms_login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username',None)
            password = form.cleaned_data.get('password',None)
            remember = form.cleaned_data.get('remember',None)

            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                nexturl = request.GET.get('next')
                if nexturl:
                    return redirect(nexturl)
                else:
                    return redirect(reverse('cms_index'))
            else:
                return render(request,'cms_login.html',{'error':'用户名或密码错误！'})
        else:
            return render(request,'cms_login.html',{'error':form.errors})


def  cms_register(request):
    if request.method == 'GET':
        return render(request,'cms_register.html')
    else:
        form = Register(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username',None)
            password = form.cleaned_data.get('password',None)
            email = form.cleaned_data.get('email',None)
            User.objects.create_user(username=username,password=password,email=email)
            return redirect(reverse('cms_login.html'))
        else:
            return render(request,'cms_register.html',{'prompt':'注册失败','error':form.errors})


def cms_logout(request):
    logout(request)
    return redirect(reverse('cms_login'))

@login_required
def cms_add_article(request):
    return render(request,'cms_add_article.html')

def cms_settings(request):
    return HttpResponse('个人设置')