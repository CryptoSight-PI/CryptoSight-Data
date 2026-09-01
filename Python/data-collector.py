import psutil
import time
from datetime import datetime
from getmac import get_mac_address
try:
    import pynvml
except ImportError:
    pynvml = None
import csv

# o que capturamos agora: cpu_percent, memory_percent, disk_usage_free, gpu_usage
# o que podemos capturar também: cpu_freq, swap_memory, mac_address, net_if_stats.speed, sensors_temperatures, sensor_fans
# discretizar com array de valores e validação de percentual de alteração
# criar todas as colunas, mesmo com valores null

def exibir(gpu):
    print()

def capturar(componentes):
    with open('./data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')

        user = get_mac_address()

        for i in range(5):
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_frequency = psutil.cpu_freq()
            ram = psutil.virtual_memory().percent
            swap_memory_total = psutil.swap_memory().total
            swap_memory_used = psutil.swap_memory().used
            swap_memory_percent = psutil.swap_memory().percent
            
            disk = round(((psutil.disk_usage('/').free) / (1024 ** 3)), 2)
            timestamp = datetime.now()

            line_cpu  = f"Uso atual da CPU: {cpu}%"
            line_ram  = f"Uso atual de memória RAM: {ram}%"
            line_disk = f"Espaço livre em disco: {disk} GB"
            line_time = f"Momento de captura: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

            gpu = False

            try: 
                pynvml.nvmlInit()
                deviceCount = pynvml.nvmlDeviceGetCount()
                for j in range(deviceCount):
                    handle = pynvml.nvmlDeviceGetHandleByIndex(j)
                    # print(f"Device {i} : {pynvml.nvmlDeviceGetName(handle)}")
                    info = pynvml.nvmlDeviceGetMemoryInfo(handle)

                    gpu_usage = round(((info.used * 100) / info.total), 2)
                    line_gpu_usage = f"Uso atual da GPU: {gpu_usage}%"

                handle = pynvml.nvmlDeviceGetHandleByIndex(0)

                power_mw = pynvml.nvmlDeviceGetPowerUsage(handle)
                gpu_energy = round((power_mw / 1000.0), 2)
                line_gpu_energy = f"Consumo atual de Energia elétrica pela GPU: {gpu_energy} W"

                gpu = True
                pynvml.nvmlShutdown()
            except:
                ""

            if (gpu):
                print(f"""
                --------------------------------------------
                | {line_cpu:<60} |
                | {line_ram:<60} |
                | {line_disk:<60} |
                | {line_gpu_usage:<60} |
                | {line_gpu_energy:<60} |
                | {line_time:<60} |
                --------------------------------------------
                """)
                if (i == 0):
                    writer.writerow(['user', 'cpu', 'ram', 'disk', 'gpu_usage', 'gpu_energy', 'timestamp'])

                writer.writerow([user, cpu, ram, disk, gpu_usage, gpu_energy, timestamp])
            else:
                print(f"""
                --------------------------------------------
                | {line_cpu:<40} |
                | {line_ram:<40} |
                | {line_disk:<40} |
                | {line_time:<40} |
                --------------------------------------------
                """)
                if (i == 0):
                    writer.writerow(['user', 'cpu', 'ram', 'disk', 'timestamp'])
                writer.writerow([user, cpu, ram, disk, timestamp])
            
            time.sleep(9)