from django.shortcuts import render  # noqa
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from .models import Telefon, Mashina
from .serializers import TelefonSeralizer, MashinaSeralizer


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


class MashinaApiView(APIView):

    def get(self, request):
        mashinalar = Mashina.objects.all()
        mashina_ser = MashinaSeralizer(mashinalar, many=True).data
        return Response(mashina_ser, status=status.HTTP_200_OK)

    def post(self, request):
        ser = MashinaSeralizer(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response(ser.data, status=status.HTTP_200_OK)


class MashinaDetailApiView(APIView):
    def get(self, request, pk=None):
        try:
            mashina = Mashina.objects.get(id=pk)
            mashina_ser = MashinaSeralizer(mashina).data
            return Response(mashina_ser, status=status.HTTP_200_OK)
        except:  # noqa
            return Response(
                {"error": "Mashina does not exist"},
                status=status.HTTP_400_BAD_REQUEST,  # noqa
            )

    def put(self, request, pk=None):
        try:
            mashina = Mashina.objects.get(id=pk)
            mashina_ser = MashinaSeralizer(data=request.data, instance=mashina)
            if mashina_ser.is_valid():
                mashina_ser.save()
            else:
                return Response(
                    mashina_ser.errors,
                    status=status.HTTP_400_BAD_REQUEST,  # noqa
                )
            return Response(mashina_ser.data, status=status.HTTP_200_OK)
        except:  # noqa
            return Response(
                {"error": "Mashina does not exist"},
                status=status.HTTP_400_BAD_REQUEST,  # noqa
            )

    def patch(self, request, pk=None):
        try:
            mashina = Mashina.objects.get(id=pk)
            mashina_ser = MashinaSeralizer(data=request.data, instance=mashina, partial=True)
            if mashina_ser.is_valid():
                mashina_ser.save()
            else:
                return Response(
                    mashina_ser.errors,
                    status=status.HTTP_400_BAD_REQUEST,  # noqa
                )
            return Response(mashina_ser.data, status=status.HTTP_200_OK)
        except:  # noqa
            return Response(
                {"error": "Mashina does not exist"},
                status=status.HTTP_400_BAD_REQUEST,  # noqa
            )
        
    def delete(self, request, pk=None):
        try:
            mashina = Mashina.objects.get(id=pk)
            mashina.delete()
            return Response(
                    {"message": f"{mashina.name} deleted succesfully"},
                    status=status.HTTP_200_OK  # noqa
                )
        except:  # noqa
            return Response(
                {"error": "Mashina does not exist"},
                status=status.HTTP_400_BAD_REQUEST,  # noqa
            )