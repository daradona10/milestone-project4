from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('size')

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = [int(cart[id][0]) + quantity, size]
    else:
        cart[id] = cart.get(id, [quantity, size])

    request.session['cart'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    print(request.POST)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = [quantity, cart[id][1]]
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))