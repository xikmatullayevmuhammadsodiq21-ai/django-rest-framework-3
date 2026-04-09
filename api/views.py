from django.shortcuts import render # noqa
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from .models import Telefon
from .serializers import TelefonSeralizer


class MyAPi(APIView):
    def get(self, request):

        telefon = Telefon.objects.all()
        data = TelefonSeralizer(telefon, many=True).data

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = TelefonSeralizer(data=request.data)
        if ser.is_valid(raise_excaption=True):
            ser.save()
            name = ser.name
        msg = f"{name} telefon qoshildi."
        return Response({"massage": msg})

    def put(self, request):
        try:
            new_name = request.data.get("new_name")
            id = request.data.get("id")
            telefon = Telefon.objects.get(id=id)
            if new_name:
                telefon.name = new_name
                telefon.save()
            return Response("Saqlandi chotkiy")
        except Telefon.DoesNotExist:
            return Response("kechirasiz telefon topilmadi.")
        except Exception as e:
            return Response("Nomalum xatolik: " + e)
