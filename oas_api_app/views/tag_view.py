from rest_framework.views import APIView
from rest_framework.response import Response

from ..services import TagService
from ..serializers import TagSerializer

class TagListView(APIView):
    path = "tag"
    name = "Tag List"
    
    def get(self, request):
        tags = TagService.get_tags(self)
        
        serializer = TagSerializer(tags, many = True)
        return Response(serializer.data)
