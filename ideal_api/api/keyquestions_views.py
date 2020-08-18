
from django.http import JsonResponse
from django.shortcuts import render
# from django_auto_prefetching import AutoPrefetchViewSetMixin

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

from key_questions.models import KeyQuestions
from .keyquestions_serializers import KeyQuestionsSerializer

from django.db import connection
from django_filters import rest_framework as filters


# AssignmentType Filter
class QuestionsFilter(filters.FilterSet):
    # single filter
    question = filters.CharFilter(lookup_expr='icontains')

    # assign model and field terms
    class Meta:
        model = KeyQuestions
        fields = ('event_collection', 'question', 'id')



class KeyQuestionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    # This shows how many queries
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print('Queries Counted: {}'.format(len(connection.queries)))
        return response

    # fetch all lexis items to setup queryset
    queryset = KeyQuestions.objects.all()

    # set serializer class
    serializer_class = KeyQuestionsSerializer
    filterset_class = QuestionsFilter

    # filter api in viewset in this case 10 = aswl1_e1
    # select_related fetches indivdual FK
    # prefetch_related fetches multiple FK items
    def get_queryset(self):
        return (KeyQuestions.objects
                .select_related('event_collection', )
                # .prefetch_related('questions', )
                )





