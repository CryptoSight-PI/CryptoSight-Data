import psutil
import time
from datetime import datetime
from getmac import get_mac_address
try:
    import pynvml
except ImportError:
    pynvml = None
import csv

# discretizar com array de valores e validação de percentual de alteração

def capture(components):
    user = get_mac_address()
    
    for i in range(5):
        cpu_percent = psutil.cpu_percent(interval=1) if components[0] == 1 else None
        cpu_frequency = round(((psutil.cpu_freq().current) / 1000), 2) if components[1] == 1 else None

        ram_percent = psutil.virtual_memory().percent if components[2] == 1 else None

        swap_memory_total = round((psutil.swap_memory().total) / (1024 ** 3), 2) if components[3] == 1 else None
        swap_memory_used = round((psutil.swap_memory().used) / (1024 ** 3), 2) if components[4] == 1 else None
        swap_memory_percent = round(psutil.swap_memory().percent, 2) if components[5] == 1 else None

        if components[6] == 1:
            try:
                upload_speed = round(((psutil.net_io_counters().bytes_sent) / 1000000000), 2)
            except Exception:
                upload_speed = 0.0
        else:
            upload_speed = None

        if components[7] == 1:
            try:
                download_speed = round(((psutil.net_io_counters().bytes_recv) / 1000000000), 2)
            except Exception:
                download_speed = 0.0
        else:
            download_speed = None

        if components[8] == 1:
            try:
                temperature = psutil.sensors_temperatures()
            except Exception:
                temperature = 0.0
        else:
            temperature = None

        if components[9] == 1:
            try:
                fans_speed = psutil.sensors_fans()
            except Exception:
                fans_speed = 0.0
        else:
            fans_speed = None

        disk = round(((psutil.disk_usage('/').free) / (1024 ** 3)), 2) if components[10] == 1 else None

        if components[11] == 1:
            try: 
                pynvml.nvmlInit()
                deviceCount = pynvml.nvmlDeviceGetCount()
                for j in range(deviceCount):
                    handle = pynvml.nvmlDeviceGetHandleByIndex(j)
                    info = pynvml.nvmlDeviceGetMemoryInfo(handle)

                    gpu_usage = round(((info.used * 100) / info.total), 2)

                pynvml.nvmlShutdown()
            except Exception:
                gpu_usage = 0.0
        else:
            gpu_usage = None

        if components[12] == 1:
            try:
                pynvml.nvmlInit()
                deviceCount = pynvml.nvmlDeviceGetCount()

                handle = pynvml.nvmlDeviceGetHandleByIndex(0)
                power_mw = pynvml.nvmlDeviceGetPowerUsage(handle)
                gpu_energy = round((power_mw / 1000.0), 2)

                pynvml.nvmlShutdown()
            except Exception:
                gpu_energy = 0.0
        else:
            gpu_energy = None

        timestamp = datetime.now()

        exhibit([user, cpu_percent, cpu_frequency, ram_percent, swap_memory_total, swap_memory_used, swap_memory_percent, upload_speed, download_speed, temperature, fans_speed, disk, gpu_usage, gpu_energy, timestamp])
        store([user, cpu_percent, cpu_frequency, ram_percent, swap_memory_total, swap_memory_used, swap_memory_percent, upload_speed, download_speed, temperature, fans_speed, disk, gpu_usage, gpu_energy, timestamp])

        time.sleep(9)

def exhibit(data):
    line_user = f"Endereço MAC do dispositivo: {data[0]}"
    line_cpu_percent  = f"Uso atual da CPU: {data[1]}%"
    line_cpu_frequency  = f"Frequência atual da CPU: {data[2]} GHz"
    line_ram_percent  = f"Uso atual de memória RAM: {data[3]}%"
    line_swap_memory_total = f"Total de memória swap: {data[4]} GiB"
    line_swap_memory_used = f"Total de memória swap usada: {data[5]} GiB"
    line_swap_memory_percent = f"Uso atual da memória swap: {data[6]}%"
    line_upload_speed = f"Velocidade atual de upload da rede: {data[7]} Mbps"
    line_download_speed = f"Velocidade atual de download da rede: {data[8]} Mbps"
    line_temperature = f"Temperatura atual: {data[9]} graus Celsius"
    line_fans_speed = f"Velocidade atual das ventoinhas: {data[10]} RPM"
    line_disk = f"Espaço livre em disco: {data[11]} GiB"
    line_gpu_usage = f"Uso atual da GPU: {data[12]}%"
    line_gpu_energy = f"Consumo atual de energia elétrica pela GPU: {data[13]} W"
    line_timestamp = f"Momento de captura: {data[14].strftime('%Y-%m-%d %H:%M:%S')}"

    print(f"""
    ----------------------------------------------------------------
    | {line_user:<60} |
    | {line_cpu_percent:<60} |
    | {line_cpu_frequency:<60} |
    | {line_ram_percent:<60} |
    | {line_swap_memory_total:<60} |
    | {line_swap_memory_used:<60} |
    | {line_swap_memory_percent:<60} |
    | {line_upload_speed:<60} |
    | {line_download_speed:<60} |
    | {line_temperature:<60} |
    | {line_fans_speed:<60} |
    | {line_disk:<60} |
    | {line_gpu_usage:<60} |
    | {line_gpu_energy:<60} |
    | {line_timestamp:<60} |
    ----------------------------------------------------------------
    """)

def store(data):
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14]])

with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(["user", "cpu_percent", "cpu_frequency", "ram_percent", "swap_memory_total", "swap_memory_used", "swap_memory_percent", "upload_speed", "download_speed", "temperature", "fans_speed", "disk", "gpu_usage", "gpu_energy", "timestamp"])

capture([1,0,1,0,0,1,1,1,1,1,1,1,1])