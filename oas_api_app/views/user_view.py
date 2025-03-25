from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json

from ..models import User
from ..services import UserService
from ..dtos import CreateUserDTO, UpdateUserDTO, LoginUserDTO, NotFoundDTO
from ..common import UserConstants
from ..serializers import UserSerializer

class UserListView(APIView):
    name = "User List"
    
    def get(self, request):
        response = UserService.get_users(self)
        return Response(response)
    
    def post(self, request):
        user_dto = CreateUserDTO.from_request_body(self, request)

        response = UserService.create_user(self, user_dto)
        return Response(response)
        
class UserDetailView(APIView):
    name = "User Detail"

    def get(self, request, id):
        response = UserService.get_user_by_id(self, id)
        return Response(response)
    
    def put(self, request, id):
        try:
            user_dto = UpdateUserDTO.from_request_body(self, request)

            user = UserService.update_user(self, user_dto, id)
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data)
        
        except User.DoesNotExist:
            not_found_data = NotFoundDTO(
                message = "Item not found!"
            ).to_dict()

            return Response(not_found_data, status = status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):

        if UserService.delete_user(self, id):
            return Response({'message': 'User deleted successfully.'}, status=200)
        else:
            return Response({'error': 'User not found.'}, status=404)
        
class UserLoginView(APIView):
    name = "User Login"

    def post(self, request):
        data = json.loads(request.body)

        user_login_dto = LoginUserDTO(
            username=data[UserConstants.FIELD_USERNAME],
            password=data[UserConstants.FIELD_PASSWORD],
        )
        response = UserService.login_user(self, user_login_dto)
        return Response(response)


