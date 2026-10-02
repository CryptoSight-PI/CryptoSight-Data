import psutil

import psutil

def get_fan_speeds():
    if not hasattr(psutil, "sensors_fans"):
        return {}  

    result = {}
    for chip, fans in psutil.sensors_fans().items():
        for fan in fans:
            result[fan.label] = fan.current
    return result

speeds = get_fan_speeds()
print(speeds.get('cpu_fan')) 
print(speeds.get('gpu_fan'))
# print(psutil.sensors_temperatures())

import psutil

def get_cpu_gpu_temps():
    if not hasattr(psutil, "sensors_temperatures"):
        return None, None  

    temps = psutil.sensors_temperatures()

    cpu = None
    for chip in ('k10temp', 'coretemp', 'zenpower'):
        if chip in temps and temps[chip]:
            cpu = temps[chip][0].current
            break

    gpu = temps['amdgpu'][0].current if temps.get('amdgpu') else None

    return cpu, gpu

cpu, gpu = get_cpu_gpu_temps()
print(f"CPU: {cpu}°C | GPU: {gpu}°C")