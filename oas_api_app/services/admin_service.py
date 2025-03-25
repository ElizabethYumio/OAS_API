from django.core.exceptions import ObjectDoesNotExist

import bcrypt

from ..models import Admin
from ..serializers import AdminSerializer
from ..dtos import LoginAdminDTO
from ..common import utils
from django.db import IntegrityError

class AdminService():
    def login_admin(self, admin_login_dto: LoginAdminDTO):
        try:
            admin = Admin.objects.get(username=admin_login_dto.username)
            if bcrypt.checkpw(admin_login_dto.password.encode('utf-8'), admin.password.encode('utf-8')):
                serializer = AdminSerializer(admin, many=False)
                return serializer.data
            else:
                raise ValueError("Invalid password")
        except ObjectDoesNotExist:
            raise ValueError("User does not exist.")
    
    def hash_password(password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    
    