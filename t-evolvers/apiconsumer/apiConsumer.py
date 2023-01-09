import redis
import random
from datetime import datetime
from random import randint
import time
from API.routes.reports import create

# coneccion con la db de redis
STREAM_KEY = "report"
stream = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# lista para guardar los ids de transmicion de los eventos de redis
id_events = []

def readevents():
    l_id= 0
    
    while True:
        # se escuchando los eventos de redis empezando por el mas antiguo
        event = stream.xread(streams={STREAM_KEY: l_id}, count=1, block=4000)
        try:
            # se agrega el id de transmision a la lista donde se guardan
            id_events.append(event[0][1][0][0])
        except IndexError:
            try:
                # se guarda en la "db" el dato obtenido de la db de redis mediante el id de transmision usando la funcion create de la API crud.
                list_id = 0
                id_metric = (id_events[list_id])
                data = create(id_metric)
                print(data)
                id_events.remove(id_metric)

            except IndexError:
                #caso en el que no hay transmisiones por escuchar
                print(f"no hay mas datos por ahora, ({datetime.now()})")

        #se aprovecha el tiempo en que no hay transmisiones por escuchar para guardar en la "db" las que ya estan en la lista de ids 
        if len(event) == 0:
            try:
                # se guarda en la "db" el dato obtenido de la db de redis mediante el id de transmision usando la funcion create de la API crud.
                list_id = 0
                id_metric = (id_events[list_id])
                data = create(id_metric)
                print(data)
                id_events.remove(id_metric)
            except IndexError:
                print(f"no hay mas datos por ahora, ({datetime.now()})")
        else:
            # se aumenta el contador para guardar los ids de transmision (se aumenta al del siguiente evento)
            now = event[0]
            current_event = now[1][0][0]
            l_id= current_event

readevents()
