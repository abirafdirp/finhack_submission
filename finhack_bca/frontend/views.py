from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from finhack_bca.store.models import Store
from finhack_bca.utils.models import Location
from finhack_bca.users.models import User
from finhack_bca.transaction.models import Transaction, CustomerTopUp
from finhack_bca.frontend.forms import TransactionConfirmationForm, CustomerTopUpForm


class StoreListView(ListView):
    model = Store
    template_name = 'pages/store_list.html'


def counter_list_view(request):
    context = {
        'counters': User.objects.filter(type='counter'),
        'locations': Location.objects.all()
    }
    template = 'pages/counter_list.html'
    return render(request, template, context)


class TransactionConfirmationView(LoginRequiredMixin, CreateView):
    template_name = 'pages/confirmation.html'
    model = Transaction
    form_class = TransactionConfirmationForm

    def get_success_url(self):
        return reverse("get_transaction_code")

    def form_valid(self, form):
        user = self.request.user
        form.instance.customer = user
        form.instance.date = timezone.now()
        form.instance.status = True
        return super(TransactionConfirmationView, self).form_valid(form)

    # get initial data from URL query parameters
    def get_initial(self):
        if self.request.GET:
            store_id = int(self.request.GET.get('id'))
            self.request.session['store'] = Store.objects.get(id=store_id).pk
            self.request.session['remarks'] = self.request.GET.get('remarks')
            self.request.session['amount'] = self.request.GET.get('amount')
        return {
            'store': self.request.session['store'],
            'remarks': self.request.session['remarks'],
            'amount': self.request.session['amount'],
        }


class GetLatestCodeView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/showcode.html'

    def get_context_data(self, **kwargs):
        context = {
            'latest_transaction': self.request.user.transactions.all().order_by('-id')[0]
        }
        return context


class CreateCustomerTopUpView(LoginRequiredMixin, CreateView):
    template_name = 'pages/customer_top_up.html'
    model = CustomerTopUp
    form_class = CustomerTopUpForm




