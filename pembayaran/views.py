from django.shortcuts import render, redirect, get_object_or_404
from .models import Pembayaran
from penyimpanan.models import Katalog
from .forms import PaymentForm
from django.contrib import messages

# Create a new payment
def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)  # Simpan tanpa menyimpan ke database
            payment.total_amount = form.cleaned_data['amount']  # Atur total_amount ke nilai yang diterima
            payment.save()  # Simpan pembayaran

            print(f"Payment created with ID: {payment.id}")

            # Simpan product_id dan amount ke dalam sesi
            request.session['product_id'] = payment.product.id
            request.session['amount'] = float(payment.total_amount)  # Simpan sebagai float
            
            # Redirect ke halaman update_payment
            return redirect('update_payment', payment_id=payment.id)

        else:
            print("Form is not valid:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PaymentForm()

    produk_list = Katalog.objects.all()
    return render(request, 'pembayaran/create_payment.html', {
        'form': form,
        'produk_list': produk_list
    })

# Read payment history
def payment_history(request):
    payments = Pembayaran.objects.all()  # Mengambil semua pembayaran dari model Pembayaran
    return render(request, 'pembayaran/payment_history.html', {'payments': payments})

# Update payment status
def update_payment(request, payment_id):
    payment = get_object_or_404(Pembayaran, id=payment_id)  # Dapatkan objek pembayaran berdasarkan ID

    # Pre-fill the form with the data dari pembayaran yang diambil
    form = PaymentForm(instance=payment)

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            # Tambahkan amount baru ke total_amount yang sudah ada
            payment.total_amount += form.cleaned_data['amount']  # Tambahkan amount baru
            payment.save()  # Simpan perubahan
            messages.success(request, 'Payment updated successfully.')
            # Clear session data after saving
            request.session.pop('product_id', None)
            request.session.pop('amount', None)
            return redirect('payment_history')

    return render(request, 'pembayaran/update_payment.html', {'form': form, 'payment': payment})

# Delete payment
def delete_payment(request, payment_id):
    payment = get_object_or_404(Pembayaran, id=payment_id)
    if request.method == 'POST':
        payment.delete()
        messages.success(request, 'Payment deleted successfully.')
        return redirect('payment_history')

    return render(request, 'pembayaran/delete_payment.html', {'payment': payment})
