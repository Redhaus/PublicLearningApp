from django.shortcuts import render
# from django_auto_prefetching import AutoPrefetchViewSetMixin

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

from extensions.models import Extensions
from .extensions_serializers import ExtensionsSerializer

from django.db import connection

from django_filters import rest_framework as filters


# AssignmentType Filter
class ExtensionsFilter(filters.FilterSet):
    # single filter
    action = filters.CharFilter(lookup_expr='icontains')

    # assign model and field terms
    class Meta:
        model = Extensions
        fields = ('event_collection', 'action', 'extension_lexis_link')




class ExtensionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    # This shows how many queries
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print('Queries Counted: {}'.format(len(connection.queries)))
        return response


    # fetch all lexis items to setup queryset
    queryset = Extensions.objects.all()

    # set serializer class
    serializer_class = ExtensionsSerializer
    filterset_class = ExtensionsFilter


    # filter api in viewset in this case 10 = aswl1_e1
    # select_related fetches indivdual FK
    # prefetch_related fetches multiple FK items
    def get_queryset(self):
        return (Extensions.objects
                .select_related('event_collection',)
                .select_related('assignment_command_types')
                .prefetch_related('extension_lexis_link')
                .prefetch_related('extension_lexis_link__term_link')

                )

