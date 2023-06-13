from datetime import timedelta

DEBUG = 1
nextButtonXPath = "/html/body/div[1]/div/main/div/div[6]/div[1]/div/div[3]/div/a[last()]"
numberOfPagesButtonSelector = "html > body > div > div > main > div > div:nth-of-type(6) > div:first-of-type > div > div:nth-of-type(3) > div > a:nth-last-child(2)"
citySelector = "div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)"
categorySelector = "div:nth-child(2) > div:nth-child(2) > p:nth-child(1)"
durationSelector = "div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)"
priceSelector = "div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)"
storeSelector = "div:nth-last-child(2) > div > div[style*='width:19px;height:19px;background-color:rgba(242, 242, 242,0.2);border-radius:50px']"  # this one was pain in the ass
isDeliverySelector = "div:nth-child(1) > div:nth-child(3) > span"

units = {
  "seconde": timedelta(seconds=1),
  "secondes": timedelta(seconds=1),
  "minute": timedelta(minutes=1),
  "minutes": timedelta(minutes=1),
  "heure": timedelta(hours=1),
  "heures": timedelta(hours=1),
  "jour": timedelta(days=1),
  "jours": timedelta(days=1),
  "semaine": timedelta(weeks=1),
  "semaines": timedelta(weeks=1),
  "mois": timedelta(days=30),
  "an": timedelta(days=365),
  "ans": timedelta(days=365),
}

headers = {
    'authority': 'www.avito.ma',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-GB,en;q=0.6',
    # 'cookie': 'lang=fr; default_ca=5; d_mode=grid; visitedAds=52074396,50682059,50479262,49387285,52258444,52387878,51805533,52093543,52297602; xsq=o=1&q=iphone+6&w=3&extend=1&cg=5000&c=5000&st=s&reg=12; sq=o=1&q=iphone+6&w=3&extend=1&cg=5000&c=5000&st=s&reg=12; friendlyUrlSQ=/fr/rabat/informatique_et_multimedia/iphone_6--%C3%A0_vendre',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Brave";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}
