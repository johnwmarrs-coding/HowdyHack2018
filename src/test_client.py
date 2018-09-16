import requests

url = '10.230.212.179:5000/climb/api2/'

my_file = open('rockWall.jpg', 'rb')

files = {'image': my_file}

response = requests.post(url, files=files)
