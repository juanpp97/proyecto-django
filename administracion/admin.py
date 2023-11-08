from django.contrib import admin
from .models import RoomImg, RoomType, RoomView, Price
# Register your models here.

admin.site.register(RoomImg)
admin.site.register(RoomType)
admin.site.register(RoomView)
admin.site.register(Price)