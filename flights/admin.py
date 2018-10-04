from django.contrib import admin
from .models import Airport, Flight, Passenger
# Register your models here.

# StackedInline - built-in class that add new relationships between objects
class PassengerInline(admin.StackedInline):
    #through tells us that there is an intermediary table between passengers and flights
    model = Passenger.flights.through
    extra = 1

class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flights',)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)