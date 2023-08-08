from django.urls import path
from . import views

app_name = "food"
urlpatterns = [
    path("", views.IndexClassView.as_view(), name="index"),
    path("item/", views.item, name="item"),
    # food/1
    path('<int:pk>/', views.FoodDetail.as_view(), name="detail"),
    # add items
    path('add/', views.create_item, name="create-item"),
    path('update/<int:id>/', views.update_item, name="update_item"),
    path('delete-item/<int:id>/', views.delete_item, name="delete_item"),
]