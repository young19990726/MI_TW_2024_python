import requests
from fhir.resources.servicerequest import ServiceRequest
import orjson


sApiUrl = 'http://fhirserver.ndmctsgh.edu.tw:18080/fhir/ServiceRequest'
sJWT = ''
# 建立 ServiceRequest 資源
service_request = {
    "resourceType": "ServiceRequest",
    "id": "114",
    "meta": {
        "versionId": "1",
        "lastUpdated": "2024-08-06T01:07:45.099+00:00",
        "source": "#U5Zf9g6CGV3vtx44"
    },
    "status": "active",
    "intent": "order",
    "category": [{
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "306170007",
            "display": "Referral to physiotherapy service (procedure)"
        }]
    }],
    "priority": "routine",
    "subject": {
        "reference": "Patient/108"
    },
    "encounter": {
        "reference": "Encounter/111"
    },
    "occurrenceDateTime": "2024-08-16",
    "authoredOn": "2024-08-05",
    "requester": {
        "reference": "Practitioner/103"
    },
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "reasonCode": [{
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "161891005",
            "display": "Backache"
        }]
    }],
    "bodySite": [{
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "122496007",
            "display": "Lumbar spine structure"
        }]
    }],
    "note": [{
        "text": "患者報告腰部疼痛持續兩週，建議進行物理治療評估和治療"
    }]
}

# 將 ServiceRequest 資源轉換為 JSON 格式
service_request_json = orjson.dumps(service_request)

# 發送 POST 請求到 HAPI FHIR 伺服器
url = f'{sApiUrl}'
headers = {"Content-Type": "application/fhir+json",
           # 'Authorization': f'Bearer {sJWT}'
           }
response = requests.post(url, data=service_request_json, headers=headers)

print(response.status_code)
print(response.json())

# # for update service request
# srid = ''
# url = f'{sApiUrl}}/{srid}'
# headers = {"Content-Type": "application/fhir+json",
#            # 'Authorization': f'Bearer {sJWT}'
#            }
# response = requests.put(url, data=service_request_json, headers=headers)
# print(response.status_code)
# print(response.json())