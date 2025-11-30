from django.contrib import admin

# Register your models here.

from .models import Profile, SellerRating, CartItem, Cart, OrderItem, Order, \
    Buyer, Review, Provider, Payment, Transaction, Booking, Product, Service, Seller, Person, \
    User, Booking, Review, History,  Feedback

admin.site.register(Profile)
admin.site.register(SellerRating)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(OrderItem)      
admin.site.register(Order)
admin.site.register(Buyer)
admin.site.register(Review)
admin.site.register(Provider)
admin.site.register(Payment)
admin.site.register(Transaction)
admin.site.register(Booking)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Seller)
admin.site.register(History)
admin.site.register(Feedback)
admin.site.register(Person)