from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
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

check_list = ['checked', '']

ANSWERS = []

for question in QUESTIONS:

    ans_num = question["answers_num"]
    if ans_num == 0:
        print("No answers")
    else:
        for i in range(ans_num):
            answer = {
                'id': i,
                'question_id': question['id'],
                'img': 'https://klike.net/uploads/posts/2023-01/1674365337_3-31.jpg',
                'answer': ' '.join([r.get_random_word() for _ in range(random.randint(10, 15))]),
                'likes_num': random.randint(0, 100),
                'correct': check_list[random.randint(0, 1)],
            }
            ANSWERS.append(answer)


def paginate(request, obj_list, num_per_page=5):
    paginator = Paginator(obj_list, num_per_page)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        objects = paginator.page(page)
    except (EmptyPage, InvalidPage):
        objects = paginator.page(paginator.num_pages)
    return objects


def index(request):
    return render(request, 'index.html', {'questions': paginate(request, QUESTIONS)})


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def ask(request):
    return render(request, 'ask.html')


def settings(request):
    return render(request, 'settings.html')


def question(request, question_id):
    question = QUESTIONS[question_id]
    answers = [answer for answer in ANSWERS if answer.get('question_id') == question_id]

    return render(request, 'question.html', {'question': question, 'answers': paginate(request, answers)})


def tag(request, slug):
    questions = [question for question in QUESTIONS if slug in question.get('tags')]
    return render(request, 'tag.html', {'tag': slug, 'questions': paginate(request, questions)})

