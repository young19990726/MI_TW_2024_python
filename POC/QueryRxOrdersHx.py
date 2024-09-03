from fhirclient import client
from fhirclient.models.medicationrequest import MedicationRequest

# 初始化 FHIR 客戶端
settings = {
    'app_id': 'FHIRConverter',
    'api_base': 'http://fhirserver.ndmctsgh.edu.tw:18080/fhir'
}
fhirServer = client.FHIRClient(settings=settings)

# 患者的 ID
patient_id = '108'

# # 查詢患者的藥物處方
# medication_requests = MedicationRequest.where({'patient': patient_id}).perform(fhirServer.server)
# 
# # 輸出藥物處方
# for med_req in medication_requests.entry:
#     print(f"Medication: {med_req.resource.medicationCodeableConcept.text}")
#     print(f"Dosage: {med_req.resource.dosageInstruction[0].doseAndRate[0].doseQuantity.value} {med_req.resource.dosageInstruction[0].doseAndRate[0].doseQuantity.unit}, {med_req.resource.dosageInstruction[0].text}")
#     print(f"Status: {med_req.resource.status}")
#     print("-----")

# 或者也可以這樣寫
# 查詢患者的藥物處方
medication_requests = MedicationRequest.where({'patient': patient_id}).perform_resources(fhirServer.server)

# 輸出藥物處方
for med_req in medication_requests:
    print(f"Medication: {med_req.medicationCodeableConcept.text}")
    print(f"Dosage: {med_req.dosageInstruction[0].doseAndRate[0].doseQuantity.value} {med_req.dosageInstruction[0].doseAndRate[0].doseQuantity.unit}, {med_req.dosageInstruction[0].text}")
    print(f"Status: {med_req.status}")
    print("-----")