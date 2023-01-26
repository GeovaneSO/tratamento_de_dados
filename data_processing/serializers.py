from rest_framework import serializers
from .models import Process

class ProcessSerializer(serializers.Serializer):
    transaction_type = serializers.IntegerField()
    transaction_date = serializers.DateField(format="%Y-%m-%d")
    transaction_value = serializers.DecimalField( max_digits=8,
        decimal_places=2,)
    cpf = serializers.CharField(max_length=11)
    card = serializers.CharField(max_length=12)
    transaction_hour = serializers.TimeField()
    store_owner = serializers.CharField(max_length=50)
    store_name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Process.objects.create(**validated_data)

