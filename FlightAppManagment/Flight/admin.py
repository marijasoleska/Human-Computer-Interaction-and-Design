from django.contrib import admin

from flight2.models import Flight, Baloon, Airline, Pilot, AirlinePilot

# Register your models here.
class AirlineInPilotInLine(admin.TabularInline):
    model = AirlinePilot
    extra = 0

class AirlineAdmin(admin.ModelAdmin):
    inlines = [AirlineInPilotInLine]

    def has_add_permission(self, request):
        return False

class FlightAdmin(admin.ModelAdmin):
    exclude = ("user",)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(FlightAdmin, self).save_model(request, obj, form, change)
    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False
class PilotAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(Flight, FlightAdmin)
admin.site.register(Baloon)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Pilot,PilotAdmin)
