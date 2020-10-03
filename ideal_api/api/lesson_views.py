from django.shortcuts import render
# from django_auto_prefetching import AutoPrefetchViewSetMixin
# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

from teacher_lessons.models import UserLesson, ClassSubject


from .lesson_serializers import UserLessonSerializer, ClassNameSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import connection
# from django_filters import rest_framework as filters





# from django_filters import rest_framework as filters


# AssignmentType Filter
# class LexisFilter(filters.FilterSet):


    # single filter
    # topics = filters.CharFilter(lookup_expr='icontains')

    # multiple choice filter
    # TOPIC_LIST = (
    #     ('device', 'device'),
    #     ('essential', 'essential'),
    #     ('common', 'common'),
    #     ('concept', 'concept'),
    #     ('person', 'person'),
    # )
    #
    # EVENT_LIST = (
    #     ('aswl_e1', 'aswl_e1'),
    #     ('aswl_e2', 'aswl_e2'),
    #     ('aswl_e3', 'aswl_e3'),
    # )
    #
    # term = filters.CharFilter(lookup_expr='icontains')
    #
    # # multiple choice filter
    # icon_list__icons = filters.MultipleChoiceFilter(
    #     field_name="icon_list__icons",
    #     lookup_expr='contains',
    #     conjoined=True,  # uses AND instead of OR
    #     choices=TOPIC_LIST
    # )

    # def getEvents(self):


    # test = filters.MultipleChoiceFilter(
    #     field_name="related_events",
    #     lookup_expr='contains',
    #     conjoined=True,  # uses AND instead of OR
    #     choices=EVENT_LIST
    # )


    # assign model and field terms
    # class Meta:
    #     model = Lexis
    #     fields = ('term', 'event_collection', 'icon_list__icons', 'related_events__event_link')
        # fields = ('event_collection', 'related_events__event_link')








# class LexisViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):

class LessonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    # This shows how many queries
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print('Queries Counted: {}'.format(len(connection.queries)))
        return response


    # fetch all lexis items to setup queryset
    queryset = UserLesson.objects.all()

    # set serializer class
    serializer_class = UserLessonSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['instructor', 'class_link']




    # filterset_fields = ['event_collection', 'related_events__event_link']

    # uses django filters
    # filterset_fields = ['event_collection', 'term', 'icon_list__icons[]']
    # custom filterset class
    # filterset_class = LexisFilter


    # a way to add custom routes with data return
    # could be used to filter lexis by event
    @action(methods=['get'], detail=False)
    def newest(self, request):
        # get a filtered queryset
        newest = self.get_queryset().order_by('term').first()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)


    # @action(methods=['get'], detail=False)
    # def explore(self, request):
    #     # get a filtered queryset
    #     newest = (Lexis.objects.values('term'))
    #     serializer = self.get_serializer_class()(newest)
    #     return Response(serializer.data)


    # filter api in viewset in this case 10 = aswl1_e1
    # select_related fetches indivdual FK
    # prefetch_related fetches multiple FK items
    def get_queryset(self):
        return (UserLesson.objects
                # .select_related('event_collection',)
                .select_related('instructor', )
                # .select_related('class_link', )

                # .prefetch_related('explorations')
                # .prefetch_related('lexis')
                # .prefetch_related('questions')

                # .prefetch_related('performances')
                # .prefetch_related('extensions')
                # .prefetch_related('goals')

                .all().order_by('-created')
                )

    #
    # event_collection = EventCollectionSerializer(many=False)
    # instructor = InstructorSerializer(many=False)
    # class_name = ClassNameSerializer(many=False)
    # explorations = ExplorationsSerializer(many=True)
    # lexis = LexisSerializer(many=True)
    # questions = QuestionsSerializer(many=True)
    # performances = PerformancesSerializer(many=True)
    # extensions = ExtensionsSerializer(many=True)
    # goals = GoalsSerializer(many=True)








class ClassNameViewSet(viewsets.ModelViewSet):

    # This shows how many queries
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print('Queries Counted: {}'.format(len(connection.queries)))
        return response


    # fetch all lexis items to setup queryset
    queryset = ClassSubject.objects.all()

    # set serializer class
    serializer_class = ClassNameSerializer
    filterset_fields = ['instructor']
    # permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]

    # filter api in viewset in this case 10 = aswl1_e1
    # select_related fetches indivdual FK
    # prefetch_related fetches multiple FK items
    def get_queryset(self):
        return (ClassSubject.objects
                .select_related('instructor', )
                # .all().order_by('-created')
                )