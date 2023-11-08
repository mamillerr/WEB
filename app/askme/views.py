from django.shortcuts import render
from random_word import RandomWords
import random

r = RandomWords()

QUESTIONS = [
    {
        'id': i,
        'img': 'https://klike.net/uploads/posts/2023-01/1674365337_3-31.jpg',
        'title': ' '.join([r.get_random_word() for _ in range(random.randint(2, 3))]) + '?',
        'description': ' '.join([r.get_random_word() for _ in range(random.randint(10, 15))]) + '...',
        'likes_num': random.randint(0, 100),
        'answers_num': random.randint(0, 5),
        'tags': [r.get_random_word() for _ in range(2)],
    } for i in range(10)
]


def index(request):
    return render(request, 'index.html', {'questions': QUESTIONS})


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def ask(request):
    return render(request, 'ask.html')


def settings(request):
    return render(request, 'settings.html')


def question(request):
    return render(request, 'question.html')


def tag(request):
    return render(request, 'tag.html')
