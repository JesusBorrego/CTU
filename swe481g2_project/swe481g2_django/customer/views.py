
# https://legionscript.medium.com/building-a-food-delivery-app-with-django-and-python-3-part-1-getting-started-and-setting-up-the-92460cc11baf
from django.shortcuts import render
from django.views import View
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')
