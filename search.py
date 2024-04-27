import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


data = input("Enter the product : ")
amazon_url = f"https://www.amazon.in/s?k={data}"
amazon_page = urlopen(amazon_url)
urlclient = amazon_page.read()
amazon_html = BeautifulSoup(urlclient,"html.parser")
amazon_product = amazon_html.find_all("div",{"class" : "sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"})

for product in amazon_product :   
    print(amazon_url + product.a['href'])