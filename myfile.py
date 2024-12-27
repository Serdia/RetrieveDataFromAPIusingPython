# activate .venv: & "C:\Users\Oleg Serdyuk\Documents\GIT\.venv\Scripts\Activate.ps1"
import requests
data = requests.get('https://data.snb.ch/api/cube/amarbma/data/csv/en').text

# list that have 3 parts:
data_text = str(data).splitlines()[-6].split(';') # ['"2024-11"', '"T1"', '"2.63448285"']
# extract third part of the list:
rate = float(data_text[2].replace('"', '')) # 2.63448285
print(f'unemployment rate: {rate}')
