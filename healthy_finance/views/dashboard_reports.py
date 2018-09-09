import decimal
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.db import connection


@api_view(['GET'])
def report_income(request):
    cursor = connection.cursor()
    cursor.execute("""
        select count(*), sector , actividad, sum(monto) from BANCOMER.movimientos mv
            INNER JOIN BANCOMER.profile po
                on po.rfc = mv.rfc
            inner join BANCOMER.lu_casfim as cas
                on cas.hashkey = po.hashkey_casfim
            where tipo= 'deposito'
        group by  sector , actividad
        limit 10;
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

@api_view(['GET'])
def report_industries(request):
    cursor = connection.cursor()
    cursor.execute("""
            select count(*), sector , actividad, sum(monto) as totalAmount from BANCOMER.movimientos mv
                INNER JOIN BANCOMER.profile po
                    on po.rfc = mv.rfc
                inner join BANCOMER.lu_casfim as cas
                    on cas.hashkey = po.hashkey_casfim
                where tipo <>'deposito'
                    group by  sector , actividad
                ORDER BY totalAmount desc 
                limit 100;
        """)

    rows = cursor.fetchall()
    response_list = list()
    for row in rows:
        response_list.append({
            "sector": row[1],
            "activity": row[2],
            "totalAmount": str(round(decimal.Decimal(row[3]), 2)),
        })
    return JsonResponse(response_list, safe=False, status=200)

@api_view(['GET'])
def report_client_movements(request, rfc):
    cursor = connection.cursor()
    query = """
                select * from BANCOMER.movimientos mv
                    INNER JOIN BANCOMER.profile po
                        on po.rfc = mv.rfc
                    inner join BANCOMER.lu_casfim as cas
                        on cas.hashkey = po.hashkey_casfim
                    where mv.rfc = '{}'   
            """
    query = query.replace('{}', rfc)
    cursor.execute(query)

    rows = cursor.fetchall()
    response_list = list()
    for row in rows:
        print(row)
        response_list.append({
            "rfc":row[0],
            "amount":row[1],
            "period":row[2],
            "type":row[3],
            "client_number":row[4],
            "rfc":row[5],
            "rfcName":row[6],
            "hashKeyCasfim":row[7],
            "celphoneNumber":row[8],
            "telephoneNumber":row[9],
            "telephoneCredencials":row[10],
            "celphoneCredencials":row[11],

            "hashkey":row[12],
            "sector":row[13],
            "businessActivity":row[14],
            "isActive":row[15],
        })
    return JsonResponse(response_list, safe=False, status=200)

