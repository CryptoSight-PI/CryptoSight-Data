import glob
import pandas as pd

file_paths = glob.glob("./data/*.csv")

df = pd.concat(([pd.read_csv(file, sep=';') for file in file_paths]), ignore_index=True)

media_cpu = round(df["cpu_percent"].mean(), 2)
pico_cpu = df["cpu_percent"].max()

media_gpu = round(df["gpu_usage"].mean(), 2)
pico_gpu = df["gpu_usage"].max()

media_consumo_gpu = round(df["gpu_energy"].mean(), 2)
pico_consumo_gpu = df["gpu_energy"].max()

media_ram = round(df["ram_percent"].mean(), 2)
pico_ram = df["ram_percent"].max()

menor_disco = df["disk"].min()

media_upload = round(df["upload_speed"].mean(), 2)
media_download = round(df["download_speed"].mean(), 2)
menor_upload = df["upload_speed"].min()
menor_download = df["download_speed"].min()

media_temperatura = round(df["temperature"].mean(), 2)
pico_temperatura = round(df["temperature"].max(), 2)

media_rpm = round(df["fans_speed"].mean(), 2)
pico_rpm = round(df["fans_speed"].max(), 2)

media_swap = round(df["swap_memory_percent"].mean(), 2)
pico_swap = round(df["swap_memory_percent"].max(), 2)

line_media_cpu = f"Média de uso da CPU: {media_cpu}%"
line_pico_cpu = f"Pico de uso da CPU: {pico_cpu}%"
line_media_gpu = f"Média de uso da CPU: {media_gpu}%"
line_pico_gpu = f"Pico de uso da GPU: {pico_gpu}%"
line_media_consumo_gpu = f"Média de comsumo de energia da CPU: {media_gpu} W"
line_pico_consumo_gpu = f"Pico de consumo de energia da GPU: {pico_gpu} W"
line_media_ram = f"Média de uso da memória RAM: {media_ram}%"
line_pico_ram = f"Pico de uso da memória RAM: {pico_ram}%"
line_menor_disco = f"Espaço mínimo em disco: {menor_disco} GiB"
line_media_upload = f"Média do tráfego de upload de bytes: {media_upload} Mbps"
line_menor_upload = f"Mínimo da tráfego de upload de bytes: {menor_upload} Mbps"
line_media_download = f"Média da tráfego de download de bytes: {media_download} Mbps"
line_menor_download = f"Mínimo da tráfego de download de bytes: {menor_download} Mbps"
line_media_temperatura = f"Média de temperatura dos componentes: {media_temperatura}%"
line_pico_temperatura = f"Pico de temperatura dos componentes: {pico_temperatura}%"
line_media_rpm = f"Média de rotações por minuto das ventoinhas: {media_cpu}"
line_pico_rom = f"Pico de rotações por minuto das ventoinhas: {pico_cpu}"
line_media_swap = f"Média de uso da memória SWAP: {media_gpu}%"
line_pico_swap = f"Pico de uso da memória SWAP: {pico_gpu}%"

print(f"""
    ----------------------------------------------------------------
    | {line_media_cpu:<60} |
    | {line_pico_cpu:<60} |
    | {line_media_gpu:<60} |
    | {line_pico_gpu:<60} |
    | {line_media_consumo_gpu:<60} |
    | {line_pico_consumo_gpu:<60} |
    | {line_media_ram:<60} |
    | {line_pico_ram:<60} |
    | {line_menor_disco:<60} |
    | {line_media_upload:<60} |
    | {line_menor_upload:<60} |
    | {line_media_download:<60} |
    | {line_menor_download:<60} |
    | {line_media_temperatura:<60} |
    | {line_pico_temperatura:<60} |
    | {line_media_rpm:<60} |
    | {line_pico_rom:<60} |
    | {line_media_swap:<60} |
    | {line_pico_swap:<60} |
    ----------------------------------------------------------------
""")