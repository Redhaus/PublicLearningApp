from django.shortcuts import render
from django_auto_prefetching import AutoPrefetchViewSetMixin

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

from performances.models import Performances, PerformanceFeatsLink
from .performances_serializers import PerformancesSerializer

from django.db import connection


from django_filters import rest_framework as filters


# AssignmentType Filter
class PerformanceFilter(filters.FilterSet):
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

    performance_title = filters.CharFilter(lookup_expr='icontains')

    # performance_feat_link = filters.CharFilter(field_name="performance_feat_link", method='custom_and_filter')

    # def custom_and_filter(self, queryset, name, value):
    #     # queryset.filter(name=1).first()
    #
    #     feat = PerformanceFeatsLink.objects.filter(id=value).first()
    #     print('FEAT: ', feat)
    #     print('CG: ', feat.continual_goal)
    #
    #
    #     # print('QUERY: ', queryset.)
    #
    #     return queryset

        # queryset passes lexis queryset
        # value passes [] values being searched for
        # name passes "icon_list__icons" field being searched
        # because value is an array set up conditional and fiter for each value
        # by chaining filters you get the "AND" functionality __in only provides or functionality

        # if len(value) == 1:
        #     return queryset.filter(**{
        #         name: value[0]
        #     })
        #
        # if len(value) == 2:
        #     return (queryset
        #             .filter(icon_list__icons=value[0])
        #             .filter(icon_list__icons=value[1])
        #             )
        #
        # if len(value) == 3:
        #     return (queryset
        #             .filter(icon_list__icons=value[0])
        #             .filter(icon_list__icons=value[1])
        #             .filter(icon_list__icons=value[2])
        #             )
        #
        # if len(value) == 4:
        #     return (queryset
        #             .filter(icon_list__icons=value[0])
        #             .filter(icon_list__icons=value[1])
        #             .filter(icon_list__icons=value[2])
        #             .filter(icon_list__icons=value[3])
        #             )
        #
        # if len(value) == 5:
        #     return (queryset
        #             .filter(icon_list__icons=value[0])
        #             .filter(icon_list__icons=value[1])
        #             .filter(icon_list__icons=value[2])
        #             .filter(icon_list__icons=value[3])
        #             .filter(icon_list__icons=value[4])
        #             )
        #
        # return


    # multiple choice filter
    # performance_feat_link = filters.MultipleChoiceFilter(
    #     field_name="icon_list__icons",
    #     lookup_expr='contains',
    #     conjoined=True,  # uses AND instead of OR
    #     choices=TOPIC_LIST
    # )

    # assign model and field terms
    class Meta:
        model = Performances
        fields = ('id', 'event_collection', 'performance_title', 'performance_feat_link')









class PerformancesViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):


    # This shows how many queries
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print('Queries Counted: {}'.format(len(connection.queries)))
        return response


    # fetch all lexis items to setup queryset
    queryset = Performances.objects.all()
    # queryset = Performances.objects.all().prefetch_related('performances__performance_feat_link', 'performances__performance_lexis_link')
    # queryset = Performances.objects.all().prefetch_related('performances__performance_feat_link', 'performance_lexis_link__lexis')

    # set serializer class
    serializer_class = PerformancesSerializer
    filterset_class = PerformanceFilter


    # filter api in viewset in this case 10 = aswl1_e1
    # select_related fetches indivdual FK
    # prefetch_related fetches multiple FK items
    #prefetch nested calls with double underscore __ in this case I am prefetching
    # all continual goals on all elements performance_feat_link elements
    def get_queryset(self):
        return (Performances.objects
                .select_related('event_collection',)
                .prefetch_related('performance_lexis_link')
                .prefetch_related('performance_lexis_link__term_link')

                .prefetch_related('performance_feat_link')
                .prefetch_related('performance_feat_link__continual_goal')

                .select_related('resource_link', )
                .select_related('student_sample', )
                )

