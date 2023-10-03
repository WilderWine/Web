from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from factory.models import Furniture
from .cart import Cart
from .forms import CartAddProductForm
from django.core.exceptions import PermissionDenied


@require_POST
def cart_add(request, product_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("You do not have access to this page.")

    cart = Cart(request)
    product = get_object_or_404(Furniture, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('/')


def cart_remove(request, product_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("You do not have access to this page.")

    cart = Cart(request)
    product = get_object_or_404(Furniture, id=product_id)
    cart.remove(product)
    return redirect('/')


def cart_detail(request):
    if not request.user.is_authenticated :
        raise PermissionDenied("You do not have access to this page.")

    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
