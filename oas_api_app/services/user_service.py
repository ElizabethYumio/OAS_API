from django.core.exceptions import ObjectDoesNotExist

import bcrypt

from ..models import User
from ..serializers import UserSerializer
from ..dtos import LoginUserDTO
from ..common import utils
from django.db import IntegrityError

class UserService():
    def get_users(self):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return (serializer.data)
    
    def get_user_by_id(self, id):
        user = User.objects.get(id = id)
        serializer = UserSerializer(user, many=False)
        return (serializer.data)
    
    def login_user(self, user_login_dto: LoginUserDTO):
        try:
            user = User.objects.get(username=user_login_dto.username)
            if bcrypt.checkpw(user_login_dto.password.encode('utf-8'), user.password.encode('utf-8')):
                serializer = UserSerializer(user, many=False)
                return serializer.data
            else:
                raise ValueError("Invalid password")
        except ObjectDoesNotExist:
            raise ValueError("User does not exist.")
        
    def create_user(self, user_dto):
        hashed_password = user_dto.hash_password()
        try:
            user = User.objects.create(
                username=user_dto.username,
                email=user_dto.email,
                password=hashed_password,
                address=user_dto.address,
                phone=user_dto.phone,
                avatar_url=user_dto.avatar_url,
            )
            serializer = UserSerializer(user, many=False)
            return serializer.data
        except IntegrityError:
            raise ValueError("User with this username or email already exists.")
    
    def update_user(self, user_dto, id):
        try:
            user = User.objects.get(id=id)

            utils.update_from_dto(user, user_dto)

            if user_dto.password:
                user.password = user_dto.hash_password()
                
            user.save()
            return user
        except ObjectDoesNotExist:
            raise ValueError("User does not exist.")
    
    def delete_user(self, id):
        try:
            user = User.objects.get(id = id)
            user.delete()
            return True
        except ObjectDoesNotExist:
            return False
    
    def hash_password(password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
