from django.shortcuts import render
from django.http import HttpResponse
from .models import Barang
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import CartItem
from django.contrib import messages


# Create your views here.
def home(request):
    searchBarang = request.GET.get('nama')
    if searchBarang:
        barangs = Barang.objects.filter(nama__icontains = searchBarang)
    else:
        barangs = Barang.objects.all()
    return render(request, 'home.html', {'searchBarang' : searchBarang, 'barangs' : barangs, 'name' : 'Toko SIJA'})

def detail(request,barang_id):
    barang = get_object_or_404(Barang, pk=barang_id)
    return render(request, 'detail.html', {'barang' : barang})

def add_to_cart(request,barang_id):
    barang_id = int(barang_id)
    barang = get_object_or_404(Barang, pk=barang_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1)) # Jumlah pesanan dari form
        if quantity < 1:
            quantity = 1 # Minimal 1
        
        if barang.stok >= quantity: # Cek apakah stok ada
            # cart_item jika sudah ada pesanan barang tersebut
            # created jika belum ada pesanan barang tersebut maka disimpan dan created = true
            cart_item, created = CartItem.objects.get_or_create(barang=barang)

            # If the item exists, update the quantity and item_total

            if not created:
                cart_item.quantity += quantity
                cart_item.item_total = cart_item.quantity * barang.harga
                cart_item.save()
            else:
                cart_item.quantity = quantity
                cart_item.item_total = quantity * barang.harga
                cart_item.save()
            # kurangi stok
            barang.stok -= quantity
            barang.save()
        else:
            # message jika stok kurang
            messages.error(request, 'Stok habis untuk barang' + barang.nama)

    return redirect('cart')

def view_cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.item_total for item in cart_items)
    return render(request, 'cart.html', {'cart_items' : cart_items, 'total_price' : total_price})

def remove_from_cart(request, barang_id):
    barang_id = int(barang_id)
    barang = Barang.objects.get(pk=barang_id)

    try:
        cart_item = CartItem.objects.get(barang=barang)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    
    return redirect('cart')

# def hasil_cart(request,):
#     return render(request, 'hasil_cart.html')

