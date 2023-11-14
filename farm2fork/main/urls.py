from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [

    
    path('', views.landing, name='landing'),
    path('index.html', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('blog.html', views.blog, name='blog'),
    path('blog-first.html', views.blog_first, name='blog-first'),
    path('blog-second.html', views.blog_second, name='blog-second'),
    path('blog-third.html', views.blog_third, name='blog-third'),
    path('cart.html', views.cart, name='cart'),
    path('checkout.html', views.checkout, name='checkout'),
    path('contact.html', views.contact, name='contact'),
    path('product-single.html', views.product_single, name='product-single'),
    path('shop.html', views.shop, name='shop'),
    path('wishlist.html', views.wishlist, name='wishlist'),
    path("signup/", SignUpView.as_view(), name="signup"),
    
]