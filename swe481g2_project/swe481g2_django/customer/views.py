
# https://legionscript.medium.com/building-a-food-delivery-app-with-django-and-python-3-part-1-getting-started-and-setting-up-the-92460cc11baf
from django.shortcuts import render
from django.views import View
from .models import MenuItem, OrderModel, Category
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')
class Order(View):
    def get(self, request, *args, **kwargs):
        appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
        entres = MenuItem.objects.filter(category__name__contains='Entre')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')
        context = {
            'appetizers': appetizers,
            'entres': entres,
            'desserts': desserts,
            'drinks': drinks,
        }
        return render(request, 'customer/order.html', context)
    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
            }
            order_items['items'].append(item_data)

        price = 0
        item_ids = []
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(price=price)
        order.items.add(*item_ids)
        context = {
            'items': order_items['items'],
            'price': price
        }
        return render(request, 'customer/order_confirmation.html', context)
