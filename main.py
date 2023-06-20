import pandas as pd
from constants import DEBUG
import json
import time
from utils import parseData, getHtml, getNumberOfPages
from server import open_browser


class Crawler():
  def __init__(self, url):
    self.url = url
    self.data = []

  def crawl(self):
    html = getHtml(self.url)
    numberOfPages = getNumberOfPages(html)
    for page in range(1, numberOfPages + 1):
      html = getHtml(f"{self.url}?o={page}") if page > 1 else html
      currentData = parseData(html)
      print(len(currentData), f"items in page {page}") if DEBUG >= 1 else None
      self.data.extend(currentData)

  def saveData(self, filename):
    df = pd.DataFrame(self.data)
    df.to_csv(f'CSVs/{filename}.csv', index=False)
    print(f"Data saved successfully to CSVs/{filename}.csv")

  def saveDataAsJson(self):
    json_data = json.dumps(self.data, indent=2, ensure_ascii=False)
    with open('src/data.json', 'w') as f:
      f.write(json_data)


if __name__ == "__main__":
  url = input("Enter avito url: ")
  crawler = Crawler(url)
  crawler.crawl()
  isSave = input("Save as csv file [y]/n: ")
  if isSave.lower() != "n":
    filename = input("Enter csv filename: ")
    crawler.saveData(filename)

  isOpen = input("Open in browser [y]/n: ")
  if isOpen.lower() != "n":
    crawler.saveDataAsJson()
    time.sleep(1)
    open_browser()
