from datetime import timedelta

DEBUG = 1
nextButtonXPath = "/html/body/div[1]/div/main/div/div[6]/div[1]/div/div[3]/div/a[last()]"
citySelector = "div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)"
categorySelector = "div:nth-child(2) > div:nth-child(2) > p:nth-child(1)"
durationSelector = "div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)"
priceSelector = "div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)"

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
