import requests
from fhirclient import client
from fhirclient.models import bundle, observation, patient, fhirreference, fhirdate, quantity, coding, codeableconcept
from fhirclient.models.bundle import BundleEntry
import orjson
import uuid


# def JsonConventer(dict_data):
#     print(orjson.dumps(dict_data, option=orjson.OPT_INDENT_2).decode("utf-8"))


settings = {
    'app_id': 'FHIRConverter',
    'api_base': 'http://fhirserver.ndmctsgh.edu.tw:18080/fhir'
}

fhirClient = client.FHIRClient(settings=settings)

obsBloodGlucose = observation.Observation({
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-laboratoryResult-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>檢驗檢查資料</b></h3></div>"
    },
    "status": "final",
    "category": [{
        "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
            "code": "laboratory",
            "display": "Laboratory"
        }]
    }],
    "code": {
        "coding": [{
            "system": "http://loinc.org",
            "code": "2339-0",
            "display": "Glucose [Mass/volume] in Blood"
        }],
        "text": "Glucose [Mass/volume] in Blood"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 95,
        "unit": "mg/dL"
    }
})

obsS1_bloodGlucosePerMeal = observation.Observation({
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-laboratoryResult-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>檢驗檢查資料</b></h3></div>"
    },
    "status": "final",
    "category": [{
        "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
            "code": "laboratory",
            "display": "Laboratory"
        }]
    }],
    "code": {
        "coding": [{
            "system": "http://loinc.org",
            "code": "88365-2",
            "display": "Glucose [Mass/volume] in Blood --pre-meal"
        }],
        "text": "Glucose [Mass/volume] in Blood --pre-meal"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 85,
        "unit": "mg/dL"
    }
})

bodyFatPercentage = observation.Observation({
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-vitalSigns-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>Observation Vital-sign 體脂率資料</b></h3></div>"
    },
    "status": "final",
    "category": [{
        "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
            "code": "vital-signs",
            "display": "Vital Signs"
        }]
    }],
    "code": {
        "coding": [{
            "system": "http://loinc.org",
            "code": "41982-0",
            "display": "Percentage of body fat Measured"
        }],
        "text": "Percentage of body fat Measured"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 10,
        "unit": "%"
    }
})

ptHeight = observation.Observation({
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-vitalSigns-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>Observation vital-sign 身高資料</b></h3></div>"
    },
    "status": "final",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "vital-signs",
                    "display": "Vital Signs"
                }
            ]
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "8302-2",
                "display": "Body height"
            }
        ],
        "text": "Body Height"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [
        {
            "reference": "Practitioner/103"
        }
    ],
    "valueQuantity": {
        "value": 180,
        "unit": "cm"
    }
})

ptTemp = observation.Observation({
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-vitalSigns-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>Observation Vital-sign 體溫資料</b></h3></div>"
    },
    "status": "final",
    "category": [{
        "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
            "code": "vital-signs",
            "display": "Vital Signs"
        }]
    }],
    "code": {
        "coding": [
            # 體溫 LOINC 8310-5
            {
                "system": "http://loinc.org",
                "code": "8310-5",
                "display": "Body Temperature"
            }
        ],
        "text": "Body Temperature"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [
        {
            "reference": "Practitioner/103"
        }
    ],
    "valueQuantity": {
        "value": 38.8,
        "unit": "Cel"
    }
})

ptWeight = observation.Observation({
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-vitalSigns-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>Observation Vital-sign 體重資料</b></h3></div>"
    },
    "status": "final",
    "category": [{
        "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
            "code": "vital-signs",
            "display": "Vital Signs"
        }]
    }],
    "code": {
        "coding": [
            # 體重 LOINC 29463-7
            {
                "system": "http://loinc.org",
                "code": "29463-7",
                "display": "Body Weight"
            }
        ],
        "text": "Body Weight"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [
        {
            "reference": "Practitioner/103"
        }
    ],
    "valueQuantity": {
        "value": 70.5,
        "unit": "kg"
    }
})

obsBundle = bundle.Bundle()
obsBundle.type = 'transaction'

listObs = [obsBloodGlucose, obsS1_bloodGlucosePerMeal, bodyFatPercentage, ptHeight, ptTemp, ptWeight]
listObsEntries = [BundleEntry() for ob in listObs]

# 使用 zip 將兩個列表配對並賦值
for be, ob in zip(listObsEntries, listObs):
    be.resource = ob

obsBundle.entry = listObsEntries

for entry in obsBundle.entry:
    # 這裡一定要設，每個 resource 根據自己的類別路徑設定，格式是 resourceType/uuid
    entry.fullUrl = f'Observation/{uuid.uuid4()}'
    entry.request = bundle.BundleEntryRequest()
    # request 也要設。這裡剛好都是新建。
    entry.request.method = "POST"
    entry.request.url = "Observation"

# # 發送 Bundle 到服務器
# response = fhirClient.server.post_json('/', obsBundle.as_json())
# print(response.status_code)
# print(response.content.decode("utf-8"))

# 用 requests 發 bundle
url = f'{settings['api_base']}/'
headers = {"Content-Type": "application/fhir+json",
           # 'Authorization': f'Bearer {sJWT}'
           }

response = requests.post(url, data=orjson.dumps(obsBundle.as_json()), headers=headers)
print(response.status_code)
print(response.json())

# pt_data = {
#     "resourceType": "Patient",
#     "id": "pat-residentNumber-example",
#     "meta": {
#         "profile": ["https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Patient-twcore"]
#     },
#     "text": {
#         "status": "generated",
#         "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>病人基本資料-居留證號碼</b></h3><blockquote><p><b>識別碼型別</b>：Permanent Resident Card Number <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\">（ <a href=\"http://terminology.hl7.org/CodeSystem/v2-0203\">Identifier Type Codes</a>#PRC）</span><br/><b>身分證字號（official）</b>：Z596839485 （http://www.immigration.gov.tw）</p></blockquote><blockquote><p><b>識別碼型別</b>：Medical record number <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\">（ <a href=\"http://terminology.hl7.org/CodeSystem/v2-0203\">Identifier Type Codes</a>#MR）</span><br/><b>病歷號（official）</b>：4958603 （https://www.tph.mohw.gov.tw）</p></blockquote><p><b>病人的紀錄（active）</b>：使用中</p><p><b>姓名（official）</b>：陳曉明 Chan, Xiao Ming</p><p><b>性別</b>：男性</p><p><b>出生日期</b>：1999-04-20</p><p><b>聯絡方式</b>：Phone <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\">（ <a href=\"https://hl7.org/fhir/R4/valueset-contact-point-system.html\">ContactPointSystem</a>#phone）</span><br/><b>聯絡電話</b>：（Mobile）0939405869 <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\">（ <a href=\"https://build.fhir.org/codesystem-contact-point-use.html\">ContactPointUse</a>#mobile）</span><br/><b>聯絡電話使用效期</b>：2023-01-01至2026-01-01</p></div>"
#     },
#     "identifier": [{
#         "use": "official",
#         "type": {
#             "coding": [{
#                 "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
#                 "code": "PRC"
#             }]
#         },
#         "system": "http://www.immigration.gov.tw",
#         "value": "Z596839485"
#     },
#         {
#             "use": "official",
#             "type": {
#                 "coding": [{
#                     "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
#                     "code": "MR"
#                 }]
#             },
#             "system": "https://www.tph.mohw.gov.tw",
#             "value": "4958603"
#         }],
#     "active": True,
#     "name": [{
#         "use": "official",
#         "text": "陳曉明",
#         "family": "Chen",
#         "given": ["Xiao Ming"]
#     }],
#     "telecom": [{
#         "system": "phone",
#         "value": "0939405869",
#         "use": "mobile",
#         "period": {
#             "start": "2023-01-01",
#             "end": "2026-01-01"
#         }
#     }],
#     "gender": "male",
#     "birthDate": "1999-04-20"
# }
# 
# ptResource = patient.Patient(pt_data)
# respPt = fhirClient.server.post_json('Patient', ptResource.as_json())
# print(respPt)
