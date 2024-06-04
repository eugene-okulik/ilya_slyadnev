import requests
import datetime


times = []
for _ in range(10):
    start = datetime.datetime.now()
    response = requests.get('https://gotiny.cc/api/y68hxc')
    end = datetime.datetime.now()
    times.append((end - start).microseconds)
    print(end - start)
print(sum(times) / len(times))
