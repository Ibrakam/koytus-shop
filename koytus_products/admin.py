from django.contrib import admin
from koytus_products.models import *

# Register your models here.
@admin.register(CategoryProduct)
class CategoryAdminModel(admin.ModelAdmin):
    search_fields = ["category_name", "id"]
    list_display = ["id", "category_name"]
    ordering = ["-id"]


@admin.register(Products)
class ProductAdminModel(admin.ModelAdmin):
    search_fields = ["pr_name", "id"]
    list_display = ["id", "pr_name", "pr_cost", "pr_category"]
    ordering = ["-id"]


@admin.register(UserCart)
class UserCartAdminModel(admin.ModelAdmin):
    search_fields = ["id", "user_id"]
    list_filter = ["creates_at"]
    list_display = ["id", "user_id", "product"]
    ordering = ["-id"]
