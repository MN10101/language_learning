# game/management/commands/populate_questions.py
from django.core.management.base import BaseCommand
from learning.models import Question, Answer


class Command(BaseCommand):
    help = 'Populates the database with initial questions and answers'

    def handle(self, *args, **kwargs):
        self.create_questions()
        self.stdout.write(self.style.SUCCESS('Successfully populated the questions and answers'))

    def create_questions(self):
        # Question 1
        q1 = Question.objects.create(text="What is the past tense of 'run'?")
        Answer.objects.create(question=q1, text="Ran", is_correct=True)
        Answer.objects.create(question=q1, text="Run", is_correct=False)
        Answer.objects.create(question=q1, text="Runned", is_correct=False)

        # Question 2
        q2 = Question.objects.create(text="What is the synonym of 'happy'?")
        Answer.objects.create(question=q2, text="Sad", is_correct=False)
        Answer.objects.create(question=q2, text="Joyful", is_correct=True)
        Answer.objects.create(question=q2, text="Angry", is_correct=False)

        # Question 3
        q3 = Question.objects.create(text="Which word is a noun?")
        Answer.objects.create(question=q3, text="Run", is_correct=False)
        Answer.objects.create(question=q3, text="Apple", is_correct=True)
        Answer.objects.create(question=q3, text="Quickly", is_correct=False)

        # Question 4
        q4 = Question.objects.create(text="What is the opposite of 'large'?")
        Answer.objects.create(question=q4, text="Small", is_correct=True)
        Answer.objects.create(question=q4, text="Big", is_correct=False)
        Answer.objects.create(question=q4, text="Huge", is_correct=False)

        # Question 5
        q5 = Question.objects.create(text="Which word is a verb?")
        Answer.objects.create(question=q5, text="Run", is_correct=True)
        Answer.objects.create(question=q5, text="Apple", is_correct=False)
        Answer.objects.create(question=q5, text="Blue", is_correct=False)

        # Question 6
        q6 = Question.objects.create(text="What is the synonym of 'fast'?")
        Answer.objects.create(question=q6, text="Slow", is_correct=False)
        Answer.objects.create(question=q6, text="Quick", is_correct=True)
        Answer.objects.create(question=q6, text="Large", is_correct=False)

        # Question 7
        q7 = Question.objects.create(text="What is the past tense of 'go'?")
        Answer.objects.create(question=q7, text="Went", is_correct=True)
        Answer.objects.create(question=q7, text="Go", is_correct=False)
        Answer.objects.create(question=q7, text="Gone", is_correct=False)

        # Question 8
        q8 = Question.objects.create(text="What is the opposite of 'good'?")
        Answer.objects.create(question=q8, text="Bad", is_correct=True)
        Answer.objects.create(question=q8, text="Nice", is_correct=False)
        Answer.objects.create(question=q8, text="Cool", is_correct=False)

        # Question 9
        q9 = Question.objects.create(text="Which word is an adjective?")
        Answer.objects.create(question=q9, text="Quickly", is_correct=False)
        Answer.objects.create(question=q9, text="Blue", is_correct=True)
        Answer.objects.create(question=q9, text="Run", is_correct=False)

        # Question 10
        q10 = Question.objects.create(text="What is the past tense of 'swim'?")
        Answer.objects.create(question=q10, text="Swam", is_correct=True)
        Answer.objects.create(question=q10, text="Swim", is_correct=False)
        Answer.objects.create(question=q10, text="Swimmed", is_correct=False)

        # Question 11
        q11 = Question.objects.create(text="What is the synonym of 'angry'?")
        Answer.objects.create(question=q11, text="Furious", is_correct=True)
        Answer.objects.create(question=q11, text="Happy", is_correct=False)
        Answer.objects.create(question=q11, text="Excited", is_correct=False)

        # Question 12
        q12 = Question.objects.create(text="Which word is a pronoun?")
        Answer.objects.create(question=q12, text="She", is_correct=True)
        Answer.objects.create(question=q12, text="Blue", is_correct=False)
        Answer.objects.create(question=q12, text="Apple", is_correct=False)

        # Question 13
        q13 = Question.objects.create(text="What is the opposite of 'hot'?")
        Answer.objects.create(question=q13, text="Cold", is_correct=True)
        Answer.objects.create(question=q13, text="Warm", is_correct=False)
        Answer.objects.create(question=q13, text="Cool", is_correct=False)

        # Question 14
        q14 = Question.objects.create(text="What is the synonym of 'easy'?")
        Answer.objects.create(question=q14, text="Simple", is_correct=True)
        Answer.objects.create(question=q14, text="Hard", is_correct=False)
        Answer.objects.create(question=q14, text="Difficult", is_correct=False)

        # Question 15
        q15 = Question.objects.create(text="What is the past tense of 'teach'?")
        Answer.objects.create(question=q15, text="Taught", is_correct=True)
        Answer.objects.create(question=q15, text="Teach", is_correct=False)
        Answer.objects.create(question=q15, text="Teached", is_correct=False)
