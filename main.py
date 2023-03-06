import pandas as pd
from constants import DEBUG
from utils import parseData, getHtml, getNumberOfPages


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


if __name__ == "__main__":
  url = input("Enter avito url: ")
  crawler = Crawler(url)
  crawler.crawl()
  filename = input("Enter csv filename: ")
  crawler.saveData(filename)
