import requests
from random import choice

print ("by dark zone ")
print ("MAFIA SCRIPT")

r = open('dark.txt','w',encoding='utf-8')
r.close()
def check(email):
    url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
    data = ""
    header = {
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "odc.officeapps.live.com",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
        "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
        "uaid": "d06e1498e7ed4def9078bd46883f187b",
        "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
        }
    r = requests.get(url, data=data, headers=header)
    if r.text.find('MSAccount')>=0:
        print(f"[-] Taken >> {email}")
    else:
        print(f"[+] Available >> {email}")
        with open('dark.txt','a',encoding='utf-8') as file:
            file.write(mail+'\n')

letters = 'qwertyuioplkjhgfdsazxcvbnm1234567890'
mails = set()
for i in range(10000):
    mail = ''
    for _ in range(4):
        mail += choice(letters)
    domain = ['@hotmail.com','@outlook.com']
    mail += choice(domain)
    if mail[0].isalpha():
        mails.add(mail)
print('Done generating '+str(len(mails))+' mail!')
print('All available mails will be saved in dark.txt file\n')
input('Click enter to start checking!')
print('لك شددد يابة.. ')

for mail in list(mails):
    check(mail)
