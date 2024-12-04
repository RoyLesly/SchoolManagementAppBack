import os
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from pymesomb.operations import PaymentOperation
from pymesomb.utils import RandomGenerator
from datetime import datetime
from back.utils import *
from back.middleware import *
import os
from django.http import FileResponse


def download_apk(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'eStudent.apk')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='eStudent.apk')


# MeSomb configuration (replace with your actual keys)
application_key = os.getenv("MESOMB_APPLICATION_KEY")
access_key = os.getenv("MESOMB_ACCESS_KEY")
secret_key = os.getenv("MESOMB_SECRET_KEY")


class MeSombPaymentViewSet(viewsets.ViewSet):
    # permission_classes = [IsAuthenticatedWithAPIKey]

    @action(detail=False, methods=["get"], url_path="check-status")
    def check_status(self, request):
        try:
            operation = PaymentOperation(application_key, access_key, secret_key)
            response = operation.get_status()
            return Response({"status": response}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=["post"], url_path="collect-money")
    def collect_money(self, request):
        # Extract request data
        print(request.data)
        amount = request.data.get("amount")
        service = request.data.get("service")
        payer = request.data.get("payer")
        message = request.data.get("message", "No message provided")

        if not all([amount, service, payer]):
            return Response(
                {"error": "amount, service, and payer are required fields"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            payment = PaymentOperation(application_key, access_key, secret_key)

            print(RandomGenerator.nonce())
            response = payment.make_collect({
                'amount': amount,
                'service': service,
                'payer': payer,
                'message': message,
                'date': datetime.now(),
                'nonce': RandomGenerator.nonce(),
            })

            # Return success response
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            # Handle errors
            print(e, 57)
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
