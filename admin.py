from django.contrib import admin
from .models import Customer, StoreAdmin, Product, Category,CategoryType,Bill, BillItems,Cart
admin.site.register(Customer)
admin.site.register(StoreAdmin)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CategoryType)
admin.site.register(Bill)
admin.site.register(BillItems)
admin.site.register(Cart)


