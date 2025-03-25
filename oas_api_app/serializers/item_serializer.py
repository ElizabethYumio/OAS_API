from rest_framework import serializers

from ..models import Item

class ItemSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    from .bid_serializer import BidSerializer
    from .user_serializer import UserSerializer
    from .tag_serializer import TagSerializer

    bids = BidSerializer(many = True)
    tags = TagSerializer(many = True)
    user = UserSerializer(many = False)
    
    class Meta:
        model = Item
        fields = '__all__'
