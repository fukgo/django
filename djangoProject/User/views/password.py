from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site

def password_reset(request):
    if request.method == 'POST':
        email_or_username = request.POST.get('email_or_username')
        try:
            user = User.objects.get(email=email_or_username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=email_or_username)
            except User.DoesNotExist:
                messages.error(request, '用户不存在，请输入正确的邮箱或用户名。')
                return redirect('password_reset')

        # 生成一个随机的Token，用于验证邮件链接的有效性
        token = default_token_generator.make_token(user)

        user_id = urlsafe_base64_encode(force_bytes(user.id))
        domain = get_current_site(request).domain
        reset_url = 'http://{}/user/password-reset/{}/{}'.format(domain, user_id, token)
        print(reset_url)
        # 发送包含重置链接的邮件
        subject = '重置密码'
        message = render_to_string('user/pwd_reset_email.html', {
            'user': user,
            'reset_url': reset_url
        })
        send_mail(subject, message, '15989481080@163.com', [user.email])

        messages.info(request, '我们已发送重置密码的邮件，请检查您的电子邮箱，并按照邮件中的指示完成密码重置。')
        return redirect('password_reset')

    return render(request, 'user/pwd_reset.html')

def password_reset_confirm(request, user_id, token):
    user_id = force_str(urlsafe_base64_decode(user_id))
    user = User.objects.get(pk=user_id)
    if not default_token_generator.check_token(user, token):
        messages.error(request, '链接无效，请重新申请重置密码。')
        return redirect('password_reset')
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            messages.success(request, '密码已重置成功，请使用新密码登录。')
            return redirect('login')
        else:
            messages.error(request, '两次输入的密码不一致，请重新输入。')

    return render(request, 'user/pwd_reset_confirm.html', {'user': user, 'token': token})