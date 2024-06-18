from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart, Category, Testimonial, Product




class HomePageView(View):
    def get(self, request):
        products = Product.objects.order_by('-name')[:3]
        categorys = Category.objects.order_by('title')[:3]
        testusers = Testimonial.objects.all() 
        context = {
            'products':products,
            'categorys': categorys,
            'testusers': testusers
        } 
        return render(request, "index.html", context)
    

class ShopPageView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, 'shop.html', context)
    

    def post(self, request):
        product_name = request.POST['product_name']
        user_name = request.POST['username']
        title = Product.objects.get(name=product_name)
        user = User.objects.get(username=user_name)
        cart = Cart.objects.create(title=title, user=user)
        cart.save()
        return redirect('cart')

class AboutPAgeView(View):
    def get(self, request):
        testusers = Testimonial.objects.all()
        context = {
           'testusers':testusers
        }
        return render(request, 'about.html', context)
    

class ServicePageView(View):
   def get(self, request):
       products = Product.objects.order_by('-name')[:3]       
       testusers = Testimonial.objects.all()
       context = {
           'products': products,
           'testusers':testusers
       }
       return render(request, 'services.html', context)
   
class BlogPageView(View):
    def get(self, request):
        categorys = Category.objects.all()
        testusers = Testimonial.objects.all()
        context = {
            'categorys': categorys,
            'testusers': testusers
        }
        return render(request, 'blog.html', context)
    
class ContactPageView(View):
    def get(self, request):
        return render(request, 'contact.html')
    

class CartPageView(LoginRequiredMixin, View):
    def get(self, request):
        username = request.user.username
        user = User.objects.get(username=username)
        user_cart = Cart.objects.filter(user=user)
        user_cart = Cart.objects.filter(user=user)

        #obshiy narxni korish uchun
        total_price = 0
        for item in user_cart:
            total_price += item.title.price
        print(total_price)

        context = {
            "user_cart" : user_cart,
            'total_price' : total_price,
        }
        return render(request, 'cart.html', context)
    
class ChekOutPageView(LoginRequiredMixin, View):
    def get (self, request):
        username = request.user.username
        user = User.objects.get(username=username)
        user_cart = Cart.objects.filter(user=user)
        user_cart = Cart.objects.filter(user=user)

        #obshiy narxni korish uchun
        total_price = 0
        for item in user_cart:
            total_price += item.title.price
        print(total_price)

        context = {
            "user_cart" : user_cart,
            'total_price' : total_price,
        }
        return render(request, 'checkout.html', context)
    
class ThankYouPageview(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'thankyou.html')