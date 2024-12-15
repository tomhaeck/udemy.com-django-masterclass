from django.contrib import admin
from shop.models import Product, Order

# Register your models here.
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"

class ProductAdmin(admin.ModelAdmin):
    # define a custom action
    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    list_display = ('title', 'price', 'discount_price', 'category')
    search_fields = ('title', 'category',)
    list_editable = ('price', )

    change_category_to_default.short_description = "Default Category"
    actions = ('change_category_to_default',)
    fields = ('title', 'price',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)



