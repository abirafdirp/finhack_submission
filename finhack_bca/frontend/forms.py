from django import forms
from dal import autocomplete

from finhack_bca.transaction.models import Transaction, CustomerTopUp
from finhack_bca.users.models import User


class TransactionConfirmationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TransactionConfirmationForm, self).__init__(*args, **kwargs)
        self.fields['store'].disabled = True
        self.fields['remarks'].disabled = True
        self.fields['amount'].disabled = True

    class Meta:
        model = Transaction
        fields = ['store', 'remarks', 'amount']


class CustomerTopUpForm(forms.ModelForm):

    class Meta:
        model = CustomerTopUp
        fields = ['customer', 'amount']
        widgets = {
            'customer': autocomplete.ModelSelect2(url='customer_autocomplete')
        }