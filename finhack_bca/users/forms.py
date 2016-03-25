from django import forms
from django.utils.translation import ugettext_lazy as _


class SignupForm(forms.Form):
    name = forms.CharField(max_length=30, label=_('Name'))
    mobile_number = forms.CharField(max_length=30)

    # TODO clean mobile_number

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.mobile_number = self.cleaned_data['mobile_number']
        user.save()
