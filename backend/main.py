from fastapi import FastAPI
import requests
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

class DeviceRequest(BaseModel):
    device_id: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"ESP32": "Backend is running"}   

@app.post("/led")
def control_led(data: DeviceRequest):
    # Simple logic
    if data.device_id == "esp32_1":
        return {"action": "ON"}
    else:
        return {"action": "OFF"}
