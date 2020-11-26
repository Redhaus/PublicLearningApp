
from rest_framework import viewsets
from django.contrib.auth.models import User
from .change_password_serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer


    # url http://127.0.0.1:8000/api/password_update/redhaus/ lookup by username
    # url http://127.0.0.1:8000/api/password_update/


# {
#     "username": "mariodev",
#     "password": "12345"
# }