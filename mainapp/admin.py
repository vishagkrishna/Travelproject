from django.contrib import admin
from . models import items
from . models import values
# Register your models here.
admin.site.register(items),
admin.site.register(values)