from django.contrib import admin

from MarketApp.models import *

# Register your models here.

class ProductsInMarketInline(admin.TabularInline):
    model=ProductInMarket
    extra=0

class MarketAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [ProductsInMarketInline]
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name","surname"]
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            return super(EmployeeAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True

class ProductAdmin(admin.ModelAdmin):
    list_filter = ["type", "homemade"]


admin.site.register(Product,ProductAdmin)
admin.site.register(Market,MarketAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(ContactInfo)
