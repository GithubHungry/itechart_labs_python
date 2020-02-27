from django.contrib import admin
from .models import PhoneCatalog


# Register your models here.
class PhoneAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'reg_date', 'address')
	list_display_links = ('name', 'phone')
	search_fields = ('name', 'phone')


admin.site.register(PhoneCatalog, PhoneAdmin)
