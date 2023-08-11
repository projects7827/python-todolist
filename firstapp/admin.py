from django.contrib import admin
from .models import all_tasks,category

# Register your models here.
admin.site.register(all_tasks)
admin.site.register(category)
