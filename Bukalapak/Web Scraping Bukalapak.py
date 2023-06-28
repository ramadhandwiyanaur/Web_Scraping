import requests
import csv

key = input('masukkan keyword :')
write = csv.writer(open('hasil/{}.csv'.format(key), 'w', newline=''))
header = ['Nama', 'Harga', 'Stok']
write.writerow(header)

url = 'https://api.bukalapak.com/multistrategy-products'
count =0
for page in range(1,11):
    parameter = {
    'prambanan_override': True,
    'keywords': key,
    'limit': 50,
    'offset': 50,
    'page': page,
    'facet': True,
    'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImFjY291bnRzLmp3dC5hY2Nlc3MtdG9rZW4iLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmJ1a2FsYXBhay5jb20vIiwic3ViIjoiNzEyMTM2NyIsImF1ZCI6WyJodHRwczovL2FjY291bnRzLmJ1a2FsYXBhay5jb20iLCJodHRwczovL2FwaS5idWthbGFwYWsuY29tIiwiaHR0cHM6Ly9hcGkuc2VydmVybWl0cmEuY29tIl0sImV4cCI6MTY4Nzg5MjA5NiwibmJmIjoxNjg3ODc5MzE2LCJpYXQiOjE2ODc4NzkzMTYsImp0aSI6IkhzUG9QdVh2LXE5OEdnYzZsTVZiMEEiLCJjbGllbnRfaWQiOiIyMzFkNGE4NjkwNWYwZjI2MmM1ZTAzZmMiLCJzY29wZSI6InB1YmxpYyB1c2VyIHN0b3JlIn0.wHmxhr3pLGGjCX3pWEwdPIFAoVWQlopcDrR4XEaE1MSOY3q8pgQyzSRNJeA70CA69MiqHl_bzxgjibymWDOVYeGQP_bsnXdtG_uKvn8pUTI7Bt_i1BbREbnwSeh_O-yOCueJN3fxWxW0Fg6bmlIHrWaazLZK1VggBnrjgEiILFEAl8WhA3PbNIGAJwvTjXJeftMZDUNQ7uGewjRjOPPHl4EeUtRmX_rzLzVJ0CPGH-9CXNbbEjXPHXUf0nD9uP2ZOkEcj5dusW3kb-i4rBazKJjZxlpgyAyEaVUnlBQrpLlps8woBji0GEOS8r9da1GeqqC-IVrpeNHblXBiVtLLBQ'
    }

    r = requests.get(url, params=parameter).json()

    products = r['data']
    for p in products:
        nama = p['name']
        harga = p['price']
        stok = p['stock']
        count+=1
        print('No :',count, 'nama :',nama, 'harga :',harga, 'stok :', stok)
        write = csv.writer(open('hasil/{}.csv'.format(key), 'a',newline=''))
        data = [nama, harga, stok]
        write.writerow(data)