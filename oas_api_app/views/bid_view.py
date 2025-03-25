from rest_framework.response import Response
from rest_framework.views import APIView
import json

from ..models import Bid
from ..services import BidService
from ..serializers import BidSerializer
from ..common import BidConstants
from ..dtos import CreateBidDTO

class BidListView(APIView):
    path = "bid"
    name = "Bid List"
    
    def get(self, request):
        buyer_id = request.query_params.get(BidConstants.QUERY_PARAM_BUYER_ID)
        bids: Bid[int] = []

        if (buyer_id):
            bids = BidService.get_bids_by_buyer_id(self, buyer_id)
        else:
            bids = BidService.get_bids(self)
        
        serializer = BidSerializer(bids, many=True)
        response = serializer.data
        return Response(response)
    
    def post(self, request):
        bid_dto = CreateBidDTO.from_request_body(self, request)

        bid = BidService.create_or_update_bid(self, bid_dto)
        
        serializer = BidSerializer(bid, many=False)
        response = serializer.data
        return Response(response)
