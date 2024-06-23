from bs4 import BeautifulSoup as bs
from datetime import datetime
import requests
from constants import *


def parseData(html):
  soup = bs(html, "html.parser")
  countainer = soup.find("div", {"class": "listing"})
  items = countainer.find_all("a")  # type: ignore

  pageData = []
  for item in items:
    map = {}
    map["title"] = item.select_one(titleSelector).text
    map["url"] = item.get("href")
    price = item.select_one(priceSelector)
    map["price"] = float(price.text.replace(',', '')) if price else None
    city_category = item.select_one(
        city_categorySelector).text.split(" dans ")
    map["categoty"] = city_category[0]
    map["city"] = city_category[1]
    map["duration"] = item.select_one(
        durationSelector).text.replace("il y a ", "")
    map["postDate"] = parseDuration(map["duration"])
    imageUrl = item.select_one(imageUrlSelector).get("src")
    map["imageUrl"] = imageUrl if imageUrl.startswith("http") else None
    # map["store"] = True if item.parent.find("svg", {"aria-labelledby": "Store2FillTitleID"}) else False
    map["store"] = True if item.select_one(storeSelector) else False
    # map["isDelivery"] = True if item.find("svg", {"aria-labelledby": "Delivery2TitleID"}) else False
    # map["isDelivery"] = True if item.select_one(
    #     isDeliverySelector) else False
    map["isDelivery"] = False
    print(map) if DEBUG >= 2 else None
    pageData.append(map)
  return pageData


def parseDuration(duration):
  duration = duration.split(" ")
  delta = int(duration[0]) * units[duration[1]]
  postDate = datetime.now() - delta
  return postDate.strftime("%d/%m/%Y")


def getHtml(url):
  response = requests.get(url, headers=headers)
  return response.text


def getNumberOfPages(html):
  soup = bs(html, "html.parser")
  ret = soup.select_one(numberOfPagesButtonSelector)
  numberOfPages = int(ret.text) if ret else 1
  return numberOfPages
