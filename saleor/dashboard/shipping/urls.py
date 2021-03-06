from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.shipping_method_list, name='shipping-methods'),
    url(r'^add/$', views.shipping_method_edit, name='shipping-method-add'),
    url(r'^(?P<pk>\d+)/update/$', views.shipping_method_edit,
        name='shipping-method-update'),
    url(r'^(?P<pk>\d+)/$', views.shipping_method_detail,
        name='shipping-method-detail'),
    url(r'^(?P<pk>\d+)/delete/$',
        views.shipping_method_delete, name='shipping-method-delete'),

    url(r'^(?P<shipping_method_pk>\d+)/country/add/$',
        views.shipping_method_country_edit,
        name='shipping-method-country-add'),
    url(r'^(?P<shipping_method_pk>\d+)/country/(?P<country_pk>\d+)/update/$',
        views.shipping_method_country_edit,
        name='shipping-method-country-edit'),
    url(r'^(?P<shipping_method_pk>\d+)/country/(?P<country_pk>\d+)/delete/$',
        views.shipping_method_country_delete,
        name='shipping-method-country-delete'),
]
