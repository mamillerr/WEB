import random

from django.core.management.base import BaseCommand
from mimesis import Person
from mimesis.locales import Locale
from askme.models import Question, Tag, Answer, Profile
from django.contrib.auth.models import User
from mimesis import Text
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Fill database with randomized content'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Indicates the number of rows to be created')

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [User, Profile, Question, Answer, Tag]
        for m in models:
            m.objects.all().delete()

        ratio = kwargs['ratio']

        _fill_users(ratio)
        _fill_tags(ratio)
        _fill_questions(ratio * 10)
        _fill_answers(ratio * 100)
        _fill_likes(ratio * 500)


def _fill_users(ratio):
    for _ in range(ratio):
        person = Person(Locale.EN)

        try:
            u = User(first_name=person.first_name(),
                     last_name=person.last_name(),
                     email=person.email(),
                     password=person.password(),
                     is_staff=False,
                     username=person.username(),
                     )

            u.save()

            p = Profile(user=u)
            p.save()
        except IntegrityError:
            continue


def _fill_tags(ratio):
    for _ in range(ratio):
        txt = Text(Locale.EN)
        try:
            t = Tag(name=txt.word())
            t.save()
        except IntegrityError:
            continue


def _fill_questions(ratio):
    for _ in range(ratio):
        txt = Text(Locale.EN)
        random_user = User.objects.order_by('?').first()

        q = Question(title=txt.quote(),
                     content=txt.text(5),
                     user=random_user
                     )

        q.save()

        tags = Tag.objects.order_by('?')[:2]
        q.tags.set(tags)
        q.save()


def _fill_answers(ratio):
    for _ in range(ratio):
        txt = Text(Locale.EN)

        random_user = User.objects.order_by('?').first()
        random_question = Question.objects.order_by('?').first()

        a = Answer(content=txt.text(5), user=random_user, question=random_question, is_correct=False)
        a.save()


def _fill_likes(ratio):
    for _ in range(ratio):
        users = list(User.objects.all())
        questions = list(Question.objects.all())
        answers = list(Answer.objects.all())

        random_user = random.choice(users)
        random_question = random.choice(questions)
        random_answer = random.choice(answers)

        random_question.likes.add(random_user)
        random_answer.likes.add(random_user)