from ..dtos import CreateBidDTO
from ..models import Bid
from ..common import BidConstants

class BidService():
    def get_bids(self):
        bids = Bid.objects.select_related(BidConstants.FIELD_ITEM).all()
        return bids
    
    def get_bids_by_buyer_id(self, buyer_id):
        bids = Bid.objects.select_related(BidConstants.FIELD_ITEM).filter(buyer = buyer_id)
        return bids
    
    def create_or_update_bid(self, create_bid_dto: CreateBidDTO) -> Bid:
        bid = Bid.objects.filter(
            buyer__id = create_bid_dto.buyer_id, 
            item__id = create_bid_dto.item_id
        ).first()

        if bid:
            bid.amount = create_bid_dto.amount
            bid.save()
        else:
            bid = create_bid_dto.to_model()
            bid.save()

        return bid 
