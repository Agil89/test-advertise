from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *

class UpdateStatus(APIView):
    permission_classes = [IsAuthenticated]
    """
    Updating statusses for choosen list of ads
    """
    def put(self, request):
        data = request.data
        id_list_advertises = data.get('list')[0].split(',')
        pay_amount = PayAmount.objects.last().sum
        ad_status = data.get('status')
        if not ad_status:
            return Response("No status was found in request,add status 'оплачено' or 'отказ'.", status=status.HTTP_404_NOT_FOUND)
        user = Autor.objects.filter(id=request.user.pk).first()
        if not user.is_admin:
            return Response("Only admins can update advertise status.", status=status.HTTP_406_NOT_ACCEPTABLE)
        for id in id_list_advertises:
            advertise = Advertise.objects.filter(id=id).first()
            if not advertise:
                return Response("No Advertise with this id or advertise was already checked!", status=status.HTTP_404_NOT_FOUND)
            author = advertise.autor
            if advertise and not advertise.is_checked:
                advertise.status = ad_status
                advertise.is_checked = True
                advertise.save()
                if ad_status == "оплачено":
                    author.balance = author.balance + pay_amount
                    author.save()
            else:
                return Response("You can not update checked ads!", status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response("All ads updated", status=status.HTTP_200_OK)