from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Inicia el server: uvicorn fichero:app --reload

#Entidad usuario

class User(BaseModel):
  id: int
  name: str
  surname: str
  age: int
  url: str

users_list = [User(id = 1, name = "Ulisao", surname = "Baretta", age = 22, url = "lol.com"),
User(id = 2, name = "Ulises", surname = "Baretta", age = 23, url = "lol.com"),
User(id = 3, name = "Lolaso", surname = "Baretta", age = 22, url = "lol.com")]

@app.get("/usersclass")
async def usersclass():
  return User(name = "Ulisao", surname = "Baretta", age = 22, url = "lol.com")


@app.get("/users")
async def users():
  return users_list


#path
@app.get("/user/{id}")
async def user(id: int):
  return search_user(id)


#query
@app.get("/user/")
async def user(id: int):
  return search_user(id)

@app.post("/user/")
async def user(user: User):
  if type(search_user(user.id)) == User :
    return {"error": "El usuario existe"}
  else:
    users_list.append(user)
    return user

@app.put("/user/")
async def user(user: User):

  found = False

  for index, saved_user in enumerate(users_list):
    if saved_user.id == user.id:
      users_list[index] = user
      found = True

  if not found:
    return {"error": "El usuario no se ha actualizado"}
  else:
    return user
  
@app.delete("/user/{id}")
async def user(id: int):

  found = False
  for index, saved_user in enumerate(users_list):
    if saved_user.id == id:
      del users_list[index]
      found = True

  if not found:
    return {"error": "El usuario no se ha eliminado"}


def search_user(id: int):
  users = filter(lambda user: user.id == id, users_list)
  try:
    return list(users)[0]
  except:
    return {"error": "No se encontro usuario"}
  

