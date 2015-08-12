from django.contrib import admin
from main.models import Manufacturer, Nutritional_facts, Cereal

# Register your models here.


admin.site.register(Cereal)
admin.site.register(Manufacturer)
admin.site.register(Nutritional_facts)