from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk, Pembayaran  
from .forms import PaymentForm

from django.contrib import messages

# Create a new payment
def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Create and save the payment object
            payment = form.save()
            print(f"Payment created with ID: {payment.id}")  # Tambahkan ini untuk debugging
            
            # Store the selected product and amount in the session
            request.session['product_id'] = payment.product.id
            request.session['amount'] = payment.amount
            
            try:
                return redirect('update_payment', payment_id=payment.id)  # Coba redirect
            except Exception as e:
                print(f"Error redirecting: {e}")  # Tangkap kesalahan redirect
                return render(request, 'pembayaran/create_payment.html', {'form': form, 'produk_list': Produk.objects.all()})
    else:
        form = PaymentForm()

    return render(request, 'pembayaran/create_payment.html', {'form': form, 'produk_list': Produk.objects.all()})

# Read payment history
def payment_history(request):
    payments = Pembayaran.objects.all() 
    return render(request, 'pembayaran/payment_history.html', {'payments': payments})

# Update payment status
def update_payment(request, payment_id):
    product_id = request.session.get('product_id')
    amount = request.session.get('amount')

    if product_id and amount:
        # Pre-fill the form with the session data
        form = PaymentForm(initial={'product': product_id, 'amount': amount})
    else:
        # Redirect to create_payment if session data is not available
        return redirect('create_payment')

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            # Clear session data after saving
            del request.session['product_id']
            del request.session['amount']
            return redirect('payment_history')

    return render(request, 'pembayaran/update_payment.html', {'form': form})

# Delete payment
def delete_payment(request, payment_id):
    payment = get_object_or_404(Pembayaran, id=payment_id)
    if request.method == 'POST':
        payment.delete()
        return redirect('payment_history')

    return render(request, 'pembayaran/delete_payment.html', {'payment': payment})