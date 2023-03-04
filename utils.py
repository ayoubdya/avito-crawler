from bs4 import BeautifulSoup as bs
from datetime import datetime
from constants import *


def parseData(html):
  soup = bs(html, "html.parser")
  countainer = soup.find("div", {"class": "listing"})
  items = countainer.find_all("a")

  pageData = []
  for item in items:
    map = {}
    map["title"] = item.find("h3").text
    map["url"] = item.get("href")
    priceSpan = item.select_one(priceSelector)
    try:
      price = priceSpan.find("span").text
      map["price"] = float(price.replace(',', ''))
    except AttributeError:
      map["price"] = None
    map["city"] = item.select_one(citySelector).text
    map["categoty"] = item.select_one(categorySelector).text
    map["duration"] = item.select_one(durationSelector).text.replace("il y a ", "")
    map["postDate"] = parseDuration(map["duration"])
    imageUrl = item.find("img").get("src")
    map["imageUrl"] = imageUrl if imageUrl.startswith("http") else None
    map["isDelivery"] = True if item.parent.find("svg", {"aria-labelledby": "Store2FillTitleID"}) else False
    print(map) if DEBUG >= 2 else None
    pageData.append(map)
  return pageData


def parseDuration(duration):
  duration = duration.split(" ")
  delta = int(duration[0]) * units[duration[1]]
  postDate = datetime.now() - delta
  return postDate.strftime("%d/%m/%Y")
