from django.contrib import admin
from . import models
from .models import Food, Consume, AboutUs


admin.site.register(Food)
admin.site.register(Consume)
admin.site.register(AboutUs)

