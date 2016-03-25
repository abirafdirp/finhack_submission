from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoObjectPermissions
from rest_framework.filters import DjangoObjectPermissionsFilter

from finhack_bca.utils.permissions import CustomObjectPermissions

from finhack_bca.transaction.models import Transaction, CounterTopUp, CustomerTopUp
from finhack_bca.transaction.serializers import TransactionSerializer, CounterTopUpSerializer, CustomerTopUpSerializer


class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_type = self.request.user.type
        if user_type == 'customer' or user_type == 'counter':
            queryset = Transaction.objects.filter(customer=self.request.user)
        if user_type == 'store':
            # if a store's user has more than one store
            store_ids = self.request.user.stores.all().values_list('id', flat=True)
            stores_ids_list = list(store_ids)
            queryset = Transaction.objects.filter(store__id__in=stores_ids_list)
        return queryset


class CounterTopUpViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CounterTopUpSerializer

    def get_queryset(self):
        user_type = self.request.user.type
        if user_type == 'counter':
            queryset = CounterTopUp.objects.filter(counter=self.request.user)
        else:
            queryset = None
        return queryset


class CustomerTopUpViewSet(viewsets.ModelViewSet):
    queryset = CustomerTopUp.objects.all()
    permission_classes = (CustomObjectPermissions,)
    serializer_class = CustomerTopUpSerializer
    filter_backends = (DjangoObjectPermissionsFilter,)
