from django.contrib import admin
from .models import UserProfile
from .models import Abonement
from .models import Visit

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'phone_number', 'is_active', 'has_subscription', 'is_staff', 'subscription_end_date')
    list_filter = ('is_active', 'has_subscription', 'is_staff')  # Фильтры по полям
    search_fields = ('name', 'phone_number', 'personal_code')  # Поля для поиска
    ordering = ('subscription_end_date',)  # Сортировка по дате окончания подписки

@admin.register(Abonement)
class AbonementAdmin(admin.ModelAdmin):
    list_display = ('abonement_id', 'name', 'description', 'duration_type', 'duration_unit', 'total_sessions', 'price', 'is_online', 'discount', 'is_active')
    list_filter = ('is_online', 'is_active')
    search_fields = ('name', 'description')

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('visit_id', 'user_id', 'service_id', 'visit_date', 'status')  # Поля, отображаемые в списке
    list_filter = ('status', 'visit_date')  # Фильтры в админке
    search_fields = ('user_id', 'service_id')  # Поля для поиска
    ordering = ('-visit_date',)  # Сортировка по умолчанию