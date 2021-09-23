from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CouponAPI,CheckoutCart


router = DefaultRouter()
router.register('coupon',CouponAPI,basename='service')
router.register('checkout',CheckoutCart,basename='Checkout')


urlpatterns = [
    path('', include(router.urls)),
]