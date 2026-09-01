import glob
import pandas as pd

file_paths = glob.glob("./data/*.csv")

df = pd.concat(([pd.read_csv(file, sep=',') for file in file_paths]), ignore_index=True)

print(df)

media_ram = round(df["ram"].mean(), 2)
pico_cpu = df["cpu"].max()
media_disco = round(df["disk"].mean(), 2)

print(f"Uso médio de RAM na última hora: {media_ram}")
print(f"Pico de uso de CPU: {pico_cpu}")
print(f"Média de disco disponível: {media_disco}")