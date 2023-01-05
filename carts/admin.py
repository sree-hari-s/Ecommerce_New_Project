from django.contrib import admin
from .models import *
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display=('cart_id','date_added')
    
class CartItemAdmin(admin.ModelAdmin):
    list_display=('product','cart','quantity','is_active')
    
class CouponAdmin(admin.ModelAdmin):
    list_display=('coupon_code', 'discount_price','is_expired', )
    
# admin.site.register(Cart,CartAdmin)
# admin.site.register(CartItem,CartItemAdmin)
admin.site.register(Coupon,CouponAdmin)
admin.site.register(CouponDetail)