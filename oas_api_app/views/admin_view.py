from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json

from ..models import Admin
from ..services import AdminService
from ..dtos import LoginAdminDTO
from ..common import AdminConstants
from ..serializers import AdminSerializer

class AdminLoginView(APIView):
    name = "User Login"

    def post(self, request):
        data = json.loads(request.body)

        admin_login_dto = LoginAdminDTO(
            username=data[AdminConstants.FIELD_USERNAME],
            password=data[AdminConstants.FIELD_PASSWORD],
        )
        response = AdminService.login_admin(self, admin_login_dto)
        return Response(response)


