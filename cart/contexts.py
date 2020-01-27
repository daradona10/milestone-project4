from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity_size in cart.items():
        if isinstance(quantity_size, int):
            product = get_object_or_404(Product, pk=id)
            quantity = quantity_size
            total += quantity * product.price
            product_count += quantity
            cart_items.append({'id': id, 'quantity': quantity, 'product': product})
        else:
            product = get_object_or_404(Product, pk=id)
            quantity = quantity_size[0]
            size = quantity_size[1]
            total += quantity * product.price
            product_count += quantity
            cart_items.append({'id': id, 'quantity': quantity, 'size': size, 'product': product})
    
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
