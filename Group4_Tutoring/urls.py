"""
URL configuration for Group4_Tutoring project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static, serve
from django.conf import settings

#Added to try and make auth_view work#
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # adding repath per PythonAnywhere instructions mjl 6/22
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), #serve media files when deployed
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), #serve static files when deployed

    # forgot password - reset
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # IMPORTANT – THE URL BELOW MUST BE AFTER THE PASSWORD RESET CUSTOM FORM ABOVE if included- was in front of the reset password
    # bringing up the django version first
    # path('', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),



    path('', include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('register.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



