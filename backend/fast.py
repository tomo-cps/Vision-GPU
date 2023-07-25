# uvicorn fast:app --host 0.0.0.0 --port 8000
from fastapi import FastAPI
import pynvml
import socket
import pexpect
import subprocess

hostname = socket.gethostname()
print("マシンのホスト名:", hostname)

pynvml.nvmlInit()
device_count = pynvml.nvmlDeviceGetCount()
print(device_count)


def get_username_detailuser():
    child = pexpect.spawn("who")
    child.expect(pexpect.EOF)
    detailuser = child.before.decode().strip()
    usernames = detailuser.split("\n")
    lst=[]
    for user in usernames:
        user = user.split(" ")
        lst.append(user[0])
    usernames = list(set(lst))
    result = subprocess.check_output("who")
    detailuser = result.decode().strip().split("\n")
    return usernames, detailuser

print(get_username_detailuser())

class FetchGPUData():
    def __init__(self):
        self.gpu_data = {"MachineName": "",
                        "UserNames" : "",
                        "DetailUser" : "",
                        "GPU" : "",
                        "GPUName" : "",
                        "TotalMemory" : "",
                        "UsedMemory": "",
                        "MemoryUtilization" : "",
                        "Utilization" : "",
                        "FanSpeed" : "",
                        "Temperature" : "",
                        "ImgPath" : ""
                        }
    def __call__(self, gpu_number):
        for i in range(gpu_number):
            if i==0:
                self.get_gpu_data(i, "")
            else:
                self.get_gpu_data(i, "/")
        return self.gpu_data

    def get_gpu_data(self, gpu_number, add_string):
        handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_number)
        gpu_name = pynvml.nvmlDeviceGetName(handle)

        memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        total_memory = memory_info.total // (1024 * 1024)
        used_memory = memory_info.used // (1024 * 1024)
        memory_utilization = (used_memory / total_memory) * 100

        utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
        fan_speed = pynvml.nvmlDeviceGetFanSpeed(handle)
        temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)

        self.gpu_data["MachineName"] = hostname
        self.gpu_data["UserNames"] = get_username_detailuser()[0]
        self.gpu_data["DetailUser"] = get_username_detailuser()[1]
        self.gpu_data["GPU"] += f"{add_string}GPU{gpu_number}"
        self.gpu_data["GPUName"] += f"{add_string}{gpu_name}"
        self.gpu_data["TotalMemory"] += f"{add_string}{total_memory} MB"
        self.gpu_data["UsedMemory"] += f"{add_string}{used_memory}MB/{total_memory} MB"
        self.gpu_data["MemoryUtilization"] += f"{add_string}{memory_utilization:.2f}%"
        self.gpu_data["Utilization"] += f"{add_string}{utilization.gpu}%"
        self.gpu_data["FanSpeed"] += f"{add_string}{fan_speed}%"
        self.gpu_data["Temperature"] += f"{add_string}{temperature}°C"
        self.gpu_data["ImgPath"] = f"/img/"+hostname+".png"
        
        return self.gpu_data

# print(output.get_gpu_data(0, ))

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
    device_count = pynvml.nvmlDeviceGetCount()
    output = FetchGPUData()
    gpu_info = output(device_count)
    return [gpu_info]

