from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Status
from .models import Drink

# Register your models here.

class DrinkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['drink_name']}),
        (None, {'fields': ['drink_desc']}),
        (None, {'fields': ['strength']}),
        (None, {'fields': ['price']}),
    ]
    list_display = ('drink_name', 'drink_desc', 'strength', 'price')


admin.site.register(Drink, DrinkAdmin)


# Define an inline admin descriptor for status model
# which acts a bit like a singleton
class StatusInline(admin.StackedInline):
    model = Status
    can_delete = False
    verbose_name_plural = 'Status'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StatusInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
