from dal import autocomplete

from finhack_bca.users.models import User


class CustomerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = User.objects.filter(type='customer')

        if self.q:
            qs = qs.filter(username__istartswith=self.q)

        return qs