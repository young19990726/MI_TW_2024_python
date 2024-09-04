import orjson
import requests

from utilities.python.forOauth import get_token

sApiUrl = 'http://172.18.0.53:10004/fhir/MolecularSequence'
sJWT = get_token()

# 創建一個新的 MoleucularSequence 資源
MolSeq_data = {
    "resourceType": "MolecularSequence",
    "meta": {
        "profile": ["http://hl7.org/fhir/StructureDefinition/MolecularSequence"]
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">\
              <p>此 MolecularSequence 資源描述了病人（分子實驗室患者編號：MEDNO=123456）的 DNA 序列。</p>\
              <p>此測序使用的樣本為分子樣本編號：MLD45-Z4-1234。</p>\
              <p>參考序列基於人類染色體7，GRCh38.p14 Primary Assembly（Ensembl ID：NC_000007.14）。</p>\
              <p>感興趣的序列窗口範圍從位置 55191822 到 55191822，在 Watson strand 上。</p>\
              <p>在此位置觀察到一個變異，觀察到的等位基因為 'G'，參考等位基因為 'T'。</p>\
            </div>"
    },
    "type": "dna",
    "coordinateSystem": 1,
    "patient": {
        "reference": "Patient/108",
        "display": "Molecular Lab Patient ID: MEDNO=123456"
    },
    "specimen": {
        "reference": "Specimen/120",
        "display": "Molecular Specimen ID: MLD45-Z4-1234"
    },
    "referenceSeq": {
        'chromosome': {
            "coding": [
                {
                    "system": "http://www.ensembl.org",
                    "code": "NC_000007.14",
                    "display": "Homo sapiens chromosome 7, GRCh38.p14 Primary Assembly"
                }
            ]
        },
        'genomeBuild': 'GRCh 38',
        "windowStart": 55191822,
        "windowEnd": 55191822,
        "strand": "watson"
    },
    "variant": [
        {
            "start": 55191822,
            "end": 55191822,
            "observedAllele": "G",
            "referenceAllele": "T",
            "cigar": "1M"
        }
    ]
}

# 將 MoleucularSequence 資源轉換為 JSON
MolSeq_json = orjson.dumps(MolSeq_data, option=orjson.OPT_INDENT_2)

# 發送 POST 請求到 HAPI FHIR 伺服器
url = f'{sApiUrl}'
headers = {"Content-Type": "application/fhir+json",
           'Authorization': f'Bearer {sJWT}'
           }
response = requests.post(url, data=MolSeq_json, headers=headers)

print(response.status_code)
print(response.json())
