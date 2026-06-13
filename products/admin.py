from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "is_active", "updated_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "description")

