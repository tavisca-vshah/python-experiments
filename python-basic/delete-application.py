import requests
from tqdm import tqdm

headers = {"oski-appName": "translation_service", "oski-tenantId": "demo"}
scopeUrl = "https://private-data.qa.oski.io/api/v1.0/data/application/4rsh9ok370t/applicationscopemapping?pageSize=101"
res = requests.get(scopeUrl, headers=headers)
data = res.json()
scopes = data["result"]

print(len(scopes))
for scope in scopes:
    scopeId = scope["__id"]
    deletescopeUrl = f"https://private-data.qa.oski.io/api/v1.0/data/scope/{scopeId}?deletelinks=true"

    scopeResponse = requests.delete(deletescopeUrl, headers=headers)
    print(scopeResponse)

