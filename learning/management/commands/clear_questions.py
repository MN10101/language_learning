from django.core.management.base import BaseCommand
from learning.models import Question, Answer

class Command(BaseCommand):
    help = 'Deletes all questions and answers from the database'

    def handle(self, *args, **kwargs):
        Answer.objects.all().delete()
        Question.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all questions and answers'))
