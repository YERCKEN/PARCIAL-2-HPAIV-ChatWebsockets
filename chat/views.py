from django.shortcuts import render

# INDEX ======================================================
def index(request):
    return render(request, "index.html")

# ROOM =======================================================
def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})
