from django import template



register = template.Library()

@register.filter
def sum_of_amounts(amount_received_set):
  total = sum(amount_received.amount for amount_received in amount_received_set.all())
  return total / 10

@register.filter
def sum_amounts(amount_received_set):
    return sum(amount_received.amount for amount_received in amount_received_set.all())


    


