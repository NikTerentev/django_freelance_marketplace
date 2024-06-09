from django.urls import path

from .views import PerformerListView, PerformerDetailView, \
    PerformerCreateView, CustomerCreateView, handle_login, profile

urlpatterns = [
    path('', PerformerListView.as_view(), name='performer-list'),
    path('account-setup', handle_login, name='handle-login'),
    path('performer/<int:pk>/', PerformerDetailView.as_view(),
         name='performer-detail'),
    path('performer/create/', PerformerCreateView.as_view(),
         name='performer-create'),
    path('customer/create/', CustomerCreateView.as_view(),
         name='customer-create'),
    path('profile/', profile, name='profile'),
]
