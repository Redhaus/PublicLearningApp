
# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

# from categories.models import ReadingCategory
from categories.models import ReadingCategory, ContinualGoalStandardType, ExtensionCommandType

from .category_serializers import ReadingCategorySerializer, GoalStandardTypeSerializer, ExCommandTypeSerializer
from django.db import connection


class ReadingCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # Dev snippet to count how many queries
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print('Queries Counted: {}'.format(len(connection.queries)))
        return response

    # fetch all lexis items to setup queryset
    queryset = ReadingCategory.objects.all()

    # set serializer class
    serializer_class = ReadingCategorySerializer

    # filter reading categories
    # select_related fetches indivdual FK
    # prefetch_related fetches multiple FK items
    def get_queryset(self):
        return (ReadingCategory.objects)





class GoalStandardTypeViewSet(viewsets.ModelViewSet):

    # Dev snippet to count how many queries
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print('Queries Counted: {}'.format(len(connection.queries)))
        return response

    # fetch all lexis items to setup queryset
    queryset = ContinualGoalStandardType.objects.all()

    # set serializer class
    serializer_class = GoalStandardTypeSerializer

    # filter reading categories
    # select_related fetches indivdual FK
    # prefetch_related fetches multiple FK items
    # def get_queryset(self):
    #     return (ReadingCategory.objects)


class ExCommandTypeViewSet(viewsets.ModelViewSet):

    # Dev snippet to count how many queries
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print('Queries Counted: {}'.format(len(connection.queries)))
        return response


    # fetch all lexis items to setup queryset
    queryset = ExtensionCommandType.objects.all()

    # set serializer class
    serializer_class = ExCommandTypeSerializer