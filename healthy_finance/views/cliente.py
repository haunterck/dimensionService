from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from healthy_finance.models import Cliente
from healthy_finance.serializers import ClienteSerializer

from django.db.utils import OperationalError

class ClienteView(APIView):

    def get(self, request, pk=None):
    
        try:
            if pk is not None:
                record = Cliente.objects.get(nu_cliente=pk)
                serializer = ClienteSerializer(record)
                return Response(serializer.data)
            else:
                records = Cliente.objects.all()
                serializer = ClienteSerializer(records, many=True)
                return Response(serializer.data)
        except Cliente.DoesNotExist:
            return Response({
                "message": "El registro no existe"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({
                "message": str(ex)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)