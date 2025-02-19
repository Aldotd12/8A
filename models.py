from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Genero(str, Enum):
    masculino = "masculino"
    femenino = "femenino"
    otro = "39 tipos de gays"
class Roles(str, Enum):
    admin = "admin"
    user = "user"
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    nombre : str
    apellidos : str
    genero : Genero
    roles : List[Roles]
class UpdateUser(BaseModel):
    nombre : Optional[str] = None
    apellidos : Optional[str] = None
    genero : Optional[Genero] = None
    roles : Optional[List[Roles]] = None           