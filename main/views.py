from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'tes' : 'tes'
    }

    return render(request, "main.html", context)