from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("index/", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard2/", views.dashboard2, name="dashboard2"),

    #list views
    path("documents/", views.documents, name="documents"),
    path("customers/", views.customers, name="customers"),
    path("suppliers/", views.suppliers, name="suppliers"),
    path("countries/", views.countries, name="countries"),
    path("products/", views.products, name="products"),
    path("promotions/", views.promotions, name="promotions"),
    path("reports/", views.reports, name="reports"),
    path("expenses/", views.expenses, name="expenses"),
    path("payment-options/", views.payment_options, name="payment-options"),


    #create views
    path("new-product/", views.new_product, name="new-product"),
    path("new-supplier/", NewSupplier.as_view(), name="new-supplier"),
    path("new-promotion/", NewPromotion.as_view(), name="new-promotion"),
    path("new-customer/", NewCustomer.as_view(), name="new-customer"),
    path("new-country/", NewCountry.as_view(), name="new-country"),
    path("new-report/", NewReport.as_view(), name="new-report"),
    path("new-expense/", NewExpense.as_view(), name="new-expense"),
    path("new-document/", NewDocument.as_view(), name="new-document"),

    #Shopping views
    path('product/<slug>/', views.ProductView.as_view(), name='product'),
    #path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('order-summary/', views.OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', views.remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/', views.payment, name='payment')
]
