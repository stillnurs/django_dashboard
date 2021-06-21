from django.contrib.admin import ModelAdmin, register
from .models import Person


# @register(Person)
# class PersonAdmin(ModelAdmin):
#     list_display = ('username', 'first_name', 'last_name', 'email')
#     icon_name = 'person'