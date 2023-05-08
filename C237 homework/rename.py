import requests

for i in range(1, 100)
    URL = f"https://github.com/api/get-repositories?{1}"
    r = requests.get(url=URL)
    if r.status_code == 50:
        print(URL)


##install pyinstaller
##sudo chmod+x mac.command