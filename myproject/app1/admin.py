from django.contrib import admin
from .models import Staff
from .models import product
from .models import Course,Language
# Register your models here.

admin.site.register(Staff)
admin.site.register(product)
admin.site.register(Course)
admin.site.register(Language)
