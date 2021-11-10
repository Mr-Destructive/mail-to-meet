from rest_framework import serializers
from .models import Mail

class MailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=32)
    email = serializers.EmailField(max_length=64)
    subject = serializers.CharField(max_length=256)
    body = serializers.CharField(max_length=384000)
    reciever = serializers.EmailField(max_length=64)

    class Meta:
        model = Mail
        fields = ('__all__')
