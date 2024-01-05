from django.urls import path, include
from User.views import login, lougout, register, generate_code, delete, password, profile_edit
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/', login.login_view, name='login'),
    path('logout/', lougout.logout_view, name='logout'),
    path('register/', register.register, name='register'),
    path('delete/<int:id>/', delete.user_delete, name='delete'),
    path('verification_code/', generate_code.generate_code, name='verification_code'),
    path('password_reset/', password.password_reset, name='password_reset'),
    path('password-reset/<str:user_id>/<str:token>/', password.password_reset_confirm, name='password_reset_confirm'),
    path('profile_edit/<int:id>/', profile_edit.profile_edit, name='profile_edit'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)