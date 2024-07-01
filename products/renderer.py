from django import forms
from django.forms.widgets import RadioSelect

class CustomRadioSelect(RadioSelect):
    template_name = "customradio.html"
