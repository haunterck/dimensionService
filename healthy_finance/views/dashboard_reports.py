import decimal
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.db import connection


@api_view(['GET'])
def reportIncome(request):
    cursor = connection.cursor()
    cursor.execute("""
        select count(*), sector , actividad, sum(monto) from BANCOMER.movimientos mv
            INNER JOIN BANCOMER.profile po
                on po.rfc = mv.rfc
            inner join BANCOMER.lu_casfim as cas
                on cas.hashkey = po.hashkey_casfim
            where tipo= 'deposito'
        group by  sector , actividad
        limit 100;
    """)

    rows = cursor.fetchall()
    response_list = list()
    for row in rows:
        response_list.append({
            "valor": row[0],
            "sector": row[1],
            "actividad": row[2],
            "monto": "$" + str(round(decimal.Decimal(row[3]), 2)),
        })
    return JsonResponse(response_list, safe=False, status=200)
