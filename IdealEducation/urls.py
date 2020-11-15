from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls import url
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from ideal_users.serializers import TeacherRegistrationView, SchoolRegistrationView, EditorRegistrationView
from ideal_users.views import AcceptInviteView, LoginCustomView

from search import views as search_views

# import index template view for vuejs
from home.views import IndexTemplateView



# API ENDPOINTS

from rest_framework.authtoken import views
from rest_framework import routers

# api views
from ideal_api.api.lexis_views import LexisViewSet
from ideal_api.api.goals_views import ContinualGoalViewSet
from ideal_api.api.events_views import EventOverviewViewSet
from ideal_api.api.extensions_views import ExtensionsViewSet
from ideal_api.api.keyquestions_views import KeyQuestionsViewSet
from ideal_api.api.performances_views import PerformancesViewSet
from ideal_api.api.readings_views import PrimaryFocusViewSet, FurtherExplorationsViewSet
from ideal_api.api.assignment_types_views import AssignmentTypeViewSet
from ideal_api.api.category_views import ReadingCategoryViewSet, ExCommandTypeViewSet, GoalStandardTypeViewSet
from ideal_api.api.lesson_views import LessonViewSet, ClassNameViewSet
from ideal_api.api.user_views import TeacherViewSet




# api router
router = routers.DefaultRouter()

# register views and routes
router.register(r'lexis', LexisViewSet)
router.register(r'goals', ContinualGoalViewSet)
router.register(r'event_overviews', EventOverviewViewSet)
router.register(r'extensions', ExtensionsViewSet)
router.register(r'questions', KeyQuestionsViewSet)
router.register(r'performances', PerformancesViewSet)
router.register(r'primary_focus', PrimaryFocusViewSet)
router.register(r'further_explorations', FurtherExplorationsViewSet)
router.register(r'assignment_types', AssignmentTypeViewSet)
router.register(r'reading_categories', ReadingCategoryViewSet)
router.register(r'extension_categories', ExCommandTypeViewSet)
router.register(r'goal_categories', GoalStandardTypeViewSet)
router.register(r'user_lessons', LessonViewSet)
router.register(r'class_name', ClassNameViewSet)
router.register(r'teacher_profile', TeacherViewSet)












urlpatterns = [

    url(r'^rest-auth/login/', LoginCustomView.as_view()),

    # API ROUTER ENDPOINTS
    url(r'^api/', include((router.urls, 'ideal_api'))),

    path('django-admin/', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('search/', search_views.search, name='search'),

    # DRF REST BROWSER URL /login/  /logout/
    url(r'^drf/', include('rest_framework.urls')),


    # REST-AUTH ENDPOINT  rest_auth urls
    url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/registration/teacher/$', TeacherRegistrationView.as_view(), name="rest_teacher_register"),
    url(r'^rest-auth/registration/school/$', SchoolRegistrationView.as_view(), name="rest_school_register"),
    url(r'^rest-auth/registration/editor/$', EditorRegistrationView.as_view(), name="rest_editor_register"),

    # invitations urls
    url(r'^invitations/accept-invite/(?P<key>\w+)/?$', AcceptInviteView.as_view(), name='accept-invite'),
    url(r'^invitations/', include('invitations.urls', namespace='invitations')),
    # invitations/send-invite/
    # invitations/send-json-invite/
    # invitations/accept-invite/

    # all auth urls needs to be placed last so they handle any incoming confirmation
    # allauth urls creates browser urls like yourwebsite.com/login/ /logout/ /signup/
    url(r'', include('allauth.urls')),

    # catch all for any url to direct to index
    url(r'^.*$', IndexTemplateView.as_view(), name="entry-point")

]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
