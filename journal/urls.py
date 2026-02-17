from django.urls import path
from . import views

urlpatterns = [
    path("<month>", views.journals_by_month)
]
