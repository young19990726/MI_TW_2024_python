from fhirclient import client
from fhirclient.models.patient import Patient

settings = {
    'app_id': 'FHIRConverter',
    'api_base': 'http://fhirserver.ndmctsgh.edu.tw:18080/fhir'
}
fhirServer = client.FHIRClient(settings=settings)

pt108 = Patient.read('108', fhirServer.server)

# 找出身份證字號
sID = list(filter(lambda x: x.system == 'http://www.moi.gov.tw', pt108.identifier))[0].value
# 找出 CHARTNO
sChartnoStr = list(filter(lambda x: x.system == 'urn:oid:1.2.36.146.595.217.0.1' and 'MEDNO' in x.value, pt108.identifier))[0].value
# 找出患者住家地址
sHomeAddress = list(filter(lambda x: x.use == 'home', pt108.address))[0].text

print(f'患者姓名: {pt108.name[0].text}')
print(f'患者身份證字號: {sID}')
print(f'患者 MEDNO: {sChartnoStr.split('=')[1]}')
print(f'患者性別: {pt108.gender}')
print(f'患者生日: {pt108.birthDate}')
print(f'患者住家地址: {sHomeAddress}')
