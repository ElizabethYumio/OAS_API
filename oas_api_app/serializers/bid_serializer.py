from rest_framework import serializers

from ..models import Bid

class BidSerializer(serializers.ModelSerializer):
    from .item_serializer import ItemSimpleSerializer
    from .user_serializer import UserSimpleSerializer

    item = ItemSimpleSerializer(many = False)
    buyer = UserSimpleSerializer(many = False)

    is_winning = serializers.SerializerMethodField()

    class Meta:
        model = Bid
        fields = '__all__'

    def get_is_winning(self, obj):
        return not Bid.objects.filter(
            item=obj.item,
            amount__gt=obj.amount
        ).exists()
