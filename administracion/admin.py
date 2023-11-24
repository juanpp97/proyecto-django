from django.contrib import admin
from .models import RoomImg, RoomType, RoomView, Price
# Register your models here.

admin.site.register(RoomImg)
# admin.site.register(RoomType)
admin.site.register(RoomView)
admin.site.register(Price)


class Imagen_linkeada(admin.TabularInline):
    model = RoomImg
    extra = 1

@admin.register(RoomType)
class RomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_view','capacity' , 'num_beds')
    inlines = [Imagen_linkeada]
    fieldsets = (
        (None, {
            'fields': ('name', 'capacity', 'num_beds')
        }), 
        (None, {
            'fields': ('view',),
        }),
        )
    
    filter_horizontal = ('view',)