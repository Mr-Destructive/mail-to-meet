from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MailSerializer
from .models import Mail
from django.core.mail import send_mail

class MailView(APIView):
    def post(self, request):
        serializer = MailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data=request.data
            email = send_mail(data['subject'] , data['body'], data['reciever'], [data['reciever']])
            return Response({"status":"success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

