import redis

#coneccion independiente con la db de redis para evitar errores 
stream = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)