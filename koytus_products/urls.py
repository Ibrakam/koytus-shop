from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page),
    path("product/<int:id>/", views.exact_product),
    path("category/<int:id>/", views.category_product)
]