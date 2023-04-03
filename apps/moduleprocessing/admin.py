from django.contrib import admin

# Register your models here.
from .models import Operator
from .models import ShipInfo

admin.site.register(Operator)
admin.site.register(ShipInfo)
