
from django.utils import timezone
timezone.now()

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    company_name = models.CharField(max_length=100, verbose_name='Название компании', blank=True, null=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя', blank=True, null=True)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', blank=True, null=True)
    email = models.EmailField(verbose_name='Электронная почта', blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Телефон', blank=True, null=True)
    telegram = models.CharField(max_length=100, verbose_name='Telegram', blank=True, null=True)
    company_link = models.URLField(verbose_name='Ссылка на компанию', blank=True, null=True)
    recvisity = models.TextField(verbose_name='Реквизиты', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.company_name} ({self.user.email})'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
class BalanceTopUp(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает оплаты'),
        ('completed', 'Оплачено'),
        ('failed', 'Ошибка оплаты'),
    ]

    CURRENCY_CHOICES = [
        ('USD', 'Доллары США'),
        ('EUR', 'Евро'),
        ('RUB', 'Рубли'),
    ]

    client_id = models.CharField(max_length=100, verbose_name='Клиент ID')
    user = models.CharField(max_length=100, verbose_name='User')  # Заменили на CharField
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Количество пополненных денег')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, verbose_name='Валюта')
    payment_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending',
                                      verbose_name='Статус оплаты')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    completed_at = models.DateTimeField(blank=True, null=True, verbose_name='Completed At')

    def __str__(self):
        return f'Пополнение баланса {self.id} - {self.client_id}'

    class Meta:
        verbose_name = 'Работа с пополнением баланса'
        verbose_name_plural = 'Работы с пополнением баланса'


class Lead(models.Model):
    REGION_CHOICES = [
        ('international', 'Международный'),
        ('russia', 'РФ'),
    ]

    STATUS_CHOICES = [
        ('pending', 'На рассмотрении'),
        ('accepted', 'Принят'),
        ('rejected', 'Отклонен'),
    ]

    niche = models.CharField(max_length=100, verbose_name='Ниша')
    client_budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сколько готов заплатить клиент?')
    contract_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость контракта')
    region = models.CharField(max_length=20, choices=REGION_CHOICES, verbose_name='Регион')
    seller = models.CharField(max_length=100, verbose_name='Продавец')  # Заменили на CharField
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='Статус лида')
    project_link = models.URLField(verbose_name='Ссылка на проект или на ваши соц сети')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_notified = models.BooleanField(default=False, verbose_name='Is Notified')
    is_auction = models.BooleanField(default=False, verbose_name='Аукцион ли это?')
    show_company = models.BooleanField(default=False, verbose_name='Показывать компанию?')
    advertising_budgets = models.TextField(verbose_name='Рекламные бюджеты', blank=True, null=True)

    def __str__(self):
        return f'Лид {self.id} - {self.niche}'

    class Meta:
        verbose_name = 'Лид'
        verbose_name_plural = 'Лиды'


class PurchasedLead(models.Model):
    lead = models.CharField(max_length=100, verbose_name='Lead')
    buyer = models.CharField(max_length=100, verbose_name='Buyer')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Purchase Price')
    seller_received = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Seller Received')
    complaint = models.TextField(verbose_name='Complaint', blank=True, null=True)
    complaint_submitted = models.BooleanField(default=False, verbose_name='Complaint Submitted')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return f'Купленный лид {self.lead}'

    class Meta:
        verbose_name = 'Купленный лид'
        verbose_name_plural = 'Купленные лиды'


