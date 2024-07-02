from django.contrib import admin
from .models import CarsModel
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src= "{}" width="40" style="border-radius: 50px;"/>'.format(object.car_photo.url))
    
    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'car_title', 'color', 'model', 'condition', 'fuel_type', 'is_featured',)
    list_display_links = ('id', 'thumbnail', 'car_title',)
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'model', 'fuel_type')
    list_filter = ('car_title', 'city', 'model', 'fuel_type',)


admin.site.register(CarsModel, CarAdmin)
