from django.contrib.auth import backends, get_user_model
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from .models import CustomUser

class ModelBackend(backends.ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
