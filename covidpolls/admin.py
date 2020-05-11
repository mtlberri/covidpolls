from django.contrib import admin

# Register your models here.
from .models import Parent1, Child

admin.site.register(Parent1)
admin.site.register(Child)

