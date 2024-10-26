from django.shortcuts import render, redirect, get_object_or_404
from .models import Pembayaran
from penyimpanan.models import Katalog
from .forms import PaymentForm
from django.contrib import messages

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False) 
            payment.total_amount = form.cleaned_data['amount'] 
            payment.save()  
            print(f"Payment created with ID: {payment.id}") 

            request.session['product_id'] = payment.product.id
            request.session['amount'] = float(payment.total_amount)  # Simpan sebagai float
            
           
            return redirect('pembayaran:update_payment', payment_id=payment.id)

        else:
            print("Form is not valid:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PaymentForm()

    produk_list = Katalog.objects.all() #ambil dari wishlist
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
           
            payment.total_amount += form.cleaned_data['amount']
            payment.save() 
            messages.success(request, 'Payment updated successfully.')
    
            request.session.pop('product_id', None)
            request.session.pop('amount', None)
            return redirect('payment_history')

    return render(request, 'pembayaran/update_payment.html', {'form': form, 'payment': payment})


def delete_payment(request, payment_id):
    payment = get_object_or_404(Pembayaran, id=payment_id)
    if request.method == 'POST':
        payment.delete()
        messages.success(request, 'Payment deleted successfully.')
        return redirect('pembayaran:payment_history')

    return render(request, 'pembayaran/delete_payment.html', {'payment': payment})