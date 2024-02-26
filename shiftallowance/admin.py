from django.contrib import admin
from .models import Shift

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('team_member','team', 'shift_type','date','nightShiftComment')
    list_filter = ('date', 'shift_type','team')
    search_fields = ('team_member__username',)

admin.site.register(Shift, ShiftAdmin)