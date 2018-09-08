from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from healthy_finance.models import LuIeps
from healthy_finance.serializers import LuIepsSerializer

from django.db.utils import OperationalError


class LuIepsView(APIView):

    def get(self, request, pk=None):

        try:
            if pk is not None:
                record = LuIeps.objects.get(hashkey=pk)
                serializer = LuIepsSerializer(record)
                return Response(serializer.data)
            else:
                records = LuIeps.objects.all()
                serializer = LuIepsSerializer(records, many=True)
                return Response(serializer.data)
        except LuIeps.DoesNotExist:
            return Response({
                "message": "El registro no existe"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({
                "message": str(ex)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
