from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *
from django.views.generic import ListView, CreateView, DetailView, View, TemplateView
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import CheckoutForm, PaymentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import (
    render, get_object_or_404, redirect
)
# Create your views here.
class HomeView(ListView):
    model = Item
    template_name = "home.html"

class ProductView(DetailView):
    model = Item
    template_name = 'product-page.html'

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, "data/order-summary.html", context)

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order.")
            return redirect("/")

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False)
    order_qs = Order.objects.filter(
        user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(
                request, "Item quantity Updated")
            return redirect("order-summary")
        else:
            order.items.add(order_item)
            messages.info(
                request, "Item added to Cart")
            return redirect("order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(
            request, "Item added to Cart")
    return redirect("order-summary")

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(
                request, "Item removed from cart")
            return redirect("order-summary")
        else:
            messages.info(
                request, "Item not in your cart")
            return redirect("product", slug=slug)
    else:
        messages.info(
            request, "You do not have an active order")
        return redirect("product", slug=slug)

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(
                request, "Item quantity was updated")
            return redirect("order-summary")
        else:
            messages.info(
                request, "Item not in your cart")
            return redirect("product", slug=slug)
    else:
        messages.info(
            request, "You do not have an active order")
        return redirect("product", slug=slug)


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
    products = Item.objects.all()

    context = {
        "products": products
    }
    return render(request, "data/products.html", context)

class NewProduct(CreateView):
    model = Item
    fields = ["name", "quantity", "price", "re_order_level", "supplier", "category"]
    template_name = "data/new-product.html"

class NewSupplier(CreateView):
    model = Supplier
    fields = "__all__"
    template_name = "data/new-supplier.html"

class NewPromotion(CreateView):
    model = Promotion
    fields = "__all__"
    template_name = "data/new-promotion.html"

class NewDocument(CreateView):
    model = Document
    fields = "__all__"
    template_name = "data/new-document.html"

class NewCountry(CreateView):
    model = Country
    fields = "__all__"
    template_name = "data/new-country.html"

class NewReport(CreateView):
    model = Report
    fields = "__all__"
    template_name = "data/new-report.html"

class NewExpense(CreateView):
    model = Expense
    fields = "__all__"
    template_name = "data/new-expense.html"

class NewCustomer(CreateView):
    model = Customer
    fields = "__all__"
    template_name = "data/new-customer.html"

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

@login_required(login_url='/login')
def payment(request):
    form = PaymentForm()
    order = Order.objects.get(user=request.user, ordered=False)
    order_items = order.items.all()
    order_amount = order.order_total()

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            order_items.update(ordered=True)
            for item in order_items:
                item.save()
            order.ordered = True

            payment.save()
            return redirect("home")
    context = {
        "form": form,
        "order_amount": order_amount
    }
    return render(request, "payment.html", context)
