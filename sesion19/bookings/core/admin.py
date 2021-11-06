from django.contrib import admin

from core.models import Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Booking, BookingAdmin)