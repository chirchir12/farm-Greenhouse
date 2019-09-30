
from django.contrib import admin

# Register your models here.
from .models import Product, Category, Contact

# this is when you need to add slug field in the admin section


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ["__str__", "slug", 'category']
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

    class Meta:
            model = Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    ordering = ('timestamp',)

    class Meta:
        model = Category
        


class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone']

    class Meta:
        model = Contact


# this registers your product model in the admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)
