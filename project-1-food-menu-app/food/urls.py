from django.urls import path
from food import views

app_name = "food"

urlpatterns = [
    # path("", views.index, name="index"),
    path('', views.IndexClassView.as_view(), name='index'),

    #path("<int:item_id>/", views.detail, name="detail"),
    path("<int:pk>/", views.FoodDetail.as_view(), name="detail"),

    # path("add/", views.create_item, name="create_item"),
    path("add/", views.CreateItem.as_view(), name="create_item"),

    path("update/<int:id>/", views.update_item, name="update_item"),
    path("detele/<int:id>/", views.delete_item, name="delete_item"),
]