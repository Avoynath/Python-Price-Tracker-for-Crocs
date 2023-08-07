import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.flipkart.com/crocs-men-black-clogs/p/itm9ed8a91daa761?pid=SNDFUDTDUPMUZHNQ&lid=LSTSNDFUDTDUPMUZHNQNPILK7&marketplace=FLIPKART&sattr[]=color&st=color'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    spans = soup.find_all('span', {'class': 'B_NuCI'})

    price = soup.find("div", class_="_30jeq3 _16Jk6d")



    price = price.text[1:6]
    price_without_comma = price.replace(",","")
    price_int = int(price_without_comma)
    if(price_int > 1500):
        send_mail()



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('avoynath2005@gmail.com', 'wwokebbbwwsfpoxd')

    subject = 'Price Dropped!!!'
    body = 'Click here: https://www.flipkart.com/crocs-men-black-clogs/p/itm9ed8a91daa761?pid=SNDFUDTDUPMUZHNQ&lid=LSTSNDFUDTDUPMUZHNQNPILK7&marketplace=FLIPKART&sattr[]=color&st=color'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'avoynathbdmi@gmail.com',
        'avoynath2005@gmail.com',
        msg
    )
    print('Email has been delivered')
    server.quit()


while(True):
    check_price()
    time.sleep(60*60)



