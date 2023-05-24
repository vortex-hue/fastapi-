## password hashing
from passlib.context import CryptContext


## creating an instance for the hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hashing class
class Hash():
    def bcrypt(password: str):
        return pwd_context.hash(password)

    def verify(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)