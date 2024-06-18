from django.urls import path
from .views import HomePageView, ShopPageView, AboutPAgeView, ServicePageView, BlogPageView, ContactPageView, CartPageView, ChekOutPageView, ThankYouPageview

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("shop/", ShopPageView.as_view(), name='shop'),
    path("about/", AboutPAgeView.as_view(), name='about'),
    path("service/", ServicePageView.as_view(), name='service'),
    path("blog/", BlogPageView.as_view(), name='blog'),
    path("contact/", ContactPageView.as_view(), name='contact'),
    path("cart/", CartPageView.as_view(), name='cart'),
    path("checkut/", ChekOutPageView.as_view(), name='checkout'),
    path("thankyou/", ThankYouPageview.as_view(), name='thankyou'),
]
