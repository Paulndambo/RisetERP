from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from . models import Payment, PaymentOption

choices = PaymentOption.objects.all().values_list('title', 'title')
payment_choices = []
for choice in choices:
    payment_choices.append(choice)

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal'),
    ('M-pesa', 'M-pesa'),
    ('Cash', 'Cash'),
    ('Airtel Money', 'Airtel Money'),
    ('T-kash', 'T-kash'),
)


class CheckoutForm(forms.Form):
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=PAYMENT_CHOICES
    )

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
