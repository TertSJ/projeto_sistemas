from fastapi import FastAPI
from controller.Controlador import Controlador
app = FastAPI()

@app.get("/")
def hello_world_root():
    return {"Hello": "World"}

@app.get("/{item_0}/{item_1}/{item_2}")
def captacaoURL(item_0: str, item_1:int, item_2:int):
    processo = Controlador()
    return {"Resultado": processo.redirecionar(item_0,item_1,item_2)}
