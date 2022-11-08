from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_student, name="add"),
    path('delete/<int:id>/', views.delete_student, name="delete_data"),
    path('<int:id>', views.update_student, name="update_data"),
]
