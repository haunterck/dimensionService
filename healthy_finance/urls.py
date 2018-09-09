from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from healthy_finance.views import LuIepsView
from healthy_finance.views import LuCasfimView
from healthy_finance.views import QRCodeView
from healthy_finance.views import ClienteView
from healthy_finance.views import AttPlanView
from healthy_finance.views import BancomerpayView
from healthy_finance.views import report_income
from healthy_finance.views import report_industries
from healthy_finance.views import report_client_movements
from healthy_finance.views import get_client_rfc

urlpatterns = [
    # LU endpoints
    path('ieps/', LuIepsView.as_view()),
    path('ieps/<str:pk>/', LuIepsView.as_view()),
    path('casfim/', LuCasfimView.as_view()),
    path('casfim/<str:pk>/', LuCasfimView.as_view()),
    path('attplan/', AttPlanView.as_view()),
    path('attplan/<str:pk>/', AttPlanView.as_view()),
    path('cliente/', ClienteView.as_view()),
    path('cliente/<str:pk>/', ClienteView.as_view()),
    path('bancomerpay/', BancomerpayView.as_view()),
    path('bancomerpay/<str:pk>/', BancomerpayView.as_view()),
    # QR code endpoint
    path('qr/<str:pk>/', QRCodeView.as_view()),

    # Dashboards
    path('better-incomes/', report_income),
    path('better-industries/', report_industries),
    path('client-movements/<str:rfc>/', report_client_movements),
    path('client/rfcs/', get_client_rfc),
]

urlpatterns = format_suffix_patterns(urlpatterns)
