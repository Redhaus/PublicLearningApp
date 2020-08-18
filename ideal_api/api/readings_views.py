from django.shortcuts import render
# from django_auto_prefetching import AutoPrefetchViewSetMixin
# from django_auto_prefetching import AutoPrefetchViewSetMixin

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

# import model and serializer
from readings.models import PrimaryFocus, FurtherExplorations
from .readings_serializers import PrimaryFocusSerializer, FurtherExplorationsSerializer


from taggit.models import Tag

from django.db import connection
from django_filters import rest_framework as filters




# AssignmentType Filter
class PrimaryFocusFilter(filters.FilterSet):
    # single filter
    title_major = filters.CharFilter(lookup_expr='icontains')
    keywords = filters.CharFilter(lookup_expr='icontains')

    # assign model and field terms
    class Meta:
        model = PrimaryFocus
        fields = ('event_collection', 'title_major', 'level_ability', 'reading_category', 'keywords')







# PRIMARY FOCUS VIEWSET
class PrimaryFocusViewSet(viewsets.ModelViewSet):

    # This shows how many queries
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print('Queries Counted: {}'.format(len(connection.queries)))
        return response


    # fetch all lexis items to setup queryset
    queryset = PrimaryFocus.objects.all()

    # set serializer class
    serializer_class = PrimaryFocusSerializer
    filterset_class = PrimaryFocusFilter


    # filter api in viewset in this case 10 = aswl1_e1
    # select_related fetches indivdual FK
    # prefetch_related fetches multiple FK items
    def get_queryset(self):
        return (PrimaryFocus.objects
                .select_related('event_collection',)
                .select_related('reading_category', )
                .select_related('book_image', )
                .all()
                )



# FURTHER EXPLORATION FILTERS
class FurtherExplorationsFilter(filters.FilterSet):
    # single filter
    title_minor = filters.CharFilter(lookup_expr='icontains')
    keywords = filters.CharFilter(lookup_expr='icontains')

    # assign model and field terms
    class Meta:
        model = FurtherExplorations
        fields = ('event_collection', 'title_minor', 'reading_category', 'keywords')


# FURTHEREXPLORATIONS VIEWSET
class FurtherExplorationsViewSet(viewsets.ModelViewSet):

    # This shows how many queries
    def dispatch(self, *args, **kwargs):

        response = super().dispatch(*args, **kwargs)
        print('Queries Counted: {}'.format(len(connection.queries)))
        return response


    # fetch all lexis items to setup queryset
    queryset = FurtherExplorations.objects.all()

    # set serializer class
    serializer_class = FurtherExplorationsSerializer
    filterset_class = FurtherExplorationsFilter


    # filter api in viewset in this case 10 = aswl1_e1
    # select_related fetches indivdual FK
    # prefetch_related fetches multiple FK items
    def get_queryset(self):

        return (FurtherExplorations.objects
                .select_related('event_collection',)
                .select_related('reading_category', )
                .select_related('resource_link', )
                )
