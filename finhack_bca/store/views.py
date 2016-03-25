from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from finhack_bca.store.serializers import StoreSerializer
from finhack_bca.store.models import Store


class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
