from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('booking/', views.booking_view, name='booking'),
    path('reserve/', views.create_reservation, name='create_reservation'),
    path('<str:page_name>', views.page_view, name='page_view'),
]
