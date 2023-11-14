from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def landing(request):
    template = loader.get_template('landing.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def blog(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())

def blog_first(request):
    template = loader.get_template('blog-first.html')
    return HttpResponse(template.render())

def blog_second(request):
    template = loader.get_template('blog-second.html')
    return HttpResponse(template.render())

def blog_third(request):
    template = loader.get_template('blog-third.html')
    return HttpResponse(template.render())

def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render())

def checkout(request):
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def product_single(request):
    template = loader.get_template('product-single.html')
    return HttpResponse(template.render())

def shop(request):
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())

def wishlist(request):
    template = loader.get_template('wishlist.html')
    return HttpResponse(template.render())
