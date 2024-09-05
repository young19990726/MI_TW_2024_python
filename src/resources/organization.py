import orjson
import requests

from utilities.python.forOauth import get_token

sApiUrl = 'http://172.18.0.53:10004/fhir/Organization'
sJWT = get_token()

organization = {
    "resourceType": "Organization",
    "id": "109",
    # "meta": {
    #     "profile": ["https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Organization-hosp-twcore"]
    # },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">台灣醫事機構基本資料</div>"
    },
    "identifier": [
        {
            "use": "official",
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": "PRN"
                    }
                ]
            },
            "system": "https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/organization-identifier-tw",
            "value": "0501110514"
        }
    ],
    "active": True,
    "type": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/organization-type",
                    "code": "prov",
                    "display": "Healthcare Provider"
                }
            ]
        }
    ],
    "name": "三軍總醫院",
    "alias": ["Tri-Service General Hospital", "三總"],
    "telecom": [
        {
            "system": "phone",
            "value": "02-87923311",
            "use": "work"
        },
        {
            "system": "fax",
            "value": "02-87923322",
            "use": "work"
        },
        {
            "system": "email",
            "value": "info@tsgh.ndmctsgh.edu.tw",
            "use": "work"
        }
    ],
    "address": [
        {
            "line": ["內湖區成功路二段325號"],
            "city": "台北市",
            "district": "內湖區",
            "state": "台灣",
            "postalCode": "114202",
            "country": "中華民國"
        }
    ],
    "contact": [
        {
            "purpose": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/contactentity-type",
                        "code": "ADMIN",
                        "display": "Administrative"
                    }
                ]
            },
            "name": {
                "family": "李",
                "given": ["大仁"]
            },
            "telecom": [
                {
                    "system": "phone",
                    "value": "02-87923311 ext.1234",
                    "use": "work"
                },
                {
                    "system": "email",
                    "value": "admin@tsgh.ndmctsgh.edu.tw",
                    "use": "work"
                }
            ],
            "address": {
                "line": ["內湖區成功路二段325號"],
                "city": "台北市",
                "district": "內湖區",
                "state": "台灣",
                "postalCode": "114202",
                "country": "中華民國"
            }
        }
    ]
}

organization_json = orjson.dumps(organization, option=orjson.OPT_INDENT_2)

# # 發送 POST 請求到 HAPI FHIR 伺服器
# url = f'{sApiUrl}'
# headers = {"Content-Type": "application/fhir+json",
#            'Authorization': f'Bearer {sJWT}'
#            }
# response = requests.post(url, data=organization_json, headers=headers)
#
# print(response.status_code)
# print(response.json())

# 發送 put 請求到 HAPI FHIR 伺服器
orgid = '109'
url = f'{sApiUrl}/{orgid}'
headers = {"Content-Type": "application/fhir+json",
           'Authorization': f'Bearer {sJWT}'
           }
response = requests.put(url, data=organization_json, headers=headers)

print(response.status_code)
print(response.json())
