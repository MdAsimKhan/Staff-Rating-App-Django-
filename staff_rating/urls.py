from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), #signup url made by us
    path('users/', include('django.contrib.auth.urls')), #inbuilt urls for login/logout; it has no signup url
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
