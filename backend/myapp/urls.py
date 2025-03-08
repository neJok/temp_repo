from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartnerViewSet, WithdrawalRequestViewSet, CompanyBalanceViewSet, LeadViewSet
from . import views
from .views import RegisterView, LoginView

router = DefaultRouter()
router.register(r'partners', PartnerViewSet)
router.register(r'withdrawal-requests', WithdrawalRequestViewSet)
router.register(r'company-balances', CompanyBalanceViewSet)
router.register(r'leads', LeadViewSet)  # Добавьте эту строку

urlpatterns = [
    path('', include(router.urls)),
    path('withdrawal-requests/', views.WithdrawalRequestListView.as_view(), name='withdrawal-request-list'),
    path('withdrawal-requests/<int:pk>/', views.WithdrawalRequestUpdateView.as_view(), name='withdrawal-request-update'),
    path('api/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]