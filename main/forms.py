from django import forms
from .models import Subscriber


class SubscriberForm(forms.ModeForm):
    class Meta:
        model = Subscriber
        field = ['email']