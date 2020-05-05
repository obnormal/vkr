from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from market.models import Order, Item


def user_page(request):

    orders = Item.objects.filter(orderitem__order__buyer_id=request.user.id).all()
    total_sum = 0
    for order in orders:
        total_sum += order.price
    context = {
        'user_info': request.user,
        'orders': orders,
        'total_sum': total_sum
    }
    return render(request, 'user_page.html', context)


def item_list(request):
    return redirect('market/items/')