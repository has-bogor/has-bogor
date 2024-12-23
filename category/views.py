from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Category
import json
from django.shortcuts import render

@csrf_exempt
@require_POST
def create_category(request):
    try:
        data = json.loads(request.body)
        print(f'Received data: {data}')  # Debug statement
        category_name = data.get("nama_category", "").strip()

        if not category_name:
            print('Category name is missing.')  # Debug statement
            return JsonResponse({"success": False, "message": "Category name is required."}, status=400)

        category = Category.objects.create(nama_category=category_name)
        print(f'Created category: {category.nama_category} with ID: {category.id}')  # Debug statement
        return JsonResponse({
            "success": True,
            "message": "Category created successfully!",
            "category": {"id": category.id, "nama_category": category.nama_category}
        }, status=201)
    except json.JSONDecodeError:
        print('Invalid JSON input.')  # Debug statement
        return JsonResponse({"success": False, "message": "Invalid JSON input."}, status=400)
    except Exception as e:
        print(f'Error creating category: {e}')  # Debug statement
        return JsonResponse({"success": False, "message": str(e)}, status=500)

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

    # Fetch categories from the database with ordering and search
    if order == 'desc':
        categories = Category.objects.order_by('-nama_category')
    else:
        categories = Category.objects.order_by('nama_category')

    if search_query:
        categories = categories.filter(nama_category__icontains=search_query)
    
    # Format database categories as a list of dictionaries
    db_categories = [{"id": category.id, "nama_category": category.nama_category} for category in categories]

    # Combine initial dataset with database categories
    all_categories = db_categories

    # Sort the combined list based on the 'nama_category'
    all_categories.sort(key=lambda x: x['nama_category'], reverse=(order == 'desc'))

    return JsonResponse({
        "success": True,
        "categories": all_categories
    })

def category_management(request):
    return render(request, 'category/list_category.html')