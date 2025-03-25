import json
import bcrypt

from ..common import AdminConstants
class LoginAdminDTO:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

    def from_request_body(self, request) -> "LoginAdminDTO":
        try:
            body = json.loads(request.body)

            username = body.get(AdminConstants.FIELD_USERNAME)
            password = body.get(AdminConstants.FIELD_PASSWORD)

            return LoginAdminDTO(
                username=username,
                password=password,
            )

        except (ValueError, KeyError, TypeError) as e:
            raise ValueError(f"Invalid request body: {e}")