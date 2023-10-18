from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('settings/', views.settings, name='settings'),
    path('ask/', views.ask, name='ask'),
    path('question/35/', views.question, name='question'),
    path('tag/blablabla/', views.tag, name='tag'), #Нужно ли добавлять отдельный шаблон?
    #path('hot/', views.hot, name='hot'), ???
]