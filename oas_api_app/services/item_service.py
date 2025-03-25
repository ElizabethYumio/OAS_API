from django.db.models import Prefetch, Count, Q
from uuid import UUID

from ..models import Item, Bid
from ..common import utils
from ..dtos import CreateItemDTO, UpdateItemDTO

def parse_tags(tags):
    if tags:
        return [int(tag) for tag in tags.split(',')]
    return []

class ItemService():
    def get_items(self, query):
        items = Item.objects.filter(name__icontains = query)
        return items
    
    def get_items_excluding_user_id(self, user_id: UUID, query: str, tags):
        tags = parse_tags(tags)

        filters = {
            'name__icontains': query
        }

        # Apply filters based on tags if provided
        if tags:
            filters['tags__id__in'] = tags
            items = Item.objects.filter(**filters).annotate(
                matching_tags=Count('tags', filter=Q(tags__id__in=tags))
            ).filter(
                matching_tags=len(tags)
            )
        else:
            items = Item.objects.filter(**filters)

        # Exclude items from the specified user and return distinct results
        return items.exclude(user__id=user_id).distinct()

    def get_items_by_user_id(self, user_id: UUID, query: str, tags):
        tags = parse_tags(tags)

        filters = {
            'user__id': user_id,
            'name__icontains': query
        }

        # Apply filters based on tags if provided
        if tags:
            filters['tags__id__in'] = tags
            items = Item.objects.filter(**filters).annotate(
                matching_tags=Count('tags', filter=Q(tags__id__in=tags))
            ).filter(
                matching_tags=len(tags)
            )
        else:
            items = Item.objects.filter(**filters)

        # Return the filtered items for the specified user
        return items.distinct()
    
    def get_item(self, id):
        item = Item.objects.prefetch_related(
            Prefetch(
                'bids',
                queryset = Bid.objects.select_related('buyer').order_by('-amount')
            )
        ).get(id = id)
        return item
    
    def create_item(self, item_dto: CreateItemDTO):
        item_dict = item_dto.to_dict()

        item = Item.objects.create(**item_dict)
        return item
    
    def update_item(self, item_dto: UpdateItemDTO, id):
        item = Item.objects.get(id = id)

        utils.update_from_dto(item, item_dto)
        item.save()

        return item
