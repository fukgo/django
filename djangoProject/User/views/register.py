from django.http import HttpResponse
from django.contrib.auth.models import User
from ..forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                return HttpResponse('用户已经存在')
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('article_list')
        else:
            print(form)
            return HttpResponse('注册表单输入有误。请重新输入')
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)