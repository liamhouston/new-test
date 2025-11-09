from django.contrib.auth.forms import UserCreationForm
from music_yearbook.models import Author


class SignupForm(UserCreationForm):

    class Meta:
        model = Author
        fields = ("username", "password1", "password2")