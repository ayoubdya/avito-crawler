import pandas as pd
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from constants import DEBUG, nextButtonXPath
from utils import parseData


class Crawler():
  def __init__(self, url, headless=True):
    self.url = url
    self.options = Options()
    self.options.add_argument('-headless') if headless else None
    # self.browser.get(url)
    self.data = []

  def crawl(self):
    self.browser = Firefox(options=self.options, executable_path="./geckodriver")
    self.browser.get(self.url)
    page = 1
    while True:
      html = self.browser.page_source
      currentData = parseData(html)
      print(len(currentData), f"items in page {page}") if DEBUG >= 1 else None
      self.data.extend(currentData)
      try:
        next = self.browser.find_element(By.XPATH, nextButtonXPath)
      except NoSuchElementException:
        break
      print("self.browser.current_url", self.browser.current_url, "next.get_attribute('href')", next.get_attribute("href")) if DEBUG >= 2 else None
      if self.browser.current_url == next.get_attribute("href"):
        break
      next.click()
      page += 1
    self.browser.close()

  def saveData(self, filename):
    df = pd.DataFrame(self.data)
    df.to_csv(f'CSVs/{filename}.csv', header=True, index=False)
    print("Data saved successfully") if DEBUG >= 1 else None


if __name__ == "__main__":
  url = input("Enter avito url: ")
  crawler = Crawler(url)
  crawler.crawl()
  filename = input("Enter csv filename: ")
  crawler.saveData(filename)
