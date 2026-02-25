from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:month>", views.journals_by_month, name="journals_by_month"),
    path("<int:month>", views.journals_by_number, name="journals_by_number"),
]
