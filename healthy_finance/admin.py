from django.contrib import admin
from .models import AttPlan
from .models import Cliente
from .models import LuCasfim
from .models import LuIeps
from .models import Bancomerpay

# Register your models here.
admin.site.register(AttPlan)
admin.site.register(Cliente)
admin.site.register(LuIeps)
admin.site.register(LuCasfim)
admin.site.register(Bancomerpay)