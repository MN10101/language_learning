from django.core.management.base import BaseCommand
from learning.models import Question, Answer

it_questions_data = [
    # HTML Questions
    {
        'text': "What does HTML stand for?",
        'level': 'Basic',
        'answers': [
            {'text': 'Hyper Trainer Marking Language', 'is_correct': False},
            {'text': 'Hyper Text Markup Language', 'is_correct': True},
            {'text': 'Hyper Text Marking Language', 'is_correct': False},
        ]
    },
    {
        'text': "Which tag is used to create a hyperlink in HTML?",
        'level': 'Basic',
        'answers': [
            {'text': '<a>', 'is_correct': True},
            {'text': '<link>', 'is_correct': False},
            {'text': '<href>', 'is_correct': False},
        ]
    },

    # CSS Questions
    {
        'text': "Which CSS property is used to change text color?",
        'level': 'Basic',
        'answers': [
            {'text': 'font-color', 'is_correct': False},
            {'text': 'text-color', 'is_correct': False},
            {'text': 'color', 'is_correct': True},
        ]
    },
    {
        'text': "How do you select an element with the id 'header' in CSS?",
        'level': 'Intermediate',
        'answers': [
            {'text': '#header', 'is_correct': True},
            {'text': '.header', 'is_correct': False},
            {'text': 'header', 'is_correct': False},
        ]
    },

    # JavaScript Questions
    {
        'text': "Which of the following is a JavaScript data type?",
        'level': 'Basic',
        'answers': [
            {'text': 'String', 'is_correct': True},
            {'text': 'Number', 'is_correct': True},
            {'text': 'Float', 'is_correct': False},
        ]
    },
    {
        'text': "Which symbol is used for comments in JavaScript?",
        'level': 'Basic',
        'answers': [
            {'text': '//', 'is_correct': True},
            {'text': '<!-- -->', 'is_correct': False},
            {'text': '#', 'is_correct': False},
        ]
    },

    # Java Questions
    {
        'text': "Which of the following is a valid keyword in Java?",
        'level': 'Intermediate',
        'answers': [
            {'text': 'class', 'is_correct': True},
            {'text': 'void', 'is_correct': True},
            {'text': 'def', 'is_correct': False},
        ]
    },
    {
        'text': "Which data type is used to create a variable that should store text in Java?",
        'level': 'Basic',
        'answers': [
            {'text': 'String', 'is_correct': True},
            {'text': 'string', 'is_correct': False},
            {'text': 'Text', 'is_correct': False},
        ]
    },

    # Python Questions
    {
        'text': "Which of these is used to create a function in Python?",
        'level': 'Basic',
        'answers': [
            {'text': 'function', 'is_correct': False},
            {'text': 'def', 'is_correct': True},
            {'text': 'func', 'is_correct': False},
        ]
    },
    {
        'text': "What is the output of print(2 ** 3) in Python?",
        'level': 'Basic',
        'answers': [
            {'text': '5', 'is_correct': False},
            {'text': '8', 'is_correct': True},
            {'text': '6', 'is_correct': False},
        ]
    },

    # Logic Questions
    {
        'text': "If both inputs of an AND gate are 1, the output is?",
        'level': 'Basic',
        'answers': [
            {'text': '0', 'is_correct': False},
            {'text': '1', 'is_correct': True},
            {'text': 'Depends on the gate', 'is_correct': False},
        ]
    },
    {
        'text': "What is the output of NOT(0) in binary logic?",
        'level': 'Basic',
        'answers': [
            {'text': '1', 'is_correct': True},
            {'text': '0', 'is_correct': False},
            {'text': 'Undefined', 'is_correct': False},
        ]
    },

    # Math Questions
    {
        'text': "What is the value of π (pi) rounded to two decimal places?",
        'level': 'Basic',
        'answers': [
            {'text': '3.14', 'is_correct': True},
            {'text': '3.15', 'is_correct': False},
            {'text': '3.13', 'is_correct': False},
        ]
    },
    {
        'text': "What is 5! (5 factorial)?",
        'level': 'Intermediate',
        'answers': [
            {'text': '120', 'is_correct': True},
            {'text': '60', 'is_correct': False},
            {'text': '20', 'is_correct': False},
        ]
    },
]

class Command(BaseCommand):
    help = 'Populates the database with questions and answers'

    def handle(self, *args, **kwargs):
        self.populate_questions('IT', it_questions_data)
        self.stdout.write(self.style.SUCCESS('Successfully populated questions and answers'))

    def populate_questions(self, subject, questions_data):
        for q_data in questions_data:
            question = Question.objects.create(
                text=q_data['text'],
                level=q_data['level'],
                category='test',
                subject=subject  
            )
            for a_data in q_data['answers']:
                Answer.objects.create(question=question, text=a_data['text'], is_correct=a_data['is_correct'])