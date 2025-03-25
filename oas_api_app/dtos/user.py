import json
import bcrypt

from ..common import UserConstants

class CreateUserDTO:
    def __init__(self, username, email, password, address, phone, avatar_url):
        self.username = username
        self.email = email
        self.password = password
        self.address = address
        self.phone = phone
        self.avatar_url = avatar_url

    def hash_password(self) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def from_request_body(self, request) -> "CreateUserDTO":
        try:
            body = json.loads(request.body)

            username = body.get(UserConstants.FIELD_USERNAME)
            email = body.get(UserConstants.FIELD_EMAIL)
            password = body.get(UserConstants.FIELD_PASSWORD)
            address = body.get(UserConstants.FIELD_ADDRESS)
            phone = body.get(UserConstants.FIELD_PHONE)
            avatar_url = body.get(UserConstants.FIELD_AVATAR_URL)

            return CreateUserDTO(
                username = username,
                email = email,
                password = password,
                address = address,
                phone = phone,
                avatar_url = avatar_url,
            )

        except (ValueError, KeyError, TypeError) as e:
            raise ValueError(f"Invalid request body: {e}")

class UpdateUserDTO:
    def __init__(self, username, email, password, address, phone, avatar_url, payment_info):
        self.username = username
        self.email = email
        self.password = password
        self.address = address
        self.phone = phone
        self.avatar_url = avatar_url
        self.payment_info = payment_info

    def hash_password(self) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def from_request_body(self, request) -> "UpdateUserDTO":
        try:
            body = json.loads(request.body)

            username = body.get(UserConstants.FIELD_USERNAME)
            email = body.get(UserConstants.FIELD_EMAIL)
            password = body.get(UserConstants.FIELD_PASSWORD)
            address = body.get(UserConstants.FIELD_ADDRESS)
            phone = body.get(UserConstants.FIELD_PHONE)
            avatar_url = body.get(UserConstants.FIELD_AVATAR_URL)
            payment_info = body.get(UserConstants.FIELD_PAYMENT_INFO)

            return UpdateUserDTO(
                username = username,
                email = email,
                password = password,
                address = address,
                phone = phone,
                avatar_url = avatar_url,
                payment_info = payment_info
            )

        except (ValueError, KeyError, TypeError) as e:
            raise ValueError(f"Invalid request body: {e}")

class LoginUserDTO:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

    def from_request_body(self, request) -> "LoginUserDTO":
        try:
            body = json.loads(request.body)

            username = body.get(UserConstants.FIELD_USERNAME)
            password = body.get(UserConstants.FIELD_PASSWORD)

            return LoginUserDTO(
                username=username,
                password=password,
            )

        except (ValueError, KeyError, TypeError) as e:
            raise ValueError(f"Invalid request body: {e}")
