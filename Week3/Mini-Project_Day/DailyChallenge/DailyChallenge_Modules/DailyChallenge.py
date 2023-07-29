import requests
from time import time


def open_web_speed(url):
    start_time = time()
    response = requests.get(url)
    end_time = time()
    seconds = round(end_time - start_time,3)
    return seconds


print(open_web_speed("https://www.google.com"))