import redis
import random
from datetime import datetime
from random import randint
import time

# coneccion con la db de redis
STREAM_KEY = "report"
stream = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

l_id= 0

while True:

    # se escuchando los eventos de redis empezando por el mas antiguo
    event = stream.xread(streams={STREAM_KEY: l_id}, count=1, block=4000)
    try:

        # se guarda el diccionario con la metrica
        pre_alert = event[0][1][0][1]
        kwh = pre_alert["kwh"]

        #condicional para imprimir una alerta si la metrica supera el numero 50
        if int(kwh) >= 50:
            txt = "\n======================================\n"
            txt += f"\tSe superó el umbral de 50 kwh en el dato de la fecha {pre_alert['Timestamp']}\n"
            txt += "\n=====================================\n"
            print(txt)
    except IndexError:
        print(f"no hay mas datos por ahora, ({datetime.now()})")

    #sleep para esperar si no hay mas datos por leer
    if len(event) == 0:
        time.sleep(4)
    else:
        # se aumenta el contador para guardar los ids de transmision (se aumenta al del siguiente evento)
        now = event[0]
        current_event = now[1][0][0]
        time.sleep(random.randint(1, 2))
        l_id= current_event