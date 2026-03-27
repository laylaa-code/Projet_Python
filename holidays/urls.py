from django.urls import path
from . import views

urlpatterns = [
    path('', views.holidays_list, name='holidays_home'),  # <-- renommé pour cohérence
    path('add/', views.add_holiday, name='add_holiday'),
    path('edit/<int:id>/', views.edit_holiday, name='edit_holiday'),
    path('delete/<int:id>/', views.delete_holiday, name='delete_holiday'),
]