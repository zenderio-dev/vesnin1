import requests
from datetime import datetime, timedelta


days = 1

while True:
    yesterday = datetime.now()-timedelta(days)

    date = yesterday.strftime("%Y-%m-%d")
    url = f"https://simurg.space/gen_file?data=obs&date={date}"
    response = requests.get(url=url, stream=True)
    print(response)
    print("status =" , response.status_code)
    if response.status_code ==200:
        print(f"Data are avaible for {yesterday}")
        break
    else:
        print("faild")

    days+=1