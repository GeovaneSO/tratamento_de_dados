from rest_framework import serializers
from .models import Process
from django.contrib.auth.models import User


class ProcessSerializer(serializers.Serializer):
    transaction_type = serializers.IntegerField()
    transaction_date = serializers.DateField(format="%Y-%m-%d")
    transaction_value = serializers.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    cpf = serializers.CharField(max_length=11)
    card = serializers.CharField(max_length=12)
    transaction_hour = serializers.TimeField()
    store_owner = serializers.CharField(max_length=50)
    store_name = serializers.CharField(max_length=50)

    def create(self, validated_data: dict):
        store_owner: str = validated_data.pop("store_owner")
        cpf: str = validated_data.pop("cpf")

        username: str = store_owner.lower().replace(" ", "")
        email: str = f"{username}@mail.com"

        User.objects.get_or_create(username=username, password=cpf, email=email)

        return Process.objects.create(
            **validated_data, cpf=cpf, store_owner=store_owner
        )
