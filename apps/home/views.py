from django.shortcuts import render, redirect
from .models import Item, Wish
from ..main.models import User
from django.contrib import messages

def index(request):
    if 'user_id' in request.session:
        user=request.session['user_id']
        context={
            'items': Item.objects.exclude(wishers__wisher_id=user),
            'wishes': Wish.objects.filter(wisher_id=user),
            'all': Wish.objects.all()
        }
    return render(request,'home/index.html', context)

def add_item(request):
    if request.method == 'POST':
        wish=request.POST['wish_name']
        if len(wish)>3:
            items=Item.objects.create(title=wish, user_id=request.session['user_id'])
            Wish.objects.create(wish_id=items.id, wisher_id=request.session['user_id'])
            return redirect('home:home')
        else:
             messages.add_message(request,messages.ERROR,'Item must be at least 3 characters')
             return redirect('home:add')
            

    return render(request,'home/add.html')

def add_wish(request, wish_id):
    Wish.objects.create(wish_id=wish_id, wisher_id=request.session['user_id'])
    return redirect('home:home')
def remove_wish(request, wish_id):
    Wish.objects.get(wish_id=wish_id, wisher_id=request.session['user_id']).delete()
    return redirect('home:home')

def item(request, item_id):
    context={
        'item': Item.objects.get(id=item_id),
        'wish': Wish.objects.filter(wish_id=item_id)
    }
    return render(request, 'home/item.html', context)

def delete(request, item_id):
    Item.objects.get(id=item_id, user_id=request.session['user_id']).delete()
    return redirect('home:home')
