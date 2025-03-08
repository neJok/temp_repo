from .models import WithdrawalRequest, CompanyBalance
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import Partner
from .models import AuctionContract
from .models import AuctionLead
from .models import LeadComplaint
from .models import Contract
from django.contrib import admin
from .models import PurchasedLead
from .models import BalanceTopUp
from django.contrib import admin
from .models import Lead

class ContractAdmin(admin.ModelAdmin):
    list_display = ('niche', 'service', 'seller', 'status', 'selected_buyer', 'creator_id')  # Добавлено новое поле
    list_editable = ('status',)
    search_fields = ('niche', 'seller', 'selected_buyer')
    fields = ('niche', 'service', 'contract_percentage', 'seller', 'status', 'selected_buyer', 'project_link', 'region',
              'details', 'creator_id')  # Добавлено новое поле
class BalanceTopUpAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'user', 'amount', 'currency', 'payment_status', 'payment_date', 'completed_at')
    list_editable = ('payment_status',)
    search_fields = ('client_id', 'user')
    list_filter = ('payment_status', 'currency')
    fields = ('client_id', 'user', 'amount', 'currency', 'payment_status', 'completed_at')


admin.site.register(BalanceTopUp, BalanceTopUpAdmin)


class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'niche', 'client_budget', 'contract_cost', 'region', 'seller', 'status', 'created_at', 'is_notified',
        'is_auction', 'show_company')
    list_editable = ('status', 'is_notified', 'is_auction', 'show_company')
    search_fields = ('niche', 'seller', 'project_link')  # Обновили поиск по seller
    list_filter = ('status', 'region', 'is_auction', 'show_company')
    fields = (
        'niche', 'client_budget', 'contract_cost', 'region', 'seller', 'status', 'project_link',
        'is_notified', 'is_auction', 'show_company', 'advertising_budgets'
    )


admin.site.register(Lead, LeadAdmin)


class PurchasedLeadAdmin(admin.ModelAdmin):
    list_display = ('lead', 'buyer', 'purchase_price', 'seller_received', 'complaint_submitted', 'created_at')
    list_editable = ('complaint_submitted',)
    search_fields = ('lead', 'buyer')
    fields = ('lead', 'buyer', 'purchase_price', 'seller_received', 'complaint', 'complaint_submitted')


admin.site.register(PurchasedLead, PurchasedLeadAdmin)


class ContractAdmin(admin.ModelAdmin):
    list_display = ('niche', 'service', 'seller', 'status', 'selected_buyer')
    list_editable = ('status',)
    search_fields = ('niche', 'seller', 'selected_buyer')
    fields = ('niche', 'service', 'contract_percentage', 'seller', 'status', 'selected_buyer', 'project_link', 'region',
              'details')


admin.site.register(Contract, ContractAdmin)


class LeadComplaintAdmin(admin.ModelAdmin):
    list_display = ('lead_purchase', 'complaint_reason', 'is_resolved', 'created_at')
    list_editable = ('is_resolved',)
    search_fields = ('lead_purchase',)
    fields = ('lead_purchase', 'complaint_reason', 'is_resolved')


admin.site.register(LeadComplaint, LeadComplaintAdmin)


class AuctionLeadAdmin(admin.ModelAdmin):
    list_display = ('lead', 'buyer', 'offered_price', 'status', 'created_at')
    list_editable = ('status',)
    search_fields = ('lead', 'buyer')
    fields = ('lead', 'buyer', 'offered_price', 'status')


admin.site.register(AuctionLead, AuctionLeadAdmin)


class AuctionContractAdmin(admin.ModelAdmin):
    list_display = ('contract', 'buyer', 'status')  # Поля, отображаемые в списке
    list_editable = ('status',)  # Поля, которые можно редактировать прямо в списке
    search_fields = ('contract', 'buyer')  # Поля для поиска
    fields = ('contract', 'buyer', 'message_to_seller', 'status')  # Поля, отображаемые в форме редактирования


admin.site.register(AuctionContract, AuctionContractAdmin)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'status', 'created_at')  # Поля, отображаемые в списке
    list_filter = ('status',)  # Фильтр по статусу
    search_fields = ('company_name', 'user', 'email')  # Поля для поиска
    list_editable = ('status',)  # Поля, которые можно редактировать прямо в списке
    fieldsets = (
        (None, {'fields': (
            'user', 'company_name', 'telegram_account', 'withdrawal_details', 'website_link', 'email', 'status')}),
    )


admin.site.register(Partner, PartnerAdmin)


class CompanyBalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')  # Поля, отображаемые в списке
    list_editable = ('amount',)  # Поля, которые можно редактировать прямо в списке
    search_fields = ('user',)  # Поля, по которым можно искать
    list_per_page = 20  # Количество записей на странице


admin.site.register(CompanyBalance, CompanyBalanceAdmin)


class WithdrawalRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date_request', 'status')
    list_filter = ('status',)
    search_fields = ('user',)
    list_editable = ('status',)
    list_per_page = 20


admin.site.register(WithdrawalRequest, WithdrawalRequestAdmin)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'is_staff', 'is_active'),
        }),
    )


# Регистрация моделей
admin.site.unregister(User)  # Отменяем стандартную регистрацию
admin.site.register(User, CustomUserAdmin)  # Регистрируем с кастомной настройкой


class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Регистрация модели Group
admin.site.unregister(Group)  # Отменяем стандартную регистрацию
admin.site.register(Group, CustomGroupAdmin)  # Регистрируем с кастомной настройкой
