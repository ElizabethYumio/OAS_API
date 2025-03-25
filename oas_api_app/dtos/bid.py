from uuid import UUID
import json

from ..models import Bid, User, Item

FIELD_NAME_BUYER_ID = "buyer_id"
FIELD_NAME_ITEM_ID = "item_id"
FIELD_NAME_AMOUNT = "amount"

class CreateBidDTO:
    buyer_id: UUID
    item_id: UUID
    amount: float

    def __init__(self, buyer_id: UUID, item_id: UUID, amount: float):
        self.buyer_id = buyer_id
        self.item_id = item_id
        self.amount = amount

    def to_model(self) -> Bid:
        from django.core.exceptions import ObjectDoesNotExist

        try:
            buyer = User.objects.get(id=self.buyer_id)
            item = Item.objects.get(id=self.item_id)

            return Bid(
                buyer = buyer, 
                item = item, 
                amount = self.amount,
            )

        except ObjectDoesNotExist as e:
            raise ValueError(f"Invalid buyer_id or item_id: {e}")
        
    def from_request_body(self, request) -> "CreateBidDTO":
        try:
            body = json.loads(request.body)

            buyer_id = UUID(body.get(FIELD_NAME_BUYER_ID))
            item_id = UUID(body.get(FIELD_NAME_ITEM_ID))
            amount = float(body.get(FIELD_NAME_AMOUNT))

            return CreateBidDTO(
                buyer_id = buyer_id, 
                item_id = item_id, 
                amount = amount
            )

        except (ValueError, KeyError, TypeError) as e:
            raise ValueError(f"Invalid request body: {e}")
