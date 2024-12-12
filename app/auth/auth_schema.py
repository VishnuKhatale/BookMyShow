from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

# OAuth2 schema
oauth2_schema = OAuth2PasswordBearer(tokenUrl="api/v1/users/token/")