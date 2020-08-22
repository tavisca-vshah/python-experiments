import requests
import json

headers = {"oski-appName": "translation_service", "oski-tenantId": "demo"}
getTranslationUrl = "https://private-data.qa.oski.io/api/v1.0/data/translation?pageSize=100"

res = requests.get(getTranslationUrl, headers=headers)
data = res.json()
translations = data["result"]

keys = []
for translation in translations:
        translationKey = translation["key"]
        keys.append(translationKey)

getScopeUrl = "https://private-data.qa.oski.io/api/v1.0/data/scope/4uziyxgrggt/scopeTranslationMapping?pageSize=100"

scopeResponse = requests.get(getScopeUrl, headers=headers)
scopeData = scopeResponse.json()
scopeTranslations = scopeData["result"]

scopeKeys = []
for scopeTranslation in scopeTranslations:
        scopeTranslationKey = scopeTranslation["key"]
        # print(translationKey)
        scopeKeys.append(scopeTranslationKey)

setDiff = set(keys) -  set(scopeKeys)

print(setDiff)
