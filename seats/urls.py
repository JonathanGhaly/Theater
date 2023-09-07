from django.urls import path
from . import views

urlpatterns = [
    path('', views.seating_chart, name='seating_chart'),
    path('submit_reservation/', views.submit_reservation, name='submit_reservation'),

]
