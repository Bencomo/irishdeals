from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """cart page that is going to be rendered"""
    return render(request, "cart.html")
    
    
def add_to_cart(request, id):
    """Add +1 product"""
    if int(len(request.POST.get('quantity'))) == 0:
        # raise error here
        print('Error raised')
        
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))
    
    
def adjust_cart(request, id):
    """Edit quantity of product"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    """
    Quantity has to be higher than zero - if there is nothing in the cart then there's no adjustment
    """
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))