import django_filters
from .models import Question_Bank


class Question_Bank_filter(django_filters.FilterSet):
    class Meta:
        model = Question_Bank
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = [
            'question_code',
            'question',
            'subject',
            'classes',
            'publisher',
            'book',
            'chapter',
            'question_type',
            'questions_from',
        ]
>>>>>>> b2b80333f0ee749cdf593a41793c9b50e7002428
