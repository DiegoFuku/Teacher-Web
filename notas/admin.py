from django.contrib import admin
from .models import Students


class StudentsAdmin(admin.ModelAdmin):
    list_display=("name","curse")


admin.site.register(Students,StudentsAdmin)


