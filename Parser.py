import shutil
import os

import requests

import image

from send_message_after_parser import send_auto_rasp
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def parse(html):
    soup = BeautifulSoup(html, features="html.parser")
    div = soup.find('div', id='blockSidebar')
    p_tag = div.find_all('p')[2]
    url = p_tag.find('a').get('href')
    if open('mrk.txt', 'r').read() == url:
        return
    with open('mrk.txt', 'w') as f:
        f.write(url)
    return url


def download_file(download_url):
    response = requests.get(download_url, stream = True)
    try:
        shutil.rmtree('rasp')
    except:
        pass
    os.mkdir('rasp')
    file = open("rasp/rasp.pdf", 'wb')
    file.write(response.content)
    file.close()
    print("Completed")


def main():
    url = parse(get_html('http://www.mrk-bsuir.by'))
    if url:
        download_file(url)
        image.main()
        send_auto_rasp()


if __name__ == '__main__':
    main()
