from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..services import ItemService
from ..dtos import CreateItemDTO, UpdateItemDTO, NotFoundDTO
from ..models import Item
from ..common import ItemConstants, CommonConstants
from ..serializers import ItemSerializer

class ItemListView(APIView):
    name = "Item List"
    
    def get(self, request):
        query = request.GET.get(ItemConstants.QUERY_PARAM_SEARCH_QUERY, CommonConstants.EMPTY_STRING)
        tagstr = request.GET.get(ItemConstants.QUERY_PARAM_TAGS)
        user_id = request.GET.get(ItemConstants.QUERY_PARAM_USERID)
        excluding_user_id = request.GET.get(ItemConstants.QUERY_PARAM_EXCLUDING_USERID)

        if (user_id):
            items = ItemService.get_items_by_user_id(self, user_id, query, tagstr)
        elif (excluding_user_id):
            items = ItemService.get_items_excluding_user_id(self, excluding_user_id, query, tagstr)
        else:
            items = ItemService.get_items(self, query)

        serializer = ItemSerializer(items, many=True)
        response = serializer.data
        return Response(response)
    
    def post(self, request):
        item_dto = CreateItemDTO.from_request_body(self, request)
        
        item = ItemService.create_item(self, item_dto)

        serializer = ItemSerializer(item, many=False)
        response = serializer.data
        return Response(response)
    
class ItemDetailView(APIView):
    name = "Item Detail"

    def get(self, request, id):
        try:
            item = ItemService.get_item(self, id)

            serializer = ItemSerializer(item, many=False)
            response = serializer.data
            return Response(response)
        
        except Item.DoesNotExist:
            not_found_data = NotFoundDTO(
                message = "Item not found!"
            ).to_dict()

            return Response(not_found_data, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id):
        try:
            item_dto = UpdateItemDTO.from_request_body(self, request)
        
            item = ItemService.update_item(self, item_dto, id)

            serializer = ItemSerializer(item, many=False)
            response = serializer.data
            return Response(response)
        
        except Item.DoesNotExist:
            not_found_data = NotFoundDTO(
                message = "Item not found!"
            ).to_dict()

            return Response(not_found_data, status=status.HTTP_404_NOT_FOUND)
