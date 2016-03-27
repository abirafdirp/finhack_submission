from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from dry_rest_permissions.generics import DRYPermissions

from finhack_bca.transaction.models import Transaction, CounterTopUp, CustomerTopUp
from finhack_bca.transaction.serializers import TransactionSerializer
from finhack_bca.transaction.serializers import CounterTopUpSerializer
from finhack_bca.transaction.serializers import CustomerTopUpSerializer
from finhack_bca.transaction.serializers import ConfirmTransactionSerializer


class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_type = self.request.user.type
        if user_type == 'customer' or user_type == 'counter':
            queryset = Transaction.objects.filter(customer=self.request.user)
        elif user_type == 'store':
            # if a store's user has more than one store
            store_ids = self.request.user.stores.all().values_list('id', flat=True)
            stores_ids_list = list(store_ids)
            queryset = Transaction.objects.filter(store__id__in=stores_ids_list)
        else:
            queryset = Transaction.objects.all()
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
    serializer_class = CustomerTopUpSerializer
    permission_classes = (DRYPermissions,)

    def get_queryset(self):
        user_type = self.request.user.type
        if user_type == 'counter':
            queryset = CustomerTopUp.objects.filter(counter=self.request.user)
        elif user_type == 'customer':
            queryset = CustomerTopUp.objects.filter(customer=self.request.user)
        else:
            queryset = None
        return queryset


@api_view(['POST'])
def confirm_transaction(request):
    serializer = ConfirmTransactionSerializer(data=request.data)
    if request.method == 'POST':
        if serializer.is_valid():
            transaction_code = request.data['transaction_code']
            transaction = Transaction.objects.get(transaction_code=transaction_code)
            if transaction.status:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
