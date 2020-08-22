import requests
from tqdm import tqdm

getTranslationUrl = "https://private-data.qa.oski.io/api/v1.0/data/translation?pageSize=100"
headers = {"oski-appName": "translation_service", "oski-tenantId": "demo"}

res = requests.get(getTranslationUrl, headers=headers)
data = res.json()
translations = data["result"]

print(len(translations))
for translation in translations:
        translationId = translation["__id"]
        print(translationId)
        print("deleting...")
        deleteUrl = f"https://private-data.qa.oski.io//api/v1.0/data/translation/{translationId}?deletelinks=true"
        res = requests.delete(deleteUrl, headers=headers)
        print(res)

# idList = []
# for translation in translations:
#     translationId = translation["__id"]
#     # getTranslationUrl = f"https://private-data.qa.oski.io/api/v1.0/data/translation/{translationId}/scopeTranslationMapping"
#     # res = requests.get(getTranslationUrl, headers=headers)
#     # data = res.json()
#     # scopeName = data["result"][0]["name"]
#     # print(scopeName,translationId)
#     idList.append(translationId)

# print(idList)
    