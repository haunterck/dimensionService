from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from healthy_finance.models import Bancomerpay
from healthy_finance.serializers import BancomerpaySerializer

from django.db.utils import OperationalError

class BancomerpayView(APIView):

    def get(self, request, pk=None):
    
        try:
            if pk is not None:
                record = Bancomerpay.objects.get(hashkey=pk)
                serializer = BancomerpaySerializer(record)
                return Response(serializer.data)
            else:
                records = Bancomerpay.objects.all()
                serializer = BancomerpaySerializer(records, many=True)
                return Response(serializer.data)
        except Bancomerpay.DoesNotExist:
            return Response({
                "message": "El registro no existe"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({
                "message": str(ex)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)