from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name ="index"),
    path("<int:cal_id>", views.cal , name ="cal"),
    path("<int:cal_id>/book", views.book, name="book")
]