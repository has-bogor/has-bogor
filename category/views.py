from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Category
import json

@csrf_exempt
@require_POST
def create_category(request):
    data = json.loads(request.body)
    category_name = data.get("nama_category", "").strip()
    
    if not category_name:
        return JsonResponse({"success": False, "message": "Category name is required."})
    
    category = Category.objects.create(nama_category=category_name)
    return JsonResponse({
        "success": True,
        "message": "Category created successfully!",
        "category": {"id": category.id, "nama_category": category.nama_category}
    })

@csrf_exempt
@require_http_methods(["PUT"])
def update_category(request, id):
    category = get_object_or_404(Category, id=id)
    data = json.loads(request.body)
    category_name = data.get("nama_category", "").strip()
    
    if not category_name:
        return JsonResponse({"success": False, "message": "Category name cannot be empty."})
    
    category.nama_category = category_name
    category.save()
    return JsonResponse({
        "success": True,
        "message": "Category updated successfully!",
        "category": {"id": category.id, "nama_category": category.nama_category}
    })

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return JsonResponse({
        "success": True,
        "message": "Category deleted successfully!"
    })

@require_GET
def list_categories_ordered(request):
    order = request.GET.get('order', 'asc')
    search_query = request.GET.get('search', '').strip()

    if order == 'desc':
        categories = Category.objects.order_by('-nama_category')
    else:
        categories = Category.objects.order_by('nama_category')

    # Apply search filter if search query is provided
    if search_query:
        categories = categories.filter(nama_category__icontains=search_query)
    
    categories_data = [{"id": category.id, "nama_category": category.nama_category} for category in categories]
    return JsonResponse({
        "success": True,
        "categories": categories_data
    })
