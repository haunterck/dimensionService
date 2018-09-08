from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from healthy_finance.models import LuCasfim
from healthy_finance.serializers import LuCasfimSerializer

from django.db.utils import OperationalError


class LuCasfimView(APIView):

    def get(self, request, pk=None):
        print(pk)
        try:
            if pk is not None:
                record = LuCasfim.objects.get(hashkey=pk)
                serializer = LuCasfimSerializer(record)
                return Response(serializer.data)
            else:
                records = LuCasfim.objects.all()
                serializer = LuCasfimSerializer(records, many=True)
                return Response(serializer.data)
        except LuCasfim.DoesNotExist:
            return Response({
                "message": "El registro no existe"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({
                "message": str(ex)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)