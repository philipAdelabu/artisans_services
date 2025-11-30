from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Product, Service, Cart, Order, Seller, 


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    social_links = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name
    

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)
    store_description = models.TextField()

    def __str__(self):
        return self.store_name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)

    def __str__(self):
        return self.nameBuyer 
    
    
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name   


class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    buyer = models.ForeignKey('Buyer', on_delete=models.CASCADE)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    scheduled_date = models.DateTimeField()
    status = models.Choices('Pending', 'Confirmed', 'Completed', 'Cancelled')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking of {self.service.name} by {self.buyer.user.username}"  
    

class Payment(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    status = models.Choices('Pending', 'Completed', 'Failed')
    transaction_id = models.CharField(max_length=100, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment of {self.amount} for booking {self.booking.id}"


# Other potential tables: [messages, categories, addresses, service_availabiblity, notificaton]
class Review(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.provider.company_name}"
    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, through='CartItem')
    products = models.ManyToManyField(Product, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Cart of {self.user.username} created on {self.created_at}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)     

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order of {self.user.username} on {self.created_at}"
    

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.TextField()

    def __str__(self):
        return self.user.username

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in cart of {self.cart.user.username}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.quantity} of {self.product.name} in order of {self.order.user.username}" 
    

class SellerRating(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating of {self.rating} for {self.seller.store_name}"
    

class Transaction(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    description = models.TextField()
    mode = models.CharField(max_length=50)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.Choices('Success', 'Failed', 'Pending')

    def __str__(self):
        return f"Transaction of {self.amount} on {self.transaction_date}"