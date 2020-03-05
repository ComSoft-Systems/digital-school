import django_filters
from .models import Entry_data


class Entry_dataFilter(django_filters.FilterSet):
    class meta:
        model = Entry_data
        fields = {
            'Query_code',
            'Name',
            'father_name',
            'Address',
            'last',
            'Previous_school'
        }