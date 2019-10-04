from django.forms import ModelForm
from .models import PersonalInfo

class PersonalInfoForm(ModelForm):
    class Meta:
        # the model to associate with the form
        model = PersonalInfo
        # a list of all the models' fields you want in the form
        fields = ['name', 'phone', 'address_ln1', 'address_ln2', 'city', 'state', 'zip', 'email']