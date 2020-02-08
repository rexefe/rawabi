from django.contrib import admin
from .models import *
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
	list_display = ('name','country','gender', 'age', 'level_edu', 'prof', 'is_reserved')


admin.site.register(Country)
admin.site.register(Profile, ProfileAdmin)

