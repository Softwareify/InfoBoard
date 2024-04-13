from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        """
        Class Meta is inner class of UserLoginForm Class Meta is used to change behaviour of model fields.

        :param model: create a User model
        :param fields: parameter define a field of model
        """

        model = User
        fields = ["username", "password"]
