#-*- coding: utf8 -*-
from django import forms

from pinnokio_test.contact.models import Person


class PersonEditForm(forms.ModelForm):
    class Meta:
        model = Person
