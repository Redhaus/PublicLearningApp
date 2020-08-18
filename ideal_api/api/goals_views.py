from django.shortcuts import render
# from django_auto_prefetching import AutoPrefetchViewSetMixin

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

from continual_goals.models import ContinualGoals
from .goals_serializers import ContinualGoalSerializer

from django.db import connection

from django_filters import rest_framework as filters


# AssignmentType Filter
class GoalsFilter(filters.FilterSet):
    # single filter
    # topics = filters.CharFilter(lookup_expr='icontains')

    # multiple choice filter
    # TOPIC_LIST = (
    #     ('device', 'device'),
    #     ('essential', 'essential'),
    #     ('common', 'common'),
    #     ('concept', 'concept'),
    #     ('person', 'person'),
    #
    #
    # )

    goal = filters.CharFilter(lookup_expr='icontains')

    # multiple choice filter
    # standard_type = filters.ModelMultipleChoiceFilter(
    #     field_name="standard_type",
    #     lookup_expr='contains',
    #     conjoined=False,  # uses AND instead of OR
    #     # choices=TOPIC_LIST
    # )

    # assign model and field terms
    class Meta:
        model = ContinualGoals
        fields = ('goal', 'standard_type')






class ContinualGoalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    # This shows how many queries
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print('Queries Counted: {}'.format(len(connection.queries)))
        return response


    # fetch all lexis items to setup queryset
    queryset = ContinualGoals.objects.all()

    # set serializer class
    serializer_class = ContinualGoalSerializer
    filterset_class = GoalsFilter


    # filter api in viewset in this case 10 = aswl1_e1
    # select_related fetches indivdual FK
    # prefetch_related fetches multiple FK items
    def get_queryset(self):
        return (ContinualGoals.objects
                .select_related('standard_type',)
                )

