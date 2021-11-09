from rest_framework import serializers

import uuid

from core.models import Payment, Token

class TokenSerializer(serializers.Serializer):
    uuid = serializers.ReadOnlyField()
    card_number = serializers.CharField()
    card_holder = serializers.CharField()
    exp_month = serializers.IntegerField()
    exp_year = serializers.IntegerField()
    active = serializers.ReadOnlyField()

    def create(self, data):
        data["uuid"] = uuid.uuid4()
        token = Token(**data)
        token.save()
        return token

class PaymentSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    token_id = serializers.IntegerField()
    created_at = serializers.ReadOnlyField()
    update_at = serializers.ReadOnlyField()

    def create(self, data):
        payment = Payment(**data)
        payment.save()
        return payment

class PaymentSearchSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    created_at = serializers.ReadOnlyField()
    update_at = serializers.ReadOnlyField()