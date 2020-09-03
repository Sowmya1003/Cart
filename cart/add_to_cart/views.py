from django.shortcuts import render
from .models import Item

def product_list(request):
    item1 = Item()
    item1.name = "Car"
    item1.desc = "On Sale"
    item1.price = "Price: $500"

    item2 = Item()
    item2.name = "Phone"
    item2.desc = "New Item"
    item2.price = "Price: $40"

    item3 = Item()
    item3.name = "Car"
    item3.desc = " For Very Smooth Driving"
    item3.price = "Price: $500"

    item4 = Item()
    item4.name = "Car"
    item4.desc = "On Sale"
    item4.price = "Price: $40"


    item5 = Item()
    item5.name = "Phone"
    item5.desc = "New Item"
    item5.price = "Price: $500"

    
    item6 = Item()
    item6.name = "Car"
    item6.desc = " For Very Smooth Driving"
    item6.price = "Price: $40"

    
    items = [item1,item2,item3,item4,item5,item6]

    return render(request,'home.html', {'items': items})

def view_cart(request):
    return render(request,'view_cart.html')
