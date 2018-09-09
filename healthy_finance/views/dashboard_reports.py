import decimal
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.db import connection
from healthy_finance.models import Cliente
from healthy_finance.serializers import ClienteSerializer


@api_view(['GET'])
def report_income(request):
    cursor = connection.cursor()
    cursor.execute("""
        select count(*), sector , actividad, sum(monto) from BANCOMER.movimientos mv
            INNER JOIN BANCOMER.cliente po
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
            "emitter":row[4],
            "nu_client":row[5],
            "rfcName":row[7],
            "hashKeyCasfim":row[8],
            "celphoneNumber":row[9],
            "telephoneNumber":row[10],
            "telephoneCredencials":row[11],
            "celphoneCredencials":row[12],

            "hashkey":row[13],
            "sector":row[14],
            "businessActivity":row[15],
            "isActive":row[16],
        })
    return JsonResponse(response_list, safe=False, status=200)

@api_view(['GET'])
def get_client_rfc(request):
    # clients = Cliente.objects.all().distinct('rfc')
    clients = Cliente.objects.values('rfc').distinct()
    list_rfc = list()
    for client in clients:
        #print(client)
        list_rfc.append(client['rfc'])

    return JsonResponse(list_rfc, safe=False, status=200)
