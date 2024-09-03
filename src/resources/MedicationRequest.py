import requests
import orjson

medication_request = {
    "resourceType": "MedicationRequest",
    "meta": {
        "profile": ["https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/MedicationRequest-twcore"]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>藥品請求的詳細資料</b></h3><p><b>藥品請求的識別碼</b>：7077 （http://www.moi.gov.tw）</p><p><b>藥品請求的狀態</b>：Active <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\">( <a href=\"http://terminology.hl7.org/CodeSystem/medicationrequest-status-reason\">MedicationRequest Status Reason Codes</a>#clarif)</span></p><p><b>藥品請求的意圖</b>：Order <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\">( <a href=\"http://hl7.org/fhir/CodeSystem/medicationrequest-intent\">medicationRequest Intent</a>#order)</span></p><p><b>藥品請求的類別</b>：Discharge <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\">( <a href=\"http://terminology.hl7.org/CodeSystem/medicationrequest-category\">MedicationRequest Category Codes</a>#discharge)</span></p><p><b>藥品</b>：阿立批挫 <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\">( <a href=\"CodeSystem-medication-fda-tw.html\">臺灣藥品及醫療器材代碼值集</a>#衛署藥輸字第025485號)</span></p><p><b>病人</b>：<a href=\"Patient-pat-example.html\">Patient/pat-example</a> \"陳加玲\"</p><p><b>就醫事件</b>：<a href=\"Encounter-enc-example.html\">Encounter/enc-example</a></p><p><b>最初請求時間</b>：2022-08-01 06:00:14-0500</p><p><b>提出藥品請求請求者</b>：<a href=\"Practitioner-pra-dr-example.html\">Practitioner/pra-dr-example</a> \"王依昇\"</p><p><b>開立處方的原因</b>：<a href=\"Observation-obs-lab-example.html\">Observation/obs-lab-example</a></p><p><b>處方可用以配藥的有效期限</b>：2022-08-01 06:00:14-0500 --&gt; 2022-08-08 06:00:14-0500</p></div>"
    },
    "identifier": [{
        "system": "http://www.moi.gov.tw",
        "value": "7077"
    }],
    "status": "active",
    "statusReason": {
        "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/medicationrequest-status-reason",
            "code": "clarif"
        }]
    },
    "intent": "order",
    "category": [{
        "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/medicationrequest-category",
            "code": "discharge"
        }]
    }],
    "medicationCodeableConcept": {
        "coding": [{
            "system": "https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-fda-tw",
            "code": "衛署藥輸字第025485號",
            "display": "阿立批挫"
        }],
        "text": "阿立批挫"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "encounter": {
        "reference": "Encounter/111"
    },
    "authoredOn": "2022-08-01T18:00:14+08:00",
    "requester": {
        "reference": "Practitioner/103"
    },
    "reasonReference": [{
        "reference": "Observation/112"
    }],
    "dosageInstruction": [{
        "text": "三餐飯後，口服",
        "timing": {
            "code": {
                "coding": [{
                    "system": "https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-frequency-nhi-tw",
                    "code": "PC"
                }],
                "text": "三餐飯後"
            }
        },
        "route": {
            "coding": [{
                "system": "https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medication-path-tw",
                "code": "PO"
            }]
        },
        "doseAndRate": [{
            "type": {
                "coding": [{
                    "system": "http://terminology.hl7.org/CodeSystem/dose-rate-type",
                    "code": "ordered"
                }]
            }
        }]
    }],
    "dispenseRequest": {
        "validityPeriod": {
            "start": "2022-08-01T18:00:14+08:00",
            "end": "2022-08-08T18:00:14+08:00"
        }
    }
}

# 將 ServiceRequest 資源轉換為 JSON 格式
service_request_json = orjson.dumps(medication_request)

# 發送 POST 請求到 HAPI FHIR 伺服器
url = "http://fhirserver.ndmctsgh.edu.tw:18080/fhir/MedicationRequest"
headers = {"Content-Type": "application/fhir+json"}
response = requests.post(url, data=service_request_json, headers=headers)

print(response.status_code)
print(response.json())
