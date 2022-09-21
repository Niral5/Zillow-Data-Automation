from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

import json
import requests
from bs4 import BeautifulSoup

chrome_driver_path = "C:/Users/Niral Patel/Desktop/Code/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
form_link = "https://docs.google.com/forms/d/e/1FAIpQLSftClpicsg-u5xOfiTf36cw8ByEsM0vvOfhs4wKhBtiNYANNA/viewform"

url = "https://www.zillow.com/cherry-hill-township-nj/?searchQueryState={%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A39.96206851053258%2C%22east%22%3A-74.89621692517089%2C%22south%22%3A39.85145766424877%2C%22west%22%3A-75.0968890748291%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A37851%2C%22regionType%22%3A6%7D%5D%7D}"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
}

soup = BeautifulSoup(requests.get(url, headers=headers).content, "html.parser")

data = json.loads(
    soup.select_one("script[data-zrr-shared-data-key]")
        .contents[0]
        .strip("!<>-")
)


# uncomment this to print all data:
# print(json.dumps(data, indent=4))
def add_house(address, price, link):
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSftClpicsg-u5xOfiTf36cw8ByEsM0vvOfhs4wKhBtiNYANNA/viewform')
    address_form = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_form.click()
    address_form.send_keys(address)

    price_form = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_form.click()
    price_form.send_keys(price)

    link_form = driver.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_form.click()
    link_form.send_keys(link)

    submit_buttom = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_buttom.click()


for result in data["cat1"]["searchResults"]["listResults"]:
    print(result)
    add_house(result["address"], result["price"], result["detailUrl"])
