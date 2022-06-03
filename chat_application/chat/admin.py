from django.contrib import admin
from .models import Permission, Space,Message, SpaceX,room

admin.site.register(Space)
admin.site.register(Message)
admin.site.register(room)
admin.site.register(Permission)
admin.site.register(SpaceX)
# Register your models here.
