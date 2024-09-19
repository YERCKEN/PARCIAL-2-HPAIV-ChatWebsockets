from django.urls import path
from . import views

urlpatterns = [
                                    # Index
    path("", views.index, name="index"),
                                                # Room
    path("<str:room_name>/", views.room, name="room"),
]