from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from api.models import User, UserProfile

class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'name',
            'siape',
        )
class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('cidade', 'endereco', 'avatar')