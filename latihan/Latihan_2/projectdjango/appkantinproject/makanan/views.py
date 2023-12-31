from django.shortcuts import render
from django.http import HttpResponse
from .models import Makanan
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import CartItem
from django.contrib import messages

# Create your views here.
def home(request):
    searchMakanan = request.GET.get('nama')
    if searchMakanan:
        makanans = Makanan.objects.filter(nama__icontains = searchMakanan)
    else:
        makanans = Makanan.objects.all()
    return render(request, 'home.html', {'searchMakanan' : searchMakanan, 'makanans' : makanans, 'name' : 'Kantin Stemba'})

def detail(request,makanan_id):
    makanan = get_object_or_404(Makanan, pk=makanan_id)
    return render(request, 'detail.html', {'makanan' : makanan})

def add_to_cart(request,makanan_id):
    makanan_id = int(makanan_id)
    makanan = get_object_or_404(Makanan, pk=makanan_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1)) # Jumlah pesanan dari form
        if quantity < 1:
            quantity = 1 # Minimal 1
        
        if makanan.stok >= quantity: # Cek apakah stok ada
            # cart_item jika sudah ada pesanan makanan tersebut
            # created jika belum ada pesanan makanan tersebut maka disimpan dan created = true
            cart_item, created = CartItem.objects.get_or_create(makanan=makanan)

            # If the item exists, update the quantity and item_total

            if not created:
                cart_item.quantity += quantity
                cart_item.item_total = cart_item.quantity * makanan.harga
                cart_item.save()
            else:
                cart_item.quantity = quantity
                cart_item.item_total = quantity * makanan.harga
                cart_item.save()
            # kurangi stok
            makanan.stok -= quantity
            makanan.save()
        else:
            # message jika stok kurang
            messages.error(request, 'Stok habis untuk makanan' + makanan.nama)

    return redirect('cart')

def view_cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.item_total for item in cart_items)
    return render(request, 'cart.html', {'cart_items' : cart_items, 'total_price' : total_price})

def remove_from_cart(request, makanan_id):
    makanan_id = int(makanan_id)
    makanan = Makanan.objects.get(pk=makanan_id)

    try:
        cart_item = CartItem.objects.get(makanan=makanan)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    
    return redirect('cart')