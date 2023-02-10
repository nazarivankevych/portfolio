from django.shortcuts import render

def front(request):
    context = { }
    return render(request, "../../frontend/build/index.html", context)

