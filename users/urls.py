from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import * 
"""импортируем все функции из views"""

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout_view, name='logout'),
    path('registration', reg_form, name='registration'),
]

handler404 = 'web.views.custom_404_view'