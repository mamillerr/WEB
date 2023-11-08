from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('settings/', views.settings, name='settings'),
    path('ask/', views.ask, name='ask'),
    path('question/<int:question_id>', views.question, name='question'),
    path('tag/<str:slug>/', views.tag, name='tag'),
    path('hot/', views.hot, name='hot'),
]