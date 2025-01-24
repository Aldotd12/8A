'''Operacion CRUD con FastApi'''
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI
from fastapi import HTTPException
from models import Genero, Roles, User, UpdateUser

app = FastAPI()

db : List[User] = [
    User(
        id = uuid4(),
        nombre = "Aldo",
        apellidos = "Tolentino",
        genero = Genero.masculino,
        roles = [Roles.admin],
    ),
    User(
        id = uuid4(),
        nombre = "Diego",
        apellidos = "Tolentino",
        genero = Genero.masculino,
        roles = [Roles.user],
    ),
    User(
        id = uuid4(),
        nombre = "Kalid",
        apellidos = "Reyes",
        genero = Genero.masculino,
        roles = [Roles.user],
    ),
    User(
        id=uuid4(),
        nombre="Ivan",
        apellidos="Marquez",
        genero=Genero.masculino,
        roles=[Roles.user],
    ),
]
@app.get('/')
async def root():
    return{"saludo": "hola!"}
@app.get('/api/users')
async def get_users():
    return db
@app.post('/api/users')
async def create_user(user : User):
    db.append(user)
    return {"id" : user.id}
@app.delete("/api/users/{nombre}")
async def delete_user(nombre):
    for user in db:
        if user.nombre.lower() == nombre.lower():
            db.remove(nombre)
            return {"mensaje"f"Eliminado correctamente {nombre}."}
        
        raise HTTPException(
            status_code=404, detail=f"Error al eliminar a {nombre} no encontrado."
        )
@app.put("/users/{id}")
async def update_user(id: UUID, user_update: UpdateUser):
    for user in db:
        if user.id == id:
            if user_update.nombre is not None:
                user.nombre = user_update.nombre
            if user_update.apellidos is not None:
                user.apellidos = user_update.apellidos
            if user_update.genero is not None:
                user.genero = user_update.genero
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"message": f"Usuario con ID {id} actualizado exitosamente."}
    raise HTTPException(
        status_code=404, detail=f"Error al actualizar, ID {id} no encontrado."
    )