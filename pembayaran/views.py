from django.shortcuts import get_object_or_404, render, redirect
from .models import Pembayaran
from .forms import PembayaranForm

def create_pembayaran(request):
    if request.method == 'POST':
        form = PembayaranForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_pembayaran')
    else:
        form = PembayaranForm()
    return render(request, 'pembayaran/create_pembayaran.html', {'form': form})

def list_pembayaran(request):
    pembayarans = Pembayaran.objects.all()
    return render(request, 'pembayaran/list_pembayaran.html', {'pembayarans': pembayarans})

def update_pembayaran(request, id):
    pembayaran = get_object_or_404(Pembayaran, id=id)
    if request.method == 'POST':
        form = PembayaranForm(request.POST, instance=pembayaran)
        if form.is_valid():
            form.save()
            return redirect('list_pembayaran')
    else:
        form = PembayaranForm(instance=pembayaran)
    return render(request, 'pembayaran/update_pembayaran.html', {'form': form})

def delete_pembayaran(request, id):
    pembayaran = get_object_or_404(Pembayaran, id=id)
    if request.method == 'POST':
        pembayaran.delete()
        return redirect('list_pembayaran')
    return render(request, 'pembayaran/delete_pembayaran.html', {'pembayaran': pembayaran})
