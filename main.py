from typing import List

from fastapi import FastAPI, requests
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

app = FastAPI()


@app.get("/ping")
def ping():
    return Response("pong")

class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: object

Car_list: List[Car] = []

def serialized_car():
    Car_serialized = []
    for car in Car_list:
        Car_serialized.append(car.model_dump())
    return Car_serialized
@app.post("/car")
def create_car(car: Car):
    Car_list.append(car)
    return JSONResponse(content="Car created",status_code=201)
@app.get("/cars")
def get_cars():
    return JSONResponse(content=serialized_car(), status_code=200)

@app.get("/car/{identifier}")
def get_car(identifier: str):
    for car in Car_list:
        if car.identifier == identifier:
            return JSONResponse(content=car, status_code=200)
        return JSONResponse(content=f"Car not found", status_code=404)

class Characteristic(BaseModel):
    max_speed: int
    max_fuel_capacity: int

@app.put("/car/{identifier}/characteristics")
def update_characteristics(identifier: int ,char: Characteristic):
    for car in Car_list:
        if car.identifier == identifier:
            car.characteristics = char
            Car_list.append(car)
            serialized_car()
            return JSONResponse(content=car.characteristics, status_code=200)
        else:
            return JSONResponse(content=f"Car not found", status_code=404)



