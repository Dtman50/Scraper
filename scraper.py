import time
from bs4 import BeautifulSoup
import requests
import smtplib


def check_if_avail():
    html_text = requests.get('https://www.alloyapparel.com/products/tall-textured-faux-leather-jeans-black').text
    soup = BeautifulSoup(html_text, 'lxml')
    div = soup.find('div', class_='swatch-element short-label')
    size4 = div.find('input', id='swatch-2-4')
    size6 = div.find('input', id='swatch-2-6')

    if size4 is not None:
        send_mail()

    if size6 is not None:
        send_mail6()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('dariustaylor17@gmail.com', 'hgrrmragrplmtusu')

    subject = 'Size 4 is available'
    body = 'Go NOW! Link: https://www.alloyapparel.com/products/tall-textured-faux-leather-jeans-black'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'dariustaylor17@gmail.com',
        'dtman50@yahoo.com',
        msg
    )
    print('Email sent')
    server.quit()


def send_mail6():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('dariustaylor17@gmail.com', 'hgrrmragrplmtusu')

    subject = 'Size 6 is available'
    body = 'Go NOW! Link: https://www.alloyapparel.com/products/tall-textured-faux-leather-jeans-black'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'dariustaylor17@gmail.com',
        'dtman50@yahoo.com',
        msg
    )
    print('Email sent')
    server.quit()


if __name__ == '__main__':
    while True:
        check_if_avail()
        time_wait = 60
        print("Scraping... Refreshing after 10 minutes")
        time.sleep(time_wait * 10)
        