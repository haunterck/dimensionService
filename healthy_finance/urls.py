from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from healthy_finance.views import LuIepsView
from healthy_finance.views import LuCasfimView

urlpatterns = [
    path('ieps/', LuIepsView.as_view()),
    path('ieps/<str:pk>/', LuIepsView.as_view()),
    path('casfim/', LuCasfimView.as_view()),
    path('casfim/<str:pk>/', LuCasfimView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
