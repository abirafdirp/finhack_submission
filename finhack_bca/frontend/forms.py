from django import forms
from finhack_bca.transaction.models import Transaction


class ConfirmationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConfirmationForm, self).__init__(*args, **kwargs)
        self.fields['store'].disabled = True
        self.fields['remarks'].disabled = True
        self.fields['amount'].disabled = True

    class Meta:
        model = Transaction
        fields = ['store', 'remarks', 'amount']