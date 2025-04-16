from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, ScheduledReward, RewardLog


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('coins',)}),
    )
    list_display = ('email', 'coins', "created_at")
    search_fields = ('email',)
    ordering = ('created_at',)


@admin.register(ScheduledReward)
class ScheduledRewardAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'execute_at')
    list_filter = ('execute_at',)
    search_fields = ('user__email', 'amount')


@admin.register(RewardLog)
class RewardLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'given_at')
    list_filter = ('given_at',)
    ordering = ('given_at',)
