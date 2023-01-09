from fastapi import FastAPI
from routes.reports import routes

#coneccion con fastapi
app = FastAPI()
app.include_router(routes, prefix="/reports")
