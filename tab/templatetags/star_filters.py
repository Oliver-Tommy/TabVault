from django import template

register = template.Library()

@register.filter
def stars_full(rating):
    """Returns a string of full stars (★) based on the rating."""
    return "★" * rating

@register.filter
def stars_empty(rating):
    """Returns a string of empty stars (☆) for the remaining out of 5."""
    return "☆" * (5 - rating)
