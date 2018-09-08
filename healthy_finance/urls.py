from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from healthy_finance.views import LuIepsView
from healthy_finance.views import LuCasfimView
from healthy_finance.views import QRCodeView
from healthy_finance.views import reportIncome

urlpatterns = [
    # LU endpoints
    path('ieps/', LuIepsView.as_view()),
    path('ieps/<str:pk>/', LuIepsView.as_view()),
    path('casfim/', LuCasfimView.as_view()),
    path('casfim/<str:pk>/', LuCasfimView.as_view()),
    # QR code endpoint
    path('qr/<str:pk>/', QRCodeView.as_view()),

    # Dashboards
    path('better-incomes/', reportIncome),
]

urlpatterns = format_suffix_patterns(urlpatterns)
