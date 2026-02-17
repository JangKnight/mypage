from django.urls import path
from . import views

urlpatterns = [
    path("<str:month>", views.journals_by_month),
    path("<int:month>", views.journals_by_number)
]
