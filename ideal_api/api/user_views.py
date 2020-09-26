from django.shortcuts import render
# from django_auto_prefetching import AutoPrefetchViewSetMixin

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

from events.models import CategoryEventCollection
from .events_serializers import EventOverviewSerializer

from django.db import connection


from django_filters import rest_framework as filters


# AssignmentType Filter
class EventsFilter(filters.FilterSet):
    # single filter
    event_title = filters.CharFilter(lookup_expr='icontains')

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

    # goal = filters.CharFilter(lookup_expr='icontains')

    # multiple choice filter
    # standard_type = filters.ModelMultipleChoiceFilter(
    #     field_name="standard_type",
    #     lookup_expr='contains',
    #     conjoined=False,  # uses AND instead of OR
    #     # choices=TOPIC_LIST
    # )

    # assign model and field terms
    class Meta:
        model = CategoryEventCollection
        fields = ('collection_name', 'event_title')



class EventOverviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    # This shows how many queries
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print('Queries Counted: {}'.format(len(connection.queries)))
        return response


    # fetch all lexis items to setup queryset
    queryset = CategoryEventCollection.objects.all()

    # set serializer class
    serializer_class = EventOverviewSerializer
    filterset_class = EventsFilter


    # filter api in viewset in this case 10 = aswl1_e1
    # select_related fetches indivdual FK
    # prefetch_related fetches multiple FK items
    def get_queryset(self):
        return (CategoryEventCollection.objects
                # .select_related('event_collection',)
                .select_related('author_image')
                )

