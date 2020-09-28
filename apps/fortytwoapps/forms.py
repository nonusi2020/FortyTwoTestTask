from django import forms
from apps.fortytwoapps.models import Contact
from datetime import date
from django.core.exceptions import ValidationError


def validate_dob(value):
    today = date.today()
    if value >= today:
        raise ValidationError(
            'Date greater than today'
        )


class UpdateContactForm(forms.ModelForm):

    formctrclass = 'form-control'
    name = forms.CharField(widget=forms.widgets.TextInput(
        attrs={
            'class': formctrclass,
            'required': True,
            'data-required-error': 'Name is required.'
        }
    ))
    lastname = forms.CharField(widget=forms.widgets.TextInput(
        attrs={
            'class': formctrclass,
            'required': True,
            'data-required-error': 'LastName is required.'
        }
    ))
    dateofbirth = forms.DateField(widget=forms.widgets.DateInput(
        format='%Y-%m-%d',
        attrs={
            'class': 'calendar-widget form-control',
            'required': True,
            'data-dateofbirth': "dateofbirth"
        }
    ), validators=[validate_dob])
    bio = forms.CharField(widget=forms.widgets.Textarea(
        attrs={
            'class': formctrclass
        }
    ), required=False)
    email = forms.EmailField(widget=forms.widgets.EmailInput(
        attrs={
            'class': formctrclass
        }
    ), required=False)
    jabber = forms.CharField(widget=forms.widgets.TextInput(
        attrs={
            'class': formctrclass
        }
    ), required=False)
    skype = forms.CharField(widget=forms.widgets.TextInput(
        attrs={
            'class': formctrclass
        }
    ), required=False)
    othercontacts = forms.CharField(widget=forms.widgets.Textarea(
        attrs={
            'class': formctrclass
        }
    ), required=False)

    class Meta:
        model = Contact
        fields = '__all__'
