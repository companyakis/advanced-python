from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Main page")

def products(request):
    return HttpResponse("Our products")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("mainpage", home),
    path("products", products)
]
