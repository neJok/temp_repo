from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from .models import WithdrawalRequest, CompanyBalance
from .serializers import WithdrawalRequestSerializer, CompanyBalanceSerializer
from rest_framework import viewsets
from .models import Partner
from .serializers import PartnerSerializer
from .serializers import RegisterSerializer
from rest_framework import generics
from .serializers import LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResponseSerializer
from .models import Lead
from .serializers import LeadSerializer
from rest_framework import viewsets

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
class ContractResponseView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['user_name']
            user_id = serializer.validated_data['user_id']
            message = serializer.validated_data['message']

            # Здесь можно добавить логику обработки отклика, например, сохранение в базу данных
            # или отправку уведомления создателю контракта.

            return Response({"status": "success", "message": "Отклик успешно отправлен"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        # Создаем или получаем токен для пользователя
        token, created = Token.objects.get_or_create(user=user)

        # Возвращаем токен и данные пользователя
        return Response({
            "token": token.key,
            "user": {
                "id": user.id,
                "email": user.email,
                "username": user.username,
            }
        }, status=status.HTTP_200_OK)
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()
        return Response({"profile_id": profile.id, "user_id": profile.user.id}, status=status.HTTP_201_CREATED)

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class CompanyBalanceViewSet(viewsets.ModelViewSet):
    queryset = CompanyBalance.objects.all()
    serializer_class = CompanyBalanceSerializer


class WithdrawalRequestViewSet(viewsets.ModelViewSet):
    queryset = WithdrawalRequest.objects.all()
    serializer_class = WithdrawalRequestSerializer


class WithdrawalRequestListView(ListView):
    model = WithdrawalRequest
    template_name = 'admin/withdrawal_request_list.html'
    context_object_name = 'withdrawal_requests'


class WithdrawalRequestUpdateView(UpdateView):
    model = WithdrawalRequest
    template_name = 'admin/withdrawal_request_update.html'
    fields = ['user', 'amount', 'date_request', 'status']
    success_url = reverse_lazy('withdrawal-request-list')


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
