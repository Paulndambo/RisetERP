from django import template
from data.models import Item

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Stock.objects.filter(
            user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0
