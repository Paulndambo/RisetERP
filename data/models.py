from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
# Create your models here.
GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Binary", "Binary"),
)

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("suppliers")

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    price = models.FloatField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    id_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
    address = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("customers")

COUNTINENT_CHOICES = (
    ("ASIA", "ASIA"),
    ("EUROPE", "EUROPE"),
    ("AFRICA", "AFRICA"),
    ("N.AMERICA", "N.AMERICA"),
    ("S.AMERICA", "S.AMERICA"),
    ("AUSTRALIA", "AUSTRALIA"),
)

class Country(models.Model):
    name = models.CharField(max_length=200)
    continent = models.CharField(max_length=100, choices=COUNTINENT_CHOICES)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("countries")

class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField(default=0)
    price = models.FloatField()
    discount_price = models.FloatField(default=0)
    re_order_level = models.FloatField(default=0)
    receive_amount = models.FloatField(default=0)
    sell_amount = models.FloatField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    def stock_price(self):
        return self.quantity * self.price

    #def get_absolute_url(self):
    #    return reverse("products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'slug': self.slug
        })

class Promotion(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date_posted = models.DateField(default=timezone.now)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("promotions")

class Report(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to="reports", null=True, blank=True)
    date_reported = models.DateField(auto_now=True)

    def report_file(self):
        if self.file:
            return self.file
        else:
            return "No File"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("reports")

class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="documents")
    date_uploaded = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("documents")

class Expense(models.Model):
    title = models.CharField(max_length=200)
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recorded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recorders")
    expense_file = models.FileField(upload_to="expenses", blank=True, null=True)
    date_spend = models.DateField(default=timezone.now)

    def expense_pdf(self):
        if self.expense_file:
            return self.expense_file
        else:
            return "No File"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("expenses")

class PaymentOption(models.Model):
    title = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    date_added = models.DateField(default=timezone.now)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price

    def get_item_total(self):
        return self.item.price * self.quantity


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(
        auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

    def order_total(self):
        order_total_items = []
        for order_item in self.items.all():
            order_total_items.append(order_item.get_item_total())
            print(order_total_items)
            sum_total = 0
            for item in order_total_items:
                sum_total += item
                return sum_total

"""
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total = total + order_item.get_final_price()
        return total
"""

class Payment(models.Model):
    amount = models.FloatField(default=0)
    payment_method = models.ForeignKey(PaymentOption, on_delete=models.SET_NULL, null=True)
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)
