import asyncio
from random import randint
import random
from datetime import datetime
import redis

# se crea la coneccion con la db en redis
STREAM_KEY = "report"
stream = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# funcion asincrona para generar los datos de forma aleatoria 
async def application():
    i = 0
    while True:
        # se generan datos con una id de dispositivo, una medida aleatoria y un timestamo cada cierto tiempo
        await asyncio.sleep(random.uniform(1,4))
        event = {"item_id": 523304, "kwh": randint(10,100), "Timestamp": str(datetime.now())}
        id = stream.xadd(STREAM_KEY,event)
        print("event_id: ",  id)
        print(event)
        


# se ejecuta la funcion "application" de manera asincrona con un loop de asyncio
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(application())
except KeyboardInterrupt:
    pass
finally:
    print("closing")
    loop.close()
