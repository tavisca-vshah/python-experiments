import requests
savedTranslation = ['4wopow6bses', '4wopow5s4gk', '4wopow55ndg', '4wopoj1qhzo', '4wopoj117ro', '4wopoj0eqok', '4wopoizh11w', '4wopo62rhck', '4wopo61o5g4', '4wopo60f79w', '4wopo5z693o', '4wopo5y2x78', '4wopntk0syc', '4wopntjebv8', '4wopnthu55g', '4wopntgo044', '4wopntfhv2s', '4wopnfyt4lw', '4wopnfx8xw4', '4wopnfx64r8', '4wopnfwguj8', '4wopnfwe1ec', '4wopn2qs87o', '4wopn2p58d0', '4wopn2owsyc', '4wopn2nth1w', '4wopn2mnc0k', '4wopmlawdjo', '4wopml9vus4', '4wopml8sivo', '4wopml7s044', '4wopm7yqkyc', '4wopm7x97dg', '4wopm7uzqfo', '4wopm7tz7o4', '4wopls6v3pw', '4wopls5ax04', '4wopls4ae8k', '4wopls20xas', '4wopls1shw4']
toSaveTranslationId =  ['4wopow6bses', '4wopow5s4gk', '4wopow5gvx0', '4wopow5b9n8', '4wopow55ndg', '4wopoj3rjis', '4wopoj1qhzo', '4wopoj117ro', '4wopoj0eqok', '4wopoizh11w', '4wopo62rhck', '4wopo61o5g4', '4wopo60f79w', '4wopo5z693o', '4wopo5y2x78', '4wopntk0syc', '4wopntjebv8', '4wopnthu55g', '4wopntgo044', '4wopntfhv2s', '4wopnfyt4lw', '4wopnfx8xw4', '4wopnfx64r8', '4wopnfwguj8', '4wopnfwe1ec', '4wopn2qs87o', '4wopn2p58d0', '4wopn2owsyc', '4wopn2nth1w', '4wopn2mnc0k', '4wopmlc5bpw', '4wopmlawdjo', '4wopml9vus4', '4wopml8sivo', '4wopml7s044', '4wopm7yqkyc', '4wopm7x97dg', '4wopm7w32c4', '4wopm7uzqfo', '4wopm7tz7o4', '4wopls6v3pw', '4wopls5ax04', '4wopls4ae8k', '4wopls20xas', '4wopls1shw4']
headers = {"oski-appName": "translation_service", "oski-tenantId": "demo"}

setSavedTranslation  = set(savedTranslation)
setToSavedTranslation = set(toSaveTranslationId)
diff = setToSavedTranslation - setSavedTranslation
print(len(diff))
lists = list(diff)
print(lists)
# print(len(set(toSaveTranslationId)))

# # for record in toSaveTranslationId:
# #     getTranslationUrl = f"https://private-data.qa.oski.io/api/v1.0/data/translation/{record}"
# #     res = requests.get(getTranslationUrl, headers=headers)
# #     data = res.json()
# #     print(data["key"])

# # check each translation is linked to scope or not

# for record in toSaveTranslationId:
#     getTranslationUrl = f"https://private-data.qa.oski.io/api/v1.0/data/translation/{record}/scopeTranslationMapping"
#     res = requests.get(getTranslationUrl, headers=headers)
#     data = res.json()
#     scopeName = data["result"][0]["name"]
#     print(scopeName,record)



