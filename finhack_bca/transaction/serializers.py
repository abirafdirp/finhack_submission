from rest_framework import serializers

from finhack_bca.transaction.models import Transaction, CounterTopUp, CustomerTopUp


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


class CounterTopUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = CounterTopUp
        fields = '__all__'


class CustomerTopUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerTopUp
        fields = '__all__'


class ConfirmTransactionSerializer(serializers.Serializer):
    transaction_code = serializers.UUIDField()
