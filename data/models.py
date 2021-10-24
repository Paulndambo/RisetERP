from django.db import models
from django.utils import timezone
from django.conf import settings
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

class Stock(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField(default=0)
    price = models.FloatField()
    re_order_level = models.FloatField(default=0)
    receive_amount = models.FloatField(default=0)
    sell_amount = models.FloatField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def stock_price(self):
        return self.quantity * self.price

    def __str__(self):
        return self.name

class Promotion(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date_posted = models.DateField(default=timezone.now)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

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

class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="documents")
    date_uploaded = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

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

class PaymentOption(models.Model):
    title = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    date_added = models.DateField(default=timezone.now)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