class Contract(models.Model):
    SERVICE_CHOICES = [
        ('marketing_strategy', 'Marketing Strategy'),
        ('full_scope_marketing', 'Full-scope Marketing'),
        ('consultancy', 'Consultancy'),
        ('traffic_media_buying', 'Traffic/media buying'),
        ('shilling', 'Shilling'),
        ('kol_influencers', 'KOL\'s/influencers'),
        ('pr', 'PR'),
        ('development', 'Development'),
        ('market_making', 'Market Making'),
        ('design', 'Design'),
        ('copywriting', 'Copywriting'),
        ('smm', 'SMM'),
        ('listing', 'Listing'),
        ('nft_creation', 'NFT creation'),
        ('hr', 'HR'),
        ('security_audit', 'Security Audit'),
        ('legal', 'Legal'),
        ('other', 'Other'),
    ]

    REGION_CHOICES = [
        ('International', 'Международный'),
        ('Russia', 'РФ'),
    ]

    niche = models.CharField(max_length=100, verbose_name='Ниша')
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, verbose_name='Услуга')
    contract_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Процент от контракта')
    seller = models.CharField(max_length=100, verbose_name='Продавец')
    status = models.CharField(max_length=50, verbose_name='Статус контракта')
    selected_buyer = models.CharField(max_length=100, verbose_name='Выбранный покупатель')
    project_link = models.URLField(verbose_name='Ссылка на проект или на соцсети')
    region = models.CharField(max_length=20, choices=REGION_CHOICES, verbose_name='Регион')
    details = models.TextField(verbose_name='Детали')
    creator_id = models.CharField(max_length=100, verbose_name='ID создателя контракта', blank=True, null=True)  # Новое поле

    def __str__(self):
        return self.niche

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'


class LeadComplaint(models.Model):
    lead_purchase = models.CharField(max_length=100, verbose_name='Lead Purchase')
    complaint_reason = models.TextField(verbose_name='Причина жалобы')
    is_resolved = models.BooleanField(default=False, verbose_name='Решена ли жалоба')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return f'Жалоба на {self.lead_purchase}'

    class Meta:
        verbose_name = 'Жалоба на лиды'
        verbose_name_plural = 'Жалобы на лиды'


class AuctionLead(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено'),
    ]

    lead = models.CharField(max_length=100, verbose_name='Lead')
    buyer = models.CharField(max_length=100, verbose_name='Buyer')
    offered_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Offered Price')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return self.lead

    class Meta:
        verbose_name = 'Аукцион лидов'
        verbose_name_plural = 'Аукцион лидов'


class AuctionContract(models.Model):
    STATUS_CHOICES = [
        ('pending', 'На рассмотрении'),
        ('accepted', 'Принята'),
        ('rejected', 'Отклонена'),
    ]

    contract = models.CharField(max_length=100, verbose_name='Контракт')
    buyer = models.CharField(max_length=100, verbose_name='Покупатель')
    message_to_seller = models.TextField(verbose_name='Сообщение для продавца')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='Статус заявки')

    def __str__(self):
        return self.contract

    class Meta:
        verbose_name = 'Аукцион контрактов'
        verbose_name_plural = 'Аукцион контрактов'


class Partner(models.Model):
    user = models.CharField(max_length=100, verbose_name='Пользователь')
    company_name = models.CharField(max_length=100, verbose_name='Название компании', default="")
    telegram_account = models.CharField(max_length=100, verbose_name='Телеграм аккаунт')
    withdrawal_details = models.TextField(verbose_name='Куда выводить деньги')
    website_link = models.URLField(verbose_name='Ссылка на сайт')
    email = models.EmailField(verbose_name='Электронная почта')
    status = models.CharField(max_length=10,
                              choices=[('pending', 'Ожидает подтверждения'), ('confirmed', 'Подтверждено'),
                                       ('rejected', 'Отклонено')], default='pending', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Работа с партнерами'
        verbose_name_plural = 'Работа с партнерами'


class CompanyBalance(models.Model):
    user = models.CharField(max_length=100, verbose_name='Название компании')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Баланс')

    def __str__(self):
        return f'{self.user} - {self.amount}'

    class Meta:
        verbose_name = 'Работа с балансом'
        verbose_name_plural = 'Работа с балансом'


class WithdrawalRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает обработки'),
        ('approved', 'Одобрено'),
        ('rejected', 'Не одобрено'),
    ]

    user = models.CharField(max_length=100, verbose_name='Пользователь')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    date_request = models.DateTimeField(auto_now_add=True, verbose_name='Дата запроса')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='Статус')

    def __str__(self):
        return f'{self.user} - {self.amount}'

    class Meta:
        verbose_name = 'Запрос на вывод денег'
        verbose_name_plural = 'Запросы на вывод денег'
