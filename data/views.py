from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *
# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required(login_url='/login')
def index(request):
    return render(request, "index.html")

@login_required(login_url='/login')
def dashboard(request):
    return render(request, "dashboard.html")

@login_required(login_url='/login')
def dashboard2(request):
    return render(request, "dashboard2.html")

@login_required(login_url='/login')
def customers(request):
    customers = Customer.objects.all()

    context = {
        "customers": customers
    }
    return render(request, "data/customers.html", context)

@login_required(login_url='/login')
def suppliers(request):
    suppliers = Supplier.objects.all()

    context = {
        "suppliers": suppliers
    }
    return render(request, "data/suppliers.html", context)

@login_required(login_url='/login')
def products(request):
    products = Stock.objects.all()

    context = {
        "products": products
    }
    return render(request, "data/products.html", context)



@login_required(login_url='/login')
def countries(request):
    countries = Country.objects.all()

    context = {
        "countries": countries
    }
    return render(request, "data/countries.html", context)

@login_required(login_url='/login')
def promotions(request):
    promotions = Promotion.objects.all()

    context = {
        "promotions": promotions
    }
    return render(request, "data/promotions.html", context)


@login_required(login_url='/login')
def reports(request):
    reports = Report.objects.all()

    context = {
        "reports": reports
    }
    return render(request, "data/reports.html", context)

@login_required(login_url='/login')
def documents(request):
    documents = Document.objects.all()
    context = {
        "documents": documents
    }
    return render(request, "data/documents.html", context)

@login_required(login_url='/login')
def expenses(request):
    expenses = Expense.objects.all()
    context = {
        "expenses": expenses
    }
    return render(request, "data/expenses.html", context)

@login_required(login_url='/login')
def payment_options(request):
    payment_options = PaymentOption.objects.all()
    context = {
        "payment_options": payment_options
    }
    return render(request, "data/payment-options.html", context)
