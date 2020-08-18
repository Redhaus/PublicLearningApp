
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

# from events.models import CategoryEventCollection
from assignment_types.models import AssignmentTypes

from .assignment_types_serializer import AssignmentTypeSerializer

from django.db import connection
from django_filters import rest_framework as filters


# AssignmentType Filter
class AssignmentTypeFilter(filters.FilterSet):
    # single filter
    # topics = filters.CharFilter(lookup_expr='icontains')

    # multiple choice filter
    TOPIC_LIST = (
        ('device', 'device'),
        ('essential', 'essential'),
        ('common', 'common'),
        ('concept', 'concept'),
        ('person', 'person'),
        ('event', 'event'),
        ('text', 'text'),
    )

    # multiple choice filter
    topics = filters.MultipleChoiceFilter(
        field_name="topics",
        lookup_expr='contains',
        conjoined=True,  # uses AND instead of OR
        choices=TOPIC_LIST
    )

    # assign model and field terms
    class Meta:
        model = AssignmentTypes
        fields = ('title', 'verb', 'topics')


# VIEWSET
class AssignmentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    # This shows how many queries
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print('Queries Counted: {}'.format(len(connection.queries)))
        return response

    # fetch all lexis items to setup queryset
    queryset = AssignmentTypes.objects.all()

    # set serializer class
    serializer_class = AssignmentTypeSerializer
    filterset_class = AssignmentTypeFilter



