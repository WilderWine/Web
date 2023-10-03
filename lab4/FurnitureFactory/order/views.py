from django.shortcuts import render
from .models import OrderItem
from cart.cart import Cart
from factory.models import Client, Furniture
from .models import Order
from django.core.exceptions import PermissionDenied


def order_create(request):
    """
    create order(deal)
    """
    if not request.user.is_authenticated:
        raise PermissionDenied("You do not have access to this page.")


    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(client=Client.objects.filter(email=request.user.email).first())
        a = 5


        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
            item['product'].purchase_count += item['quantity']
            item['product'].save()

        # clear bush
        cart.clear()
        return render(request,
                      'order/created.html',
                      {'order': order})

    return render(request,
                  'order/create.html',
                  {'cart': cart})
