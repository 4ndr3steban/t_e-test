from conection import stream
from redis.exceptions import ResponseError
from datetime import datetime

#key para coneccion con la db de redis
STREAM_KEY = "report"

#crud para guardar datos en la db de redis 
def save_hash(data: dict):
    try:
        stream.xadd(STREAM_KEY,data)
    except ResponseError as e:
        print(e)


#obtener datos de la db de redis
def get_hash(key: str):
    try:
        #se lee un dato especifico y se retorna el diccionario con los valores de interes
        try:
            event = stream.xread(streams={STREAM_KEY: key}, count=1, block=4000)
            return event[0][1][0][1]
        except IndexError:
            return {"message:" f"no hay mas datos por ahora, ({datetime.now()})"}

    except ResponseError as e:
        print(e)

#eliminar datos de la db de redis
def delete_hash(key: str):
    try:
        #se elimina el dato especificado
        stream.xdel(STREAM_KEY, key)

    except ResponseError as e:
        print(e)