from django.shortcuts import render, redirect, get_object_or_404
from .models import Pembayaran
from penyimpanan.models import Katalog
from .forms import PaymentForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from promo.models import Promo

def create_payment(request):
    # Tangani GET request untuk menampilkan halaman create_payment dengan produk yang dipilih
    if request.method == 'GET':
        product_id = request.GET.get('product_id')  # Ambil product_id dari query parameter
        
        # Debugging: Cek apakah product_id diterima
        print(f"Received product_id: {product_id}")

        if not product_id:
            messages.error(request, 'Produk tidak valid. Silakan pilih produk dari katalog.')
            return redirect('authentication:home')

        # Ambil produk dari database
        product = get_object_or_404(Katalog, id=product_id)

        # Render halaman create_payment dengan produk yang dipilih
        return render(request, 'pembayaran/create_payment.html', {'product': product})
    
    # Tangani POST request untuk memproses pembayaran
    elif request.method == 'POST':
        product_id = request.POST.get('product_id')  # Ambil product_id dari POST data
        
        # Debugging: Cek apakah product_id diterima
        print(f"Product ID: {product_id}")

        if not product_id:
            messages.error(request, 'Produk tidak valid. Silakan pilih produk dari katalog.')
            return redirect('authentication:home')

        # Ambil produk dari database
        product = get_object_or_404(Katalog, id=product_id)

        # Buat form dengan data POST
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Simpan pembayaran tanpa komitmen dulu
            payment = form.save(commit=False)
            payment.product = product  # Tentukan produk yang dipilih
            payment.total_payment = form.cleaned_data['amount'] * product.harga  # Hitung total pembayaran
            payment.save()

            # Tampilkan pesan sukses
            messages.success(request, 'Pembayaran berhasil dibuat.')

            # Redirect ke halaman update_payment dengan ID pembayaran
            return redirect('pembayaran:update_payment', payment_id=payment.id)
        
        else:
            # Jika form tidak valid, tampilkan pesan error dan debug form
            print(f"Form Errors: {form.errors}")
            messages.error(request, 'Form tidak valid. Silakan periksa kembali.')
            return render(request, 'pembayaran/create_payment.html', {'form': form, 'product': product})

    else:
        # Jika bukan POST atau GET request, redirect ke homepage
        messages.error(request, 'Akses tidak valid.')
        return redirect('authentication:home')


def payment_history(request):
    payments = Pembayaran.objects.all()
    return render(request, 'pembayaran/payment_history.html', {'payments': payments})

def update_payment(request, payment_id):
    payment = get_object_or_404(Pembayaran, id=payment_id)
    form = PaymentForm(instance=payment)


    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            payment.total_payment = form.cleaned_data['amount'] * form.cleaned_data['product'].harga
            payment.save()
            messages.success(request, 'Pembayaran berhasil diperbarui.')
            request.session.pop('product_id', None)
            request.session.pop('amount', None)
            return redirect('pembayaran:payment_history')

    return render(request, 'pembayaran/update_payment.html', {'form': form, 'payment': payment})

def delete_payment(request, payment_id):
    payment = get_object_or_404(Pembayaran, id=payment_id)
    if request.method == 'POST':
        payment.delete()
        messages.success(request, 'Pembayaran berhasil dihapus.')
        return redirect('pembayaran:payment_history')

    return render(request, 'pembayaran/delete_payment.html', {'payment': payment})