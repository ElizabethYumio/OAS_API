from uuid import UUID
import json

from ..models import User, Item
from ..common import utils

FIELD_NAME = "name"
FIELD_IMAGE_URL = "image_url"
FIELD_DESCRIPTION = "description"
FIELD_START_PRICE = "start_price"
FIELD_END_DATE = "end_date"
FIELD_USER_ID = "user_id"
FIELD_STATUS = "status"
FIELD_STEP = "step"

class CreateItemDTO:
    def __init__(self, name, image_url, description, start_price, end_date, user_id, status, step):
        self.name = name
        self.image_url = image_url
        self.description = description
        self.start_price = start_price
        self.end_date = end_date
        self.user_id = user_id
        self.status = status
        self.step = step

    def from_request_body(self, request) -> "CreateItemDTO":
        try:
            body = json.loads(request.body)

            name = body.get(FIELD_NAME)
            image_url = body.get(FIELD_IMAGE_URL)
            description = body.get(FIELD_DESCRIPTION)
            start_price = float(body.get(FIELD_START_PRICE))
            step = float(body.get(FIELD_STEP))
            end_date = body.get(FIELD_END_DATE)
            user_id = UUID(body.get(FIELD_USER_ID))
            status = body.get(FIELD_STATUS)

            return CreateItemDTO(
                name=name,
                image_url=image_url,
                description=description,
                start_price=start_price,
                end_date=end_date,
                user_id=user_id,
                status=status,
                step=step
            )

        except (ValueError, KeyError, TypeError) as e:
            raise ValueError(f"Invalid request body: {e}")
        
    def to_dict(self) -> dict:
        return utils.dto_to_dict(self)
        
class UpdateItemDTO:
    def __init__(self, name, image_url, description, start_price, step, end_date, status):
        self.name = name
        self.image_url = image_url
        self.description = description
        self.start_price = start_price
        self.step = step
        self.end_date = end_date
        self.status = status

    def from_request_body(self, request) -> "UpdateItemDTO":
        try:
            body = json.loads(request.body)

            name = body.get(FIELD_NAME)
            image_url = body.get(FIELD_IMAGE_URL)
            description = body.get(FIELD_DESCRIPTION)
            start_price = float(body.get(FIELD_START_PRICE))
            end_date = body.get(FIELD_END_DATE)
            status = body.get(FIELD_STATUS)

            return UpdateItemDTO(
                name=name,
                image_url=image_url,
                description=description,
                start_price=start_price,
                end_date=end_date,
                status=status
            )

        except (ValueError, KeyError, TypeError) as e:
            raise ValueError(f"Invalid request body: {e}")
