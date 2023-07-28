from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.palette import router as palette_router


app = FastAPI()
app.include_router(palette_router, prefix='/palette', tags=['palette'])

app.mount('/', app=StaticFiles(directory='static', html=True), name='static')
