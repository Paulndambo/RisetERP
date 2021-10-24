from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard2/", views.dashboard2, name="dashboard2"),
    path("documents/", views.documents, name="documents"),
    path("customers/", views.customers, name="customers"),
    path("suppliers/", views.suppliers, name="suppliers"),
    path("countries/", views.countries, name="countries"),
    path("products/", views.products, name="products"),
    path("promotions/", views.promotions, name="promotions"),
    path("reports/", views.reports, name="reports"),
    path("expenses/", views.expenses, name="expenses"),
    path("payment-options/", views.payment_options, name="payment-options"),
]
