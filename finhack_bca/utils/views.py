from dal import autocomplete

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from finhack_bca.users.models import User


class CustomerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = User.objects.filter(type='customer')

        if self.q:
            qs = qs.filter(username__istartswith=self.q)

        return qs

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'confirm transaction': reverse('api_confirm_transaction', request=request, format=format),
        'transactions': reverse('transaction-list', request=request, format=format),
        'counter top ups': reverse('counter_top_up-list', request=request, format=format),
        'customer top ups': reverse('customer_top_up-list', request=request, format=format),
        'stores': reverse('store-list', request=request, format=format),
        'registration': reverse('rest_register', request=request, format=None),
        'verify email': reverse('rest_verify_email', request=request, format=None),
        'password reset': reverse('rest_password_reset', request=request, format=None),
        'password reset confirm': reverse('rest_password_reset_confirm', request=request, format=None),
        'login': reverse('rest_login', request=request, format=None),
        'logout': reverse('rest_logout', request=request, format=None),
        'user': reverse('rest_user_details', request=request, format=None),
        'password change': reverse('rest_password_change', request=request, format=None),
    })