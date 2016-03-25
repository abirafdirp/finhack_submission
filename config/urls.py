# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from rest_framework.routers import DefaultRouter

from finhack_bca.frontend import views
from finhack_bca.transaction.views import TransactionViewSet, CounterTopUpViewSet, CustomerTopUpViewSet


# API
router = DefaultRouter()
router.register(r'api/transactions', TransactionViewSet, base_name='Transaction')
router.register(r'api/countertopups', CounterTopUpViewSet, base_name='CounterTopUp')
router.register(r'api/customertopups', CustomerTopUpViewSet, base_name='CustomerTopUp')

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),
    url(r'^daftar-toko/$', views.StoreListView.as_view(), name="list-toko"),
    url(r'^daftar-counter/$', views.CounterListView.as_view(), name="list-counter"),
    url(r'^konfirmasi/$', views.TransactionConfirmationView.as_view(), name="transaction-confirmation"),
    url(r'^developer/$', TemplateView.as_view(template_name='pages/developer.html'), name='developer'),
    url(r'^konfirmasi/kode/$', views.GetLatestCodeView.as_view(), name='get-transaction-code'),

    # Django Admin, use {% url 'admin:index' %}
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include("finhack_bca.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^api/', include('rest_auth.urls')),
    url(r'^api/docs/', include('rest_framework_docs.urls')),
    url(r'^api/registration/', include('rest_auth.registration.urls')),
    url(r'^', include(router.urls)),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception("Permission Denied")}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
        url(r'^500/$', default_views.server_error),
    ]
