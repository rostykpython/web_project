from django.forms import ModelForm
from .models import AddressBook
from django.forms.widgets import SelectDateWidget
from datetime import datetime


class AddAddressBook(ModelForm):
    class Meta:
        model = AddressBook
        fields = ['name', 'surname', 'phone', 'email', 'street', 'birthday']
        widgets = {
            'birthday': SelectDateWidget(
                years=[year for year in range(1970, datetime.now().year + 1)]
            )
        }
