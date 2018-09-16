import requests

url = 'http://localhost:5000/climb/api'

my_file = open('../TestImages/rockWall.jpg', 'rb')

files = {'image': my_file}

response = requests.post(url, files=files)
