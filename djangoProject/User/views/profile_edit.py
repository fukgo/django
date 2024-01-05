from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..models import Profile
from ..forms import UserProfileForm
from django import forms

@login_required(login_url='/user/login/')
def profile_edit(request, id):
    """表单必须设置`enctype="multipart/form-data"`属性，才能够正确上传图片等文件"""
    user = User.objects.get(id=id)
    # user_id 是 OneToOneField 自动生成的字段
    profile = Profile.objects.get(user_id=id)
    form = UserProfileForm()
    if request.method == 'POST':
        if request.user != user:
            return HttpResponse("你没有权限修改此用户信息。")
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            print(request.FILES)
            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']
                print(profile.avatar)
            else:
                print(False)
            profile.introduction = form.cleaned_data['introduction']
            profile.gender = form.cleaned_data['gender']
            profile.birth_date = form.cleaned_data['birth_date']
            profile.save()
            return redirect('profile_edit', id=id)
        else:
            print(form.errors)
            print(form.cleaned_data)
            return HttpResponse("注册表单输入有误。请重新输入~")

    return render(request, 'user/profile_edit.html', {'form': form, 'user': user, 'profile': profile})