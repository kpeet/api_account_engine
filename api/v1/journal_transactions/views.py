from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import JournalTransactionsSerializer,JournalOperationTransactionsSerializer
import json

class JournalTransaction(APIView):
    """
    List all batches or create a new batch with journals
    """
    def get(self, request, format=None):
        print("GET BATCH!!!")
        """
        List all batches
        """

        return request#Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a new Batch with this format
        {
            "transaction_type":1,
            "from_account":1,
            "to_account":2,
            "amount":9900,
            "asset_type":1
        }

        :return: a new journal
        """


        serializer= JournalTransactionsSerializer(data=request.data)
        if serializer.is_valid():
            print("Estructura valida para JournalTransaction")
            #TODO: validar transacciones por doble partida, No aplica

            #TODO: Validar que las cuentas no sean la misma

            #TODO: Validar transacciones por Materialización
            #if make_virtual_payment_materialization(serializer.data['from_account'], serializer.data['amount']):
            json_data=serializer.save()
            return Response(json_data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ErrorJournalTransactionResponse():

    def __init__(self, account_id, amount_error):
        self.account_id = account_id
        self.amount_error = amount_error


class JournalOperationTransaction(APIView):
    """
    List all batches or create a new batch with journals
    """
    def get(self, request, format=None):
        print("GET BATCH!!!")
        """
        List all batches
        """

        return request#Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a new Batch with this format
        {
            "transaction_type":1,
            "from_account":1,
            "to_account":2,
            "amount":9900,
            "asset_type":1
        }

        :return: a new journal
        """


        serializer= JournalOperationTransactionsSerializer(data=request.data)
        if serializer.is_valid():
            print("Estructura valida para JournalTransaction")
            #TODO: validar transacciones por doble partida, No aplica

            #TODO: Validar que las cuentas no sean la misma

            #TODO: Validar transacciones por Materialización
            #if make_virtual_payment_materialization(serializer.data['from_account'], serializer.data['amount']):
            json_data=serializer.save()
            return Response(json_data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



