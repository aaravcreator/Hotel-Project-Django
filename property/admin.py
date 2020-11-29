from django.contrib import admin

from .models import Property , Category , Reserve


class PropertyAdmin(admin.ModelAdmin):
    list_display = ["name","location","category","property_type","price"]
    list_filter = ["property_type","category"]
    search_fields = ["name","location"]
# Register your models here.

admin.site.register(Property,PropertyAdmin)
admin.site.register(Category)
admin.site.register(Reserve)

