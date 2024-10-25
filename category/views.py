from django.shortcuts import get_object_or_404, render, redirect
from .models import Category
from .forms import CategoryForm

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_category')
    else:
        form = CategoryForm()
    return render(request, 'category/create_category.html', {'form': form})

def list_category(request):
    categories = Category.objects.all()
    return render(request, 'category/list_category.html', {'categories': categories})

def update_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list_category')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/update_category.html', {'form': form})

def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('list_category')
    return render(request, 'category/delete_category.html', {'categories': category})