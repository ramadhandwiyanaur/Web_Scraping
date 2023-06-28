import requests
import csv

# key = input('masukkan keyword :')
# write = csv.writer(open('hasil/{}.csv'.format(key), 'w', newline=''))
# header = ['Nama', 'Harga', 'Stok']
# write.writerow(header)

url = 'https://api.bukalapak.com/multistrategy-products'
count =0
for page in range(1000):
    parameter = {
    'prambanan_override': True,
    # 'keywords': key,
    'limit': 50,
    'offset': 50,
    'page': page,
    'facet': True,
    'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImFjY291bnRzLmp3dC5hY2Nlc3MtdG9rZW4iLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmJ1a2FsYXBhay5jb20vIiwic3ViIjoiNzEyMTM2NyIsImF1ZCI6WyJodHRwczovL2FjY291bnRzLmJ1a2FsYXBhay5jb20iLCJodHRwczovL2FwaS5idWthbGFwYWsuY29tIiwiaHR0cHM6Ly9hcGkuc2VydmVybWl0cmEuY29tIl0sImV4cCI6MTY4Nzg2MzY2NSwibmJmIjoxNjg3ODU0ODQ1LCJpYXQiOjE2ODc4NTQ4NDUsImp0aSI6InB5UGk2WjJxSU52MFF3MzdVZkY0LWciLCJjbGllbnRfaWQiOiI5OTM5YjgxYTViYmJiM2ExM2Y3NDM0YTEiLCJzY29wZSI6InB1YmxpYyB1c2VyIHN0b3JlIn0.hxbGYh8joOi9PDlz_nldDlI3dVdjuyd32-ochCYOa8FcJaULdrSEU6VdXXLDX_Z9wLCbtWE7LKReZkHdRshNv3e5D_e9LL11PQzOs3nQZtoGZKNN2b6khrmvz2qBJVMNut6fCZcPzzKk5B2E_5izhkwjBfoJ4M2Usb5wi7aEFrk5W9aeD53YOZWX8zQneEN74-8imQ-j9YqT87gfHGE4VVRyKq1iTUBo7vN8DagCiv5spTuMl_6DfHq8_B_s5sMHmDT-5lG5LKhJ1XC8JayZ_GGgdiKtphO4ZAsHYvACWl46zlf3msq9o594-FvtLk6R1Ezh-5BVb0JeKKj5rIl1UA'
    }

    r = requests.get(url, params=parameter).json()

    products = r['data']
    for p in products:
        print (p)
        # nama = p['name']
        # harga = p['price']
        # stok = p['stock']
        # count+=1
        # print('No :',count, 'nama :',nama, 'harga :',harga, 'stok :', stok)
        # write = csv.writer(open('hasil/{}.csv'.format(key), 'a',newline=''))
        # data = [nama, harga, stok]
        # write.writerow(data)