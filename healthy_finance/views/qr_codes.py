import decimal
import base64
import qrcode
import os
import unicodedata

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import OperationalError


class QRCodeView(APIView):
    QR_PATH = os.getcwd() + "/qrImage.png"
    BBVA_KEY = "012"
    MX_COUNTRY = "MX"
    MX_CURRENCY = "MXN"
    OT = "0001"

    def delete_accent_mark(self, string_value):
        s = ''.join((c for c in unicodedata.normalize('NFD', str(string_value)) if unicodedata.category(c) != 'Mn'))
        return s

    def get(self, request, format=None, pk=None):
        print(self.QR_PATH)
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )


            payment_motive = "Pruebña verificación código ñoño QR"
            clabe = "012987654321234567"
            payment_type = "CL"
            qr_reference = "ABCdef1"
            beneficiary_name = "Pedro López Patiño"
            amount = "2346768.687867997897"[:10]
            amount = str(round(decimal.Decimal(amount), 2))
            bank = "00" + "012"


            data = {
                "ot": self.OT,
                "dOp": [
                    {"alias": self.delete_accent_mark(payment_motive)},
                    {"cl": clabe},
                    {"type": payment_type},
                    {"refn": qr_reference},
                    {"refa": self.delete_accent_mark(beneficiary_name)},
                    {"amount": amount},
                    {"bank": bank},
                    {"country": self.MX_COUNTRY.upper()},
                    {"currency": self.MX_CURRENCY.upper()}
                ]
            }

            print("DATA: ", data)

            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image()
            img.save(self.QR_PATH)

            with open(self.QR_PATH, 'rb') as imgFile:
                image = base64.b64encode(imgFile.read())

            return Response({
                "qrBase64": image
            }, status=status.HTTP_200_OK)

        except Exception as ex:
            return Response({
                "message": str(ex)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
