from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab


from api.models import User, UserProfile

class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('name', 'siape', 'funcao', 'cpf')
        # fields = (
        #     'name',
        #     'siape',
        # )
            
class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('dtnascimento', 'endereco', 'cidade', 'cep', 'avatar')

    dtnascimento = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
    )