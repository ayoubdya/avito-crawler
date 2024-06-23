from datetime import timedelta

DEBUG = 1
nextButtonXPath = "/html/body/div/div/main/div/div[5]/div[1]/div/div[2]/div/a[last()]"
numberOfPagesButtonSelector = "html > body > div > div > main > div > div:nth-child(5) > div:nth-child(1) > div > div:nth-child(2) > div > a:nth-last-child(2)"
priceSelector = "a > div:last-child > div:last-child > div > div > p > span > span:nth-child(1)"
titleSelector = "a > div:last-child > div:nth-child(1) > p"
city_categorySelector = "a > div:last-child > div:nth-child(1) > div > div > p"
durationSelector = "a > div:first-child > div > div:nth-child(2) > div:last-child > p"
storeSelector = "a > div:nth-child(2) > div > div:last-child > span:nth-child(2)"
imageUrlSelector = "a > div:nth-child(2) > div > div:nth-child(2) > img"
# isDeliverySelector = "div:nth-child(1) > div:nth-child(1) >  div:nth-child(2) > span"

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
