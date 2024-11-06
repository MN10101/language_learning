from django.core.management.base import BaseCommand
from learning.models import Question, Answer

class Command(BaseCommand):
    help = 'Populates German test questions'

    def handle(self, *args, **kwargs):
        german_questions_data = [
            # A1 Level Questions
            {
                'text': "Was ist die Vergangenheitsform von 'gehen'?",
                'level': 'A1',
                'subject': 'German',
                'answers': [
                    {'text': 'geht', 'is_correct': False},
                    {'text': 'ging', 'is_correct': True},
                    {'text': 'gegangen', 'is_correct': False},
                ]
            },
            {
                'text': "Wie sagt man 'good morning' auf Deutsch?",
                'level': 'A1',
                'subject': 'German',
                'answers': [
                    {'text': 'Guten Tag', 'is_correct': False},
                    {'text': 'Guten Morgen', 'is_correct': True},
                    {'text': 'Gute Nacht', 'is_correct': False},
                ]
            },
            # A2 Level Questions
            {
                'text': "Welches Wort passt: 'Ich habe ___ Hund.'?",
                'level': 'A2',
                'subject': 'German',
                'answers': [
                    {'text': 'einen', 'is_correct': True},
                    {'text': 'eine', 'is_correct': False},
                    {'text': 'ein', 'is_correct': False},
                ]
            },
            {
                'text': "Wie sagt man 'I am hungry' auf Deutsch?",
                'level': 'A2',
                'subject': 'German',
                'answers': [
                    {'text': 'Ich habe Hunger', 'is_correct': True},
                    {'text': 'Ich bin Hunger', 'is_correct': False},
                    {'text': 'Ich esse Hunger', 'is_correct': False},
                ]
            },
            # B1 Level Questions
            {
                'text': "Welches Wort passt: 'Ich freue mich ___ die Reise.'?",
                'level': 'B1',
                'subject': 'German',
                'answers': [
                    {'text': 'auf', 'is_correct': True},
                    {'text': 'zu', 'is_correct': False},
                    {'text': 'bei', 'is_correct': False},
                ]
            },
            {
                'text': "Wie sagt man 'I am looking forward to it' auf Deutsch?",
                'level': 'B1',
                'subject': 'German',
                'answers': [
                    {'text': 'Ich freue mich darauf', 'is_correct': True},
                    {'text': 'Ich denke daran', 'is_correct': False},
                    {'text': 'Ich erinnere mich daran', 'is_correct': False},
                ]
            },
            # B2 Level Questions
            {
                'text': "Welches Wort passt: 'Sie hat das Buch ___ ihrer Mutter gegeben.'?",
                'level': 'B2',
                'subject': 'German',
                'answers': [
                    {'text': 'an', 'is_correct': False},
                    {'text': 'für', 'is_correct': False},
                    {'text': 'von', 'is_correct': True},
                ]
            },
            {
                'text': "Wie sagt man 'The concert was canceled due to the weather' auf Deutsch?",
                'level': 'B2',
                'subject': 'German',
                'answers': [
                    {'text': 'Das Konzert wurde wegen des Wetters abgesagt', 'is_correct': True},
                    {'text': 'Das Konzert war durch das Wetter abgebrochen', 'is_correct': False},
                    {'text': 'Das Konzert ist auf das Wetter abgesagt', 'is_correct': False},
                ]
            },
            # C1 Level Questions
            {
                'text': "Welches Wort passt: 'Er hat den Job ___ seiner Erfahrung bekommen.'?",
                'level': 'C1',
                'subject': 'German',
                'answers': [
                    {'text': 'wegen', 'is_correct': True},
                    {'text': 'zu', 'is_correct': False},
                    {'text': 'bei', 'is_correct': False},
                ]
            },
            {
                'text': "Wie sagt man 'Despite the problems, we managed to finish the project' auf Deutsch?",
                'level': 'C1',
                'subject': 'German',
                'answers': [
                    {'text': 'Trotz der Probleme haben wir das Projekt fertiggestellt', 'is_correct': True},
                    {'text': 'Wegen der Probleme haben wir das Projekt beendet', 'is_correct': False},
                    {'text': 'Dank der Probleme haben wir das Projekt durchgeführt', 'is_correct': False},
                ]
            },
            # C2 Level Questions
            {
                'text': "Welches Wort passt: 'Das Unternehmen hat das Projekt ___ kurzer Zeit abgeschlossen.'?",
                'level': 'C2',
                'subject': 'German',
                'answers': [
                    {'text': 'innerhalb', 'is_correct': True},
                    {'text': 'außerhalb', 'is_correct': False},
                    {'text': 'über', 'is_correct': False},
                ]
            },
            {
                'text': "Wie sagt man 'The intricacies of language require careful study' auf Deutsch?",
                'level': 'C2',
                'subject': 'German',
                'answers': [
                    {'text': 'Die Feinheiten der Sprache erfordern ein sorgfältiges Studium', 'is_correct': True},
                    {'text': 'Die Sprache ist schwer zu verstehen', 'is_correct': False},
                    {'text': 'Sprachliche Regeln sind immer komplex', 'is_correct': False},
                ]
            },
        ]

        for question_data in german_questions_data:
            question = Question.objects.create(
                text=question_data['text'],
                level=question_data['level'],
                subject=question_data['subject']
            )
            for answer_data in question_data['answers']:
                Answer.objects.create(
                    question=question,
                    text=answer_data['text'],
                    is_correct=answer_data['is_correct']
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated German questions'))
