
from sqlalchemy.inspection import inspect
import hashlib
import base64
from config import SECRET_KEY

class Serializer():

    @staticmethod
    def serialize(model):
        return {c: getattr(model, c) for c in inspect(model).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [Serializer.serialize(m) for m in l]
    

class Encrypt():

    @staticmethod
    def encrypt(password):
        # Concatena la contraseña y el salt
        data_to_hash = password.encode() + SECRET_KEY.encode()

        # Crea el hash SHA-512
        hashed = hashlib.sha512(data_to_hash).digest()

        # Codifica el hash resultante en base64
        return base64.urlsafe_b64encode(hashed).decode()