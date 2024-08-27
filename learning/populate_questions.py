from learning.models import Question, Answer

# Sample questions and answers from A1 to C2 levels
questions_data = [
    # A1 Level Questions
    {
        'text': "What is the past tense of 'go'?",
        'level': 'A1',
        'answers': [
            {'text': 'go', 'is_correct': False},
            {'text': 'went', 'is_correct': True},
            {'text': 'gone', 'is_correct': False},
        ]
    },
    {
        'text': "Choose the correct sentence.",
        'level': 'A1',
        'answers': [
            {'text': 'He go to school.', 'is_correct': False},
            {'text': 'He goes to school.', 'is_correct': True},
            {'text': 'He going to school.', 'is_correct': False},
        ]
    },
    {
        'text': "What is the plural of 'mouse'?",
        'level': 'A1',
        'answers': [
            {'text': 'Mouses', 'is_correct': False},
            {'text': 'Mice', 'is_correct': True},
            {'text': 'Mouse', 'is_correct': False},
        ]
    },
    {
        'text': "Fill in the blank: 'She is ____ teacher.'",
        'level': 'A1',
        'answers': [
            {'text': 'a', 'is_correct': True},
            {'text': 'an', 'is_correct': False},
            {'text': 'the', 'is_correct': False},
        ]
    },

    # A2 Level Questions
    {
        'text': "Which of these is a synonym for 'happy'?",
        'level': 'A2',
        'answers': [
            {'text': 'Sad', 'is_correct': False},
            {'text': 'Joyful', 'is_correct': True},
            {'text': 'Angry', 'is_correct': False},
        ]
    },
    {
        'text': "Choose the correct sentence.",
        'level': 'A2',
        'answers': [
            {'text': 'She is going to the store.', 'is_correct': True},
            {'text': 'She are going to the store.', 'is_correct': False},
            {'text': 'She go to the store.', 'is_correct': False},
        ]
    },
    {
        'text': "Fill in the blank: 'They _____ dinner last night.'",
        'level': 'A2',
        'answers': [
            {'text': 'eated', 'is_correct': False},
            {'text': 'ate', 'is_correct': True},
            {'text': 'eat', 'is_correct': False},
        ]
    },

    # B1 Level Questions
    {
        'text': "Choose the correct form of the verb: 'She _____ a book.'",
        'level': 'B1',
        'answers': [
            {'text': 'reads', 'is_correct': True},
            {'text': 'reading', 'is_correct': False},
            {'text': 'read', 'is_correct': False},
        ]
    },
    {
        'text': "Which sentence is in the past perfect tense?",
        'level': 'B1',
        'answers': [
            {'text': 'She had finished the project.', 'is_correct': True},
            {'text': 'She finishes the project.', 'is_correct': False},
            {'text': 'She will finish the project.', 'is_correct': False},
        ]
    },
    {
        'text': "Fill in the blank: 'If I _____ more time, I would learn Spanish.'",
        'level': 'B1',
        'answers': [
            {'text': 'have', 'is_correct': False},
            {'text': 'had', 'is_correct': True},
            {'text': 'will have', 'is_correct': False},
        ]
    },

    # B2 Level Questions
    {
        'text': "Which of these sentences is grammatically correct?",
        'level': 'B2',
        'answers': [
            {'text': 'She don’t like coffee.', 'is_correct': False},
            {'text': 'She doesn’t like coffee.', 'is_correct': True},
            {'text': 'She no like coffee.', 'is_correct': False},
        ]
    },
    {
        'text': "Choose the correct sentence.",
        'level': 'B2',
        'answers': [
            {'text': 'If I see him, I would tell him.', 'is_correct': False},
            {'text': 'If I saw him, I would tell him.', 'is_correct': True},
            {'text': 'If I seen him, I would tell him.', 'is_correct': False},
        ]
    },
    {
        'text': "What is the meaning of the word 'meticulous'?",
        'level': 'B2',
        'answers': [
            {'text': 'Careful and precise', 'is_correct': True},
            {'text': 'Quick and easy', 'is_correct': False},
            {'text': 'Rough and careless', 'is_correct': False},
        ]
    },

    # C1 Level Questions
    {
        'text': "Which of these words is an antonym for 'abundant'?",
        'level': 'C1',
        'answers': [
            {'text': 'Plentiful', 'is_correct': False},
            {'text': 'Sparse', 'is_correct': True},
            {'text': 'Numerous', 'is_correct': False},
        ]
    },
    {
        'text': "Complete the sentence: 'Had he known the truth, he _____ differently.'",
        'level': 'C1',
        'answers': [
            {'text': 'would have acted', 'is_correct': True},
            {'text': 'acted', 'is_correct': False},
            {'text': 'would act', 'is_correct': False},
        ]
    },
    {
        'text': "Which sentence uses the subjunctive mood correctly?",
        'level': 'C1',
        'answers': [
            {'text': 'If I was you, I would go.', 'is_correct': False},
            {'text': 'If I were you, I would go.', 'is_correct': True},
            {'text': 'If I am you, I would go.', 'is_correct': False},
        ]
    },

    # C2 Level Questions
    {
        'text': "Choose the correct sentence with advanced grammar.",
        'level': 'C2',
        'answers': [
            {'text': 'Despite of the rain, we went outside.', 'is_correct': False},
            {'text': 'In spite of the rain, we went outside.', 'is_correct': True},
            {'text': 'In spite the rain, we went outside.', 'is_correct': False},
        ]
    },
    {
        'text': "Which sentence best demonstrates proper use of a conditional clause?",
        'level': 'C2',
        'answers': [
            {'text': 'Were she to know the truth, she would react differently.', 'is_correct': True},
            {'text': 'If she would know the truth, she will react differently.', 'is_correct': False},
            {'text': 'If she knows the truth, she would react differently.', 'is_correct': False},
        ]
    },
    {
        'text': "Which of these sentences correctly uses a relative clause?",
        'level': 'C2',
        'answers': [
            {'text': 'The book which I bought it yesterday is on the table.', 'is_correct': False},
            {'text': 'The book I bought yesterday is on the table.', 'is_correct': True},
            {'text': 'The book that I bought it yesterday is on the table.', 'is_correct': False},
        ]
    }
]

for q_data in questions_data:
    question = Question.objects.create(text=q_data['text'], level=q_data['level'])
    for a_data in q_data['answers']:
        Answer.objects.create(question=question, text=a_data['text'], is_correct=a_data['is_correct'])

print('Successfully populated the database with A1 to C2 questions and answers')
