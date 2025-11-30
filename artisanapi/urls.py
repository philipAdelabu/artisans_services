from django.urls import path, include
from rest_framework import routers
from artisanapi import views


router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'seller-ratings', views.SellerRatingViewSet)
router.register(r'cart-items', views.CartItemViewSet)
router.register(r'carts', views.CartViewSet)
router.register(r'order-items', views.OrderItemViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'buyers', views.BuyerViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'providers', views.ProviderViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'bookings', views.BookingViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'sellers', views.SellerViewSet)
router.register(r'services', views.ServiceViewSet)



urlpatterns = [
    path("/", views.HomePage(), name="home-page"),
    path('api/v1/', include(router.urls)),
]