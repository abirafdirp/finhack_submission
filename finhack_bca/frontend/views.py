from django.shortcuts import render
from django.views.generic import ListView

from finhack_bca.store.models import Store
from finhack_bca.users.models import User


class StoreListView(ListView):
    model = Store
    template_name = 'pages/store_list.html'


class CounterListView(ListView):
    model = User
    queryset = User.objects.filter(type='counter')
    template_name = 'pages/counter_list.html'
