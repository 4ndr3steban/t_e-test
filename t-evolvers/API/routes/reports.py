from fastapi import APIRouter
from redisconections import crud

routes = APIRouter()

#simulacion de db para guardar datos
fake_db = []

# crear (guardar) datos obtenidos de redis en una db
@routes.post("/create/{id}", response_model=dict)
def create(id: str):
    try:
        # se obtiene el dato del id de stream especifico y se agrega a la db local  
        data = dict(crud.get_hash(id))
        fake_db.append(data)
        return data

    except Exception as e:
        print(e)

# obtener (mostrar) datos obtenidos de redis en una db
@routes.get("/metrica/{id}")
def get(id: str):
    try:

        # se busca el dato en la db de redis
        data = crud.get_hash(key=id)

        # si por alguna razon el dato no existe en la db de redis, se busca en la db local como ultimo recurso
        if len(data) == 0:

            return list(filter(lambda rep: rep["item_id"] == id, fake_db))[0]
        return data
    except Exception as e:
        print(e)

# eliminar datos obtenidos de redis en una db
@routes.delete("/delete/{id}")
def delete(id: str):
    try:
        
        # se elimina el dato de la db de redis
        crud.delete_hash(id)

        # se busca el dato a eliminar y se remueve de la db local
        rep = list(filter(lambda rep: rep["item_id"] != id, fake_db))
        if len(rep) != 0:
            fake_db.remove(rep)

        return {"mensaje": "success"}
    except Exception as e:
        print(e)
