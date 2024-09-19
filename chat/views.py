from django.shortcuts import render

# INDEX ======================================================
def index(request):
    return render(request, "index.html")