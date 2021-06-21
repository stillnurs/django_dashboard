from helayel_app.models import *
from django.contrib.admin import ModelAdmin, register
from .models import *


@register(User)
class UserAdmin(ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone')
    icon_name = 'featured_play_list'


@register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone', 'designition')
    icon_name = 'featured_play_list'