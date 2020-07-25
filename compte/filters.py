import django_filters
from .models import *
from django_filters import DateFilter

class CommandeFilter(django_filters.FilterSet):

    date_ajout = DateFilter(field_name="date_add", lookup_expr='gte')
    class Meta:
        model = Commande
        fields = '__all__'
        exclude = ['client', 'date_add']

