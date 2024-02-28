from django.contrib import admin
from .models import Shift,UserInfo
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User




class ShiftAdmin(admin.ModelAdmin):
    list_display = ('team_member', 'shift_type','date','nightShiftComment')
    list_filter = ('date', 'shift_type','team_member')
    search_fields = ('team_member__username',)
    ordering = ('-date',)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user','team','employeeID']
admin.site.register(Shift, ShiftAdmin)
admin.site.register(UserInfo,UserInfoAdmin)


###stacking User model and custom UserInfo model

class UserInfoInline(admin.StackedInline):
    model = UserInfo
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (UserInfoInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)