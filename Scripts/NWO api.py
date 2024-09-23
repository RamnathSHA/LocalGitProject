import requests as r
import urllib.parse
import json
import pandas as pd

## API adres
rio_api = 'https://nwopen-api.nwo.nl/NWOpen-API/api/Projects'

#rio_api = 'https://lod.onderwijsregistratie.nl/rio-api/api/v2'

## GET Request
result_api = r.get(rio_api)    #change based on API adress

print(result_api.text)



