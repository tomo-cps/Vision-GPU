# uvicorn fast:app --host 0.0.0.0 --port 8000
from fastapi import FastAPI
import pynvml
import socket
import os

hostname = socket.gethostname()
print("マシンのホスト名:", hostname)

username = os.getlogin()
print("Logged-in username:", username)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # NVIDIAドライバーと関連ライブラリを初期化
    pynvml.nvmlInit()

@app.on_event("shutdown")
async def shutdown_event():
    # NVIDIAドライバーと関連ライブラリをクリーンアップ
    pynvml.nvmlShutdown()

@app.get("/"+hostname)
async def get_gpu_info():
    gpu_info = []

    # 利用可能なGPUの数を取得
    device_count = pynvml.nvmlDeviceGetCount()

    # 各GPUの情報を取得
    for i in range(device_count):
        gpu_data = {}
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        gpu_name = pynvml.nvmlDeviceGetName(handle)


        memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        total_memory = memory_info.total // (1024 * 1024)
        used_memory = memory_info.used // (1024 * 1024)
        memory_utilization = (used_memory / total_memory) * 100



        utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
        fan_speed = pynvml.nvmlDeviceGetFanSpeed(handle)
        temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)

        gpu_data["MachineName"] = hostname
        gpu_data["LoginUser"] = username
        gpu_data["GPU"] = f"GPU{i}"
        gpu_data["Name"] = gpu_name

        gpu_data["TotalMemory"] = f"{total_memory} MB"
        gpu_data["UsedMemory"] = f"{used_memory}MB/{total_memory} MB"
        gpu_data["MemoryUtilization"] = f"{memory_utilization:.2f}%"


        gpu_data["Utilization"] = f"{utilization.gpu}%"
        gpu_data["FanSpeed"] = f"{fan_speed}%"
        gpu_data["Temperature"] = f"{temperature}°C"
        # gpu_data["ImgPath"] = "../assets/"+hostname+".png"
        gpu_data["ImgPath"] = f"../assets/"+hostname+".png"

        gpu_info.append(gpu_data)
        print(gpu_info)

    return gpu_info

