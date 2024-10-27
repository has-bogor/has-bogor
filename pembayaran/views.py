from django.shortcuts import render, redirect, get_object_or_404
from .models import Pembayaran
from penyimpanan.models import Katalog
from .forms import PaymentForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from promo.models import Promo

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.total_payment = form.cleaned_data['amount'] * form.cleaned_data['product'].harga
            payment.save() 
            print(f"Payment created with ID: {payment.id}")
            messages.success(request, 'Pembayaran berhasil dibuat.')
            request.session.pop('product_id', None)
            request.session.pop('amount', None)
            return redirect('pembayaran:update_payment', payment_id=payment.id)

        else:
            print("Form is not valid:", form.errors)
            messages.error(request, 'Mohon perbaiki kesalahan berikut.')
    else:
        form = PaymentForm()

    produk_list = Katalog.objects.all()
    return render(request, 'pembayaran/create_payment.html', {
        'form': form,
        'produk_list': produk_list
    })

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