from django.shortcuts import render,redirect,get_object_or_404
from store.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)#get product
    #check if user is authenticated
    if current_user.is_authenticated:
        product_variation=[]
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                try:
                    variation = Variation.objects.get(product=product,variation_category__iexact=key,variation_value__iexact=value)
                    product_variation.append(variation)

                except:
                    pass
        
        is_cart_item_exists=CartItem.objects.filter(product=product,user=current_user).exists()
        if is_cart_item_exists:
            cart_item=CartItem.objects.filter(product=product,user=current_user)
            if product.stock<=cart_item[0].quantity:
                messages.error(request,'Out of stock')
                return redirect('cart')
            ex_var_list=[]
            id = []
            for item in cart_item:
                existing_variation= item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)
            if product_variation in ex_var_list:
                #increase cart item quantity
                index=ex_var_list.index(product_variation)
                item_id=id[index]
                item=CartItem.objects.get(product=product,id=item_id)
                item.quantity+=1
                item.save()
            else:
                #create new cart item
                item=CartItem.objects.create(product=product,quantity=1,user=current_user)
                if len(product_variation)>0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
        else:
            cart_item= CartItem.objects.create(
                product = product,
                quantity=1,
                user=current_user,
            )
            if len(product_variation)>0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)
            cart_item.save()
        return redirect('cart')
    #if the user is not authenticated
    else:
        product_variation=[]
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                try:
                    variation = Variation.objects.get(product=product,variation_category__iexact=key,variation_value__iexact=value)
                    product_variation.append(variation)
                    
                except:
                    pass
        
        try:
            cart= Cart.objects.get(cart_id=_cart_id(request))#get the cart using the cart id present in the session
        except Cart.DoesNotExist:
            cart=Cart.objects.create(
                cart_id = _cart_id(request)
            )
        cart.save()
        is_cart_item_exists=CartItem.objects.filter(product=product,cart=cart).exists()
        if is_cart_item_exists:
            cart_item=CartItem.objects.filter(product=product,cart=cart)
            #existing variations coming from database 
            #current variations -->product variation
            #item id --> database
            ex_var_list=[]
            id = []
            for item in cart_item:
                existing_variation= item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)
            if product_variation in ex_var_list:
                #increase cart item quantity
                index=ex_var_list.index(product_variation)
                item_id=id[index]
                item=CartItem.objects.get(product=product,id=item_id)
                item.quantity+=1
                item.save()
            else:
                #create new cart item
                item=CartItem.objects.create(product=product,quantity=1,cart=cart)
                if len(product_variation)>0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
        else:
            cart_item= CartItem.objects.create(
                product = product,
                quantity=1,
                cart= cart,
            )
            if len(product_variation)>0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)
            cart_item.save()
        return redirect('cart')

def remove_cart(request,product_id,cart_item_id):
    product = get_object_or_404(Product,id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item=CartItem.objects.get(product=product,user=request.user,id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item= CartItem.objects.get(product=product,cart=cart,id=cart_item_id)
        if cart_item.quantity>1:
            cart_item.quantity-=1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')

def remove_cart_item(request,product_id,cart_item_id):
    product = get_object_or_404(Product,id=product_id)
    if request.user.is_authenticated:
        cart_item=CartItem.objects.get(product=product,user=request.user,id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item= CartItem.objects.get(product=product,cart=cart,id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

def cart(request):
    total=0
    quantity =0  
    cart_items=None
    coupon_obj=None
    try:
        tax=0
        grand_total=0
        if request.user.is_authenticated:
            cart_items=CartItem.objects.filter(user=request.user,is_active=True)
        else:    
            cart= Cart.objects.get(cart_id=_cart_id(request))
            cart_items=CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            product = Product.objects.get(pk = cart_item.product.id)
            if product.stock<cart_item.quantity:
                cart_item.delete()
                return redirect('cart')
            else:
                total+=(cart_item.product.price * cart_item.quantity)
                quantity+= cart_item.quantity       
        tax = (0.02)*(total) 
        tax = round(tax,2)
        grand_total=total+tax
        
    except ObjectDoesNotExist:
        pass
    
    if request.method == 'POST':
        coupon = request.POST.get('coupon')     
        try: 
            try:
                coupon_obj = Coupon.objects.filter(coupon_code__icontains = coupon).get()
                print(coupon_obj)
            except:
                coupon_obj=None
                
            is_coupon_found = CouponDetail.objects.filter(coupon_id=coupon_obj.pk,user_id=request.user.pk).count()
        except:
            is_coupon_found = 0
            coupon_obj=None    
        
        if coupon_obj != None:
            if is_coupon_found == 0:
                CouponDetail.objects.create(user=request.user,coupon=coupon_obj).save()
                
                messages.success(request,"Coupon added")
                grand_total-=coupon_obj.discount_price 
            else:
                messages.warning(request,"Coupon redeemed")
                coupon_obj=None
                grand_total=total+tax
        else:
            messages.warning(request,"Coupon Not found")
            grand_total=total+tax
        
    context={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'coupon_obj':coupon_obj,
        'grand_total':grand_total,
    }
    return render(request,'store/cart.html',context)

@login_required(login_url='login')
def checkout(request):
    total=0
    quantity =0 
    cart_items=None
    try:
        tax=0
        grand_total=0
        if request.user.is_authenticated:
            cart_items=CartItem.objects.filter(user=request.user,is_active=True)
        else:    
            cart= Cart.objects.get(cart_id=_cart_id(request))
            cart_items=CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            quantity+= cart_item.quantity
        
        tax=(0.02)*(total) 
        grand_total=total+tax
    except ObjectDoesNotExist:
        pass
    context={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,
    }
    return render(request,'store/checkout.html',context)