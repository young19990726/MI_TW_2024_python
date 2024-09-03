import orjson
import requests
from fhir.resources.observation import Observation

# 創建新的 observation 資源

# Scenario #1 ------------------
# 血糖 LOINC 2339-0
S1_bloodGlucose = {
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
}
# 飯前血糖 LOINC 88365-2
S1_bloodGlucosePerMeal = {
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
}
# 飯後血糖 LOINC 87422-2
S1_bloodGlucosePostMeal = {
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
            "code": "87422-2",
            "display": "Glucose [Mass/volume] in Blood --post meal"
        }],
        "text": "Glucose [Mass/volume] in Blood --post meal"
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
}
# 血壓 LOINC 35094-2 or 85354-9 ?
S1_bloodPressure = {
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-bloodPressure-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>檢驗檢查資料</b></h3><p><b>狀態</b>：final</p><p><b>分類</b>：Vital Signs <span style=\"background: LightGoldenRodYellow; margin：4px; border：1px solid khaki\">( <a href=\"http://hl7.org/fhir/R4/codesystem-observation-category.html\">Observation Category Codes</a>#vital-signs)</span></p><p><b>檢驗項目</b>：Blood pressure panel with all children optional <span style=\"background: LightGoldenRodYellow; margin：4px; border：1px solid khaki\">( <a href=\"https://loinc.org/\">LOINC</a>#85354-9 \"Blood pressure panel with all children optional\")</span></p><p><b>病人</b>： <a href=\"Patient-pat-example.html\">Patient/108</a> \"高東萬\"</p><p><b>檢查者</b>：<a href=\"Practitioner-pra-dr-example.html\">Practitioner/103</a> \"John Smith\"</p><p><b>執行日期</b>：2024-07-31</p><p><b>檢驗結果</b></p><blockquote><p><b>檢驗項目</b>：Systolic blood pressure <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\">( <a href=\"https://loinc.org/\">LOINC</a>#8480-6)</span></p><p><b>檢驗值</b>：117 mmHg <span style=\"background: LightGoldenRodYellow\"></span></p></blockquote><blockquote><p><b>檢驗項目</b>：Diastolic blood pressure <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\">( <a href=\"https://loinc.org/\">LOINC</a>#8462-4)</span></p><p><b>檢驗值</b>：76 mmHg</p></blockquote></div>"
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
            "code": "85354-9",
            "display": "Blood Pressure panel"
        }],
        "text": "Blood Pressure panel"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "component": [
        {
            "code": {
                "coding": [{
                    "system": "http://loinc.org",
                    "code": "8480-6",
                    "display": "Systolic blood pressure"
                }]
            },
            "valueQuantity": {
                "value": 130,
                "unit": "mmHg",
                "system": "http://unitsofmeasure.org",
                "code": "mm[Hg]"
            }}, {
            "code": {
                "coding": [{
                    "system": "http://loinc.org",
                    "code": "8462-4",
                    "display": "Diastolic blood pressure"
                }]
            },
            "valueQuantity": {
                "value": 70,
                "unit": "mmHg",
                "system": "http://unitsofmeasure.org",
                "code": "mm[Hg]"
            }
        }]
}
# 體脂率 LOINC 41982-0  Vital signs or Laboratory?
S1_bodyFat = {
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
            "display": "Vital signs"
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
}
# 身高 LOINC 3137-7 or 8302-2
S1_bodyHeight = {
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
            "code": "8302-2",
            "display": "Body height"
        }],
        "text": "Body Height"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 180,
        "unit": "cm"
    }
}
# 體溫 LOINC 8310-5
S1_bodyTemperature = {
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
        "coding": [{
            "system": "http://loinc.org",
            "code": "8310-5",
            "display": "Body Temperature"
        }],
        "text": "Body Temperature"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 35.8,
        "unit": "Cel"
    }
}
# 體重 LOINC 29463-7
S1_bodyWeight = {
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
        "coding": [{
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
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 70.5,
        "unit": "kg"
    }
}
# 微血管充填時間 LOINC 44963-7 Laboratory?
S1_capillaryRefill = {
    "resourceType": "Observation",
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>Observation Vital-sign 微血管充填時間資料</b></h3></div>"
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
            "code": "44963-7",
            "display": "Capillary refill [Time] of Nail bed"
        }
        ],
        "text": "Capillary refill time of Nail bed"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 2,
        "unit": "seconds",
        "system": "http://unitsofmeasure.org",
        "code": "s"
    }
}
# 右手握力 LOINC 83174-3 Vital signs?
# 1 WARNING
S1_gripStrengthRight = {
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-vitalSigns-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>Observation Vital-sign 右手握力資料</b></h3></div>"
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
            "code": "83174-3",
            "display": "Grip strength Hand - right Dynamometer"
        }],
        "text": "Grip strength Hand - right Dynamometer"
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
        "unit": "kg"
    }
}
# 心率 LOINC 8867-4
S1_HeartRate = {
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-vitalSigns-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>Observation Vital-sign 心率資料</b></h3></div>"
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
            "code": "8867-4",
            "display": "Heart rate"
        }],
        "text": "Heart rate"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 80,
        "unit": "beats/minute",
        "system": "http://unitsofmeasure.org",
        "code": "/min"
    }
}
# 脈搏 LOINC 8867-4?
S1_PulseRate = {
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-vitalSigns-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>Observation Vital-sign 脈搏資料</b></h3></div>"
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
            "code": "8867-4",
            "display": "Heart rate"
        }],
        "text": "Heart rate"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 80,
        "unit": "beats/minute",
        "system": "http://unitsofmeasure.org",
        "code": "/min"
    }
}
# 呼吸頻率 LOINC 9279-1
S1_RespiratoryRate = {
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-vitalSigns-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>Observation Vital-sign 呼吸頻率資料</b></h3></div>"
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
            "code": "9279-1",
            "display": "Respiratory Rate"
        }],
        "text": "Respiratory Rate"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 15,
        "unit": "breaths/minute",
        "system": "http://unitsofmeasure.org",
        "code": "/min"
    }
}
# 脈博血氧飽和度 LOINC 2708-6 or 59408-5?
S1_SpO2 = {
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-vitalSigns-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>Observation Vital-sign 脈博血氧飽和度 資料</b></h3></div>"
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
            "code": "2708-6",
            "display": "Oxygen saturation in Arterial blood by Pulse oximetry"
        }],
        "text": "Oxygen saturation in Arterial blood by Pulse oximetry"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 50,
        "unit": "%"
    }
}

# Scenario #2 ------------------
# 需要依據處方簽(MedicationRequest)中的天數早晚各上傳一次血壓與心率量測值。血壓與心率的資料中必須參考到該處方簽。

# 血壓 LOINC 35094-2 or 85354-9 ?
S2_bloodPressure = {
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-bloodPressure-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>檢驗檢查資料</b></h3></div>"
    },
    "basedOn": [{
        "reference": "MedicationRequest/"
    }],
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
            "code": "85354-9",
            "display": "Blood Pressure panel"
        }],
        "text": "Blood Pressure panel"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "component": [
        {
            "code": {
                "coding": [{
                    "system": "http://loinc.org",
                    "code": "8480-6",
                    "display": "Systolic blood pressure"
                }]
            },
            "valueQuantity": {
                "value": 120,
                "unit": "mmHg",
                "system": "http://unitsofmeasure.org",
                "code": "mm[Hg]"
            }}, {
            "code": {
                "coding": [{
                    "system": "http://loinc.org",
                    "code": "8462-4",
                    "display": "Diastolic blood pressure"
                }]
            },
            "valueQuantity": {
                "value": 78,
                "unit": "mmHg",
                "system": "http://unitsofmeasure.org",
                "code": "mm[Hg]"
            }
        }]
}
# 心率 LOINC 8867-4
S2_HeartRate = {
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://twcore.mohw.gov.tw/ig/twcore/StructureDefinition/Observation-vitalSigns-twcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>檢驗檢查資料</b></h3></div>"
    },
    "basedOn": [{
        "reference": "MedicationRequest/"
    }],
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
            "code": "8867-4",
            "display": "Heart rate"
        }],
        "text": "Heart rate"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 80,
        "unit": "beats/minute",
        "system": "http://unitsofmeasure.org",
        "code": "/min"
    }
}

# Scenario #3 ------------------
# 資料中必須參考到檢查單(ServiceRequest)
# ServiceRequest.code.coding.system：http://snomed.info/sct
# ServiceRequest.code.coding.code：3998005
# ServiceRequest.code.coding.display：Bone imaging of limited area
# 已將測試合併成股骨密度、左股骨密度、右股骨密度與腰椎骨質密度四項。因此若要通過測試，各項目內的各個部位皆須完成審核。

# 股骨密度 LOINC 38263-0 (股骨幹密度、股骨頸密度、股骨全部密度、股骨 Ward 三角密度)
S3_boneDensityDXATscoreBodyOfFemur = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38263-0",
            "display": "DXA Femur [T-score] Bone density"
        }],
        "text": "DXA Femur [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.889,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "119190009"
        }],
        "text": "Entire shaft of femur"
    }
}
S3_boneDensityDXATscoreNeckOfFemur = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38263-0",
            "display": "DXA Femur [T-score] Bone density"
        }],
        "text": "DXA Femur [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.889,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "29627003"
        }],
        "text": "Structure of neck of femur"
    }
}
S3_boneDensityDXATscoreEntireFemur = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38263-0",
            "display": "DXA Femur [T-score] Bone density"
        }],
        "text": "DXA Femur [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "182046008"
        }],
        "text": "Entire femur"
    }
}
S3_boneDensityDXATscoreEntireFemurTriangle = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38263-0",
            "display": "DXA Femur [T-score] Bone density"
        }],
        "text": "DXA Femur [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "731966006"
        }],
        "text": "Entire femoral triangle (body structure)"
    }
}

# 左股骨骨密度 LOINC 80948-3 (股骨幹密度、股骨頸密度、股骨全部密度、股骨 Ward 三角密度)
S3_boneDensityDXATscoreBodyOfLFemur = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "80948-3",
            "display": "DXA Femur - left [T-score] Bone density"
        }],
        "text": "DXA Femur - left [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.889,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "119190009"
        }],
        "text": "Entire shaft of femur"
    }
}
S3_boneDensityDXATscoreNeckOfLFemur = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "80948-3",
            "display": "DXA Femur - left [T-score] Bone density"
        }],
        "text": "DXA Femur - left [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.889,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "29627003"
        }],
        "text": "Structure of neck of femur"
    }
}
S3_boneDensityDXATscoreEntireLFemur = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "80948-3",
            "display": "DXA Femur - left [T-score] Bone density"
        }],
        "text": "DXA Femur - left [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "182046008"
        }],
        "text": "Entire femur"
    }
}
S3_boneDensityDXATscoreEntireLFemurTriangle = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "80948-3",
            "display": "DXA Femur - left [T-score] Bone density"
        }],
        "text": "DXA Femur - left [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "731966006"
        }],
        "text": "Entire femoral triangle (body structure)"
    }
}

# 右股骨骨密度 LOINC 80947-5 (股骨幹密度、股骨頸密度、股骨全部密度、股骨 Ward 三角密度)
S3_boneDensityDXATscoreBodyOfRFemur = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "80947-5",
            "display": "DXA Femur - right [T-score] Bone density "
        }],
        "text": "DXA Femur - right [T-score] Bone density "
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.889,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "119190009"
        }],
        "text": "Entire shaft of femur"
    }
}
S3_boneDensityDXATscoreNeckOfRFemur = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "80947-5",
            "display": "DXA Femur - right [T-score] Bone density "
        }],
        "text": "DXA Femur - right [T-score] Bone density "
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.889,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "29627003"
        }],
        "text": "Structure of neck of femur"
    }
}
S3_boneDensityDXATscoreEntireRFemur = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "80947-5",
            "display": "DXA Femur - right [T-score] Bone density"
        }],
        "text": "DXA Femur - right [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "182046008"
        }],
        "text": "Entire femur"
    }
}
S3_boneDensityDXATscoreEntireRFemurTriangle = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "80947-5",
            "display": "DXA Femur - right [T-score] Bone density"
        }],
        "text": "DXA Femur - right [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "731966006"
        }],
        "text": "Entire femoral triangle (body structure)"
    }
}

# 腰椎骨密度 LOINC 38267-1 (腰椎第一節、腰椎第二節、腰椎第三節、腰椎第四節、腰椎第一~二節、腰椎第一~三節、腰椎第一~四節、腰椎第二~三節、腰椎第二~四節、腰椎第三~四節)
S3_boneDensityDXATscoreLumbarSpineL1 = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38267-1",
            "display": "DXA Lumbar spine [T-score] Bone density"
        }],
        "text": "DXA Lumbar spine [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "66794005"
        }],
        "text": "Bone structure of L1 (body structure)"
    }
}
S3_boneDensityDXATscoreLumbarSpineL2 = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38267-1",
            "display": "DXA Lumbar spine [T-score] Bone density"
        }],
        "text": "DXA Lumbar spine [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "14293000"
        }],
        "text": "Bone structure of L2 (body structure)"
    }
}
S3_boneDensityDXATscoreLumbarSpineL3 = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38267-1",
            "display": "DXA Lumbar spine [T-score] Bone density"
        }],
        "text": "DXA Lumbar spine [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "36470004"
        }],
        "text": "Bone structure of L3 (body structure)"
    }
}
S3_boneDensityDXATscoreLumbarSpineL4 = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38267-1",
            "display": "DXA Lumbar spine [T-score] Bone density"
        }],
        "text": "DXA Lumbar spine [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "11994002"
        }],
        "text": "Bone structure of L4 (body structure)"
    }
}
S3_boneDensityDXATscoreLumbarSpineL1_L2 = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38267-1",
            "display": "DXA Lumbar spine [T-score] Bone density"
        }],
        "text": "DXA Lumbar spine [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "1179750007"
        }],
        "text": "Structure of facet joint between first and second vertebra of lumbar spine (body structure)"
    }
}
S3_boneDensityDXATscoreLumbarSpineL2_L3 = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38267-1",
            "display": "DXA Lumbar spine [T-score] Bone density"
        }],
        "text": "DXA Lumbar spine [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "1179751006"
        }],
        "text": "Structure of facet joint between second and third vertebra of lumbar spine (body structure)"
    }
}
S3_boneDensityDXATscoreLumbarSpineL3_L4 = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38267-1",
            "display": "DXA Lumbar spine [T-score] Bone density"
        }],
        "text": "DXA Lumbar spine [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [{
            "system": "http://snomed.info/sct",
            "code": "1179749007"
        }],
        "text": "Structure of facet joint between third and fourth vertebra of lumbar spine (body structure))"
    }
}
S3_boneDensityDXATscoreLumbarSpineL1_L3 = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38267-1",
            "display": "DXA Lumbar spine [T-score] Bone density"
        }],
        "text": "DXA Lumbar spine [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "1179750007"
            },
            {
                "system": "http://snomed.info/sct",
                "code": "1179751006"
            }
        ],
        "text": "Structure of facet joint between first and second, second and third vertebra of lumbar spine (body structure))"
    }
}
S3_boneDensityDXATscoreLumbarSpineL1_L4 = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38267-1",
            "display": "DXA Lumbar spine [T-score] Bone density"
        }],
        "text": "DXA Lumbar spine [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "1179750007"
            },
            {
                "system": "http://snomed.info/sct",
                "code": "1179751006"
            },
            {
                "system": "http://snomed.info/sct",
                "code": "1179749007"
            }
        ],
        "text": "Structure of facet joint between first and second, second and third, third and fourth vertebra of lumbar spine (body structure))"
    }
}
S3_boneDensityDXATscoreLumbarSpineL2_L4 = {
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
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
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
            "code": "38267-1",
            "display": "DXA Lumbar spine [T-score] Bone density"
        }],
        "text": "DXA Lumbar spine [T-score] Bone density"
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-13T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "valueQuantity": {
        "value": 0.887,
        "unit": "g/cm²",
        "system": "http://unitsofmeasure.org",
        "code": "g/cm-2"
    },
    "bodySite": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "1179751006"
            },
            {
                "system": "http://snomed.info/sct",
                "code": "1179749007"
            }
        ],
        "text": "Structure of facet joint between second and third, third and fourth vertebra of lumbar spine (body structure))"
    }
}

# Scenario #4 ------------------
# 數據類別的代碼系統使用：urn:oid:2.16.840.1.113883.6.24
# 資料中必須參考到檢查單(ServiceRequest)。
# ServiceRequest.code.coding.system：http://snomed.info/sct
# ServiceRequest.code.coding.code：3130004
# ServiceRequest.code.coding.display：Monitoring of cardiac output by electrocardiogram
# original measured value[i] = (valueSampledData.data[i] - valueSampledData.origin.value) * valueSampledData.factor
# period 是以毫秒為單位。
# data 欄位規定上是以空白做間隔。
# 須提供自家產品繪製心電圖的畫面。此介面必須包含標準心電圖格線，並附上格線的 scale，以及每個心電圖對應的導程名稱。

# 12導程心電圖
S4_EKG = {
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "https://standard-interoperability-lab.com/fhir/StructureDefinition/Observationtwcore"
        ]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h3><b>心電圖資料</b></h3></div>"
    },
    "basedOn": [{
        "reference": "ServiceRequest/"
    }],
    "status": "final",
    "category": [{
        "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
            "code": "procedure",
            "display": "Procedure"
        }]
    }],
    "code": {
        "coding": [{
            "system": "urn:oid:2.16.840.1.113883.6.24",
            "code": "131328",
            "display": "MDC_ECG_ELEC_POT"
        }]
    },
    "subject": {
        "reference": "Patient/108"
    },
    "effectiveDateTime": "2024-08-16T09:30:10+01:00",
    "performer": [{
        "reference": "Practitioner/103"
    }],
    "device": {
        "display": "12 lead EKG Device Metric"
    },
    "component": [
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131329",
                        "display": "MDC_ECG_ELEC_POTL_I"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 2408
                },
                "period": 4,
                "factor": 1.612,
                "lowerLimit": -3300,
                "upperLimit": 3300,
                "dimensions": 1,
                "data": "2041 2043 2037 2047 2060 2062 2051 2023 2014 2027 2034 2033 2040 2047 2047 2053 2058 2064 2059 2063 2061 2052 2053 2038 1966 1885 1884 2009 2129 2166 2137 2102 2086 2077 2067 2067 2060 2059 2062 2062 2060 2057 2045 2047 2057 2054 2042 2029 2027 2018 2007 1995 2001 2012 2024 2039 2068 2092 2111 2125 2131 2148 2137 2138 2128 2128 2115 2099 2097 2096 2101 2101 2091 2073 2076 2077 2084 2081 2088 2092 2070 2069 2074 2077 2075 2068 2064 2060 2062 2074 2075 2074 2075 2063 2058 2058 2064 2064 2070 2074 2067 2060 2062 2063 2061 2059 2048 2052 2049 2048 2051 2059 2059 2066 2077 2073"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131330",
                        "display": "MDC_ECG_ELEC_POTL_II"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 2408
                },
                "period": 4,
                "factor": 1.612,
                "lowerLimit": -3300,
                "upperLimit": 3300,
                "dimensions": 1,
                "data": "2045 2047 2040 2050 2063 2065 2054 2026 2017 2030 2037 2036 2043 2050 2050 2056 2061 2067 2062 2066 2064 2055 2056 2041 1969 1888 1887 2012 2132 2169 2140 2105 2089 2080 2070 2070 2063 2062 2065 2065 2063 2060 2048 2050 2060 2057 2045 2032 2030 2021 2010 1998 2004 2015 2027 2042 2071 2095 2114 2128 2134 2151 2140 2141 2131 2131 2118 2102 2100 2099 2104 2104 2094 2076 2079 2080 2087 2084 2091 2095 2073 2072 2077 2080 2078 2071 2067 2063 2065 2077 2078 2077 2078 2066 2061 2061 2067 2067 2073 2077 2070 2063 2065 2066 2064 2062 2051 2055 2052 2051 2054 2062 2062 2069 2080 2076"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131331",
                        "display": "MDC_ECG_ELEC_POTL_III"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 2408
                },
                "period": 4,
                "factor": 1.612,
                "lowerLimit": -3300,
                "upperLimit": 3300,
                "dimensions": 1,
                "data": "2049 2051 2044 2054 2067 2069 2058 2030 2021 2034 2041 2040 2047 2054 2054 2060 2065 2071 2066 2070 2068 2059 2060 2045 1973 1892 1891 2016 2136 2173 2144 2109 2093 2084 2074 2074 2067 2066 2069 2069 2067 2064 2052 2054 2064 2061 2049 2036 2034 2025 2014 2002 2008 2019 2031 2046 2075 2099 2118 2132 2138 2155 2144 2145 2135 2135 2122 2106 2104 2103 2108 2108 2098 2080 2083 2084 2091 2088 2095 2099 2077 2076 2081 2084 2082 2075 2071 2067 2069 2081 2082 2081 2082 2070 2065 2065 2071 2071 2077 2081 2074 2067 2069 2070 2068 2066 2055 2059 2056 2055 2058 2066 2066 2073 2084 2080"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131389",
                        "display": "MDC_ECG_ELEC_POTL_AVR"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 2408
                },
                "period": 4,
                "factor": 1.612,
                "lowerLimit": -3300,
                "upperLimit": 3300,
                "dimensions": 1,
                "data": "2053 2055 2048 2058 2071 2073 2062 2034 2025 2038 2045 2044 2051 2058 2058 2064 2069 2075 2070 2074 2072 2063 2064 2049 1977 1896 1895 2020 2140 2177 2148 2113 2097 2088 2078 2078 2071 2070 2073 2073 2071 2068 2056 2058 2068 2065 2053 2040 2038 2029 2018 2006 2012 2023 2035 2050 2079 2103 2122 2136 2142 2159 2148 2149 2139 2139 2126 2110 2108 2107 2112 2112 2102 2084 2087 2088 2095 2092 2099 2103 2081 2080 2085 2088 2086 2079 2075 2071 2073 2085 2086 2085 2086 2074 2069 2069 2075 2075 2081 2085 2078 2071 2073 2074 2072 2070 2059 2063 2060 2059 2062 2070 2070 2077 2088 2084"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131390",
                        "display": "MDC_ECG_ELEC_POTL_AVL"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 2408
                },
                "period": 4,
                "factor": 1.612,
                "lowerLimit": -3300,
                "upperLimit": 3300,
                "dimensions": 1,
                "data": "2057 2059 2052 2062 2075 2077 2066 2038 2029 2042 2049 2048 2055 2062 2062 2068 2073 2079 2074 2078 2076 2067 2068 2053 1981 1900 1899 2024 2144 2181 2152 2117 2101 2092 2082 2082 2075 2074 2077 2077 2075 2072 2060 2062 2072 2069 2057 2044 2042 2033 2022 2010 2016 2027 2039 2054 2083 2107 2126 2140 2146 2163 2152 2153 2143 2143 2130 2114 2112 2111 2116 2116 2106 2088 2091 2092 2099 2096 2103 2107 2085 2084 2089 2092 2090 2083 2079 2075 2077 2089 2090 2089 2090 2078 2073 2073 2079 2079 2085 2089 2082 2075 2077 2078 2076 2074 2063 2067 2064 2063 2066 2074 2074 2081 2092 2088"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131391",
                        "display": "MDC_ECG_ELEC_POTL_AVF"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 2408
                },
                "period": 4,
                "factor": 1.612,
                "lowerLimit": -3300,
                "upperLimit": 3300,
                "dimensions": 1,
                "data": "2061 2063 2056 2066 2079 2081 2070 2042 2033 2046 2053 2052 2059 2066 2066 2072 2077 2083 2078 2082 2080 2071 2072 2057 1985 1904 1903 2028 2148 2185 2156 2121 2105 2096 2086 2086 2079 2078 2081 2081 2079 2076 2064 2066 2076 2073 2061 2048 2046 2037 2026 2014 2020 2031 2043 2058 2087 2111 2130 2144 2150 2167 2156 2157 2147 2147 2134 2118 2116 2115 2120 2120 2110 2092 2095 2096 2103 2100 2107 2111 2089 2088 2093 2096 2094 2087 2083 2079 2081 2093 2094 2093 2094 2082 2077 2077 2083 2083 2089 2093 2086 2079 2081 2082 2080 2078 2067 2071 2068 2067 2070 2078 2078 2085 2096 2092"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131392",
                        "display": "MDC_ECG_ELEC_POTL_V1"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 2408
                },
                "period": 4,
                "factor": 1.612,
                "lowerLimit": -3300,
                "upperLimit": 3300,
                "dimensions": 1,
                "data": "2065 2067 2060 2070 2083 2085 2074 2046 2037 2050 2057 2056 2063 2070 2070 2076 2081 2087 2082 2086 2084 2075 2076 2061 1989 1908 1907 2032 2152 2189 2160 2125 2109 2100 2090 2090 2083 2082 2085 2085 2083 2080 2068 2070 2080 2077 2065 2052 2050 2041 2030 2018 2024 2035 2047 2062 2091 2115 2134 2148 2154 2171 2160 2161 2151 2151 2138 2122 2120 2119 2124 2124 2114 2096 2099 2100 2107 2104 2111 2115 2093 2092 2097 2100 2098 2091 2087 2083 2085 2097 2098 2097 2098 2086 2081 2081 2087 2087 2093 2097 2090 2083 2085 2086 2084 2082 2071 2075 2072 2071 2074 2082 2082 2089 2100 2096"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131331",
                        "display": "MDC_ECG_ELEC_POTL_V2"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 2408
                },
                "period": 4,
                "factor": 1.612,
                "lowerLimit": -3300,
                "upperLimit": 3300,
                "dimensions": 1,
                "data": "2069 2071 2064 2074 2087 2089 2078 2050 2041 2054 2061 2060 2067 2074 2074 2080 2085 2091 2086 2090 2088 2079 2080 2065 1993 1912 1911 2036 2156 2193 2164 2129 2113 2104 2094 2094 2087 2086 2089 2089 2087 2084 2072 2074 2084 2081 2069 2056 2054 2045 2034 2022 2028 2039 2051 2066 2095 2119 2138 2152 2158 2175 2164 2165 2155 2155 2142 2126 2124 2123 2128 2128 2118 2100 2103 2104 2111 2108 2115 2119 2097 2096 2101 2104 2102 2095 2091 2087 2089 2101 2102 2101 2102 2090 2085 2085 2091 2091 2097 2101 2094 2087 2089 2090 2088 2086 2075 2079 2076 2075 2078 2086 2086 2093 2104 2100"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131332",
                        "display": "MDC_ECG_ELEC_POTL_V3"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 2408
                },
                "period": 4,
                "factor": 1.612,
                "lowerLimit": -3300,
                "upperLimit": 3300,
                "dimensions": 1,
                "data": "2073 2075 2068 2078 2091 2093 2082 2054 2045 2058 2065 2064 2071 2078 2078 2084 2089 2095 2090 2094 2092 2083 2084 2069 1997 1916 1915 2040 2160 2197 2168 2133 2117 2108 2098 2098 2091 2090 2093 2093 2091 2088 2076 2078 2088 2085 2073 2060 2058 2049 2038 2026 2032 2043 2055 2070 2099 2123 2142 2156 2162 2179 2168 2169 2159 2159 2146 2130 2128 2127 2132 2132 2122 2104 2107 2108 2115 2112 2119 2123 2101 2100 2105 2108 2106 2099 2095 2091 2093 2105 2106 2105 2106 2094 2089 2089 2095 2095 2101 2105 2098 2091 2093 2094 2092 2090 2079 2083 2080 2079 2082 2090 2090 2097 2108 2104"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131333",
                        "display": "MDC_ECG_ELEC_POTL_V4"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 2408
                },
                "period": 4,
                "factor": 1.612,
                "lowerLimit": -3300,
                "upperLimit": 3300,
                "dimensions": 1,
                "data": "2077 2079 2072 2082 2095 2097 2086 2058 2049 2062 2069 2068 2075 2082 2082 2088 2093 2099 2094 2098 2096 2087 2088 2073 2001 1920 1919 2044 2164 2201 2172 2137 2121 2112 2102 2102 2095 2094 2097 2097 2095 2092 2080 2082 2092 2089 2077 2064 2062 2053 2042 2030 2036 2047 2059 2074 2103 2127 2146 2160 2166 2183 2172 2173 2163 2163 2150 2134 2132 2131 2136 2136 2126 2108 2111 2112 2119 2116 2123 2127 2105 2104 2109 2112 2110 2103 2099 2095 2097 2109 2110 2109 2110 2098 2093 2093 2099 2099 2105 2109 2102 2095 2097 2098 2096 2094 2083 2087 2084 2083 2086 2094 2094 2101 2112 2108"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131334",
                        "display": "MDC_ECG_ELEC_POTL_V5"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 2408
                },
                "period": 4,
                "factor": 1.612,
                "lowerLimit": -3300,
                "upperLimit": 3300,
                "dimensions": 1,
                "data": "2081 2083 2076 2086 2099 2101 2090 2062 2053 2066 2073 2072 2079 2086 2086 2092 2097 2103 2098 2102 2100 2091 2092 2077 2005 1924 1923 2048 2168 2205 2176 2141 2125 2116 2106 2106 2099 2098 2101 2101 2099 2096 2084 2086 2096 2093 2081 2068 2066 2057 2046 2034 2040 2051 2063 2078 2107 2131 2150 2164 2170 2187 2176 2177 2167 2167 2154 2138 2136 2135 2140 2140 2130 2112 2115 2116 2123 2120 2127 2131 2109 2108 2113 2116 2114 2107 2103 2099 2101 2113 2114 2113 2114 2102 2097 2097 2103 2103 2109 2113 2106 2099 2101 2102 2100 2098 2087 2091 2088 2087 2090 2098 2098 2105 2116 2112"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "urn:oid:2.16.840.1.113883.6.24",
                        "code": "131335",
                        "display": "MDC_ECG_ELEC_POTL_V6"
                    }
                ]
            },
            "valueSampledData": {
                "origin": {
                    "value": 2408
                },
                "period": 4,
                "factor": 1.612,
                "lowerLimit": -3300,
                "upperLimit": 3300,
                "dimensions": 1,
                "data": "2085 2087 2080 2090 2103 2105 2094 2066 2057 2070 2077 2076 2083 2090 2090 2096 2101 2107 2102 2106 2104 2095 2096 2081 2009 1928 1927 2052 2172 2209 2180 2145 2129 2120 2110 2110 2103 2102 2105 2105 2103 2100 2088 2090 2100 2097 2085 2072 2070 2061 2050 2038 2044 2055 2067 2082 2111 2135 2154 2168 2174 2191 2180 2181 2171 2171 2158 2142 2140 2139 2144 2144 2134 2116 2119 2120 2127 2124 2131 2135 2113 2112 2117 2120 2118 2111 2107 2103 2105 2117 2118 2117 2118 2106 2101 2101 2107 2107 2113 2117 2110 2103 2105 2106 2104 2102 2091 2095 2092 2091 2094 2102 2102 2109 2120 2116"
            }
        }
    ]
}

# 使用 fhir.resources 進行驗證
# observation = Observation.parse_obj(bloodGlucose)

# 將 要上傳的 資源轉換為 JSON
Observation_json = orjson.dumps(S1_bloodGlucose, option=orjson.OPT_INDENT_2)

# 發送 POST 請求到 HAPI FHIR 伺服器
url = "http://fhirserver.ndmctsgh.edu.tw:18080/fhir/Observation"
headers = {"Content-Type": "application/fhir+json",
           # 'Authorization': f'Bearer {YOUR_JWT_TOKEN}'
           }
response = requests.post(url, data=Observation_json, headers=headers)

print(response.status_code)
print(response.json())

# # for update patient
# url = "http://fhirserver.ndmctsgh.edu.tw:18080/fhir/Patient/108"
# headers = {"Content-Type": "application/fhir+json"}
# response = requests.put(url, data=patient_json, headers=headers)
# print(response.status_code)
# print(response.json())

# Delete Observation
# url = "http://fhirserver.ndmctsgh.edu.tw:18080/fhir/Observation/117"
# headers = {"Content-Type": "application/fhir+json"}
# response = requests.delete(url)
# print(response.status_code)
# print(response.json())
