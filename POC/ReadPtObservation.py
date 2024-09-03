from fhirclient import client
from fhirclient.models.observation import Observation


settings = {
    'app_id': 'FHIRConverter',
    'api_base': 'http://fhirserver.ndmctsgh.edu.tw:18080/fhir'
}
fhirServer = client.FHIRClient(settings=settings)

# 定義只搜尋 Observation
search = Observation.where(struct={'subject': '108', 'status': 'final'})
observations = search.perform_resources(fhirServer.server)
# 查詢有哪些 observation 項目( in text, 去重複 )
for rslt in set([ob.code.text for ob in observations]):
    print(f'檢驗檢查項目: {rslt}')

# 查詢有哪些 observation 項目( in tuple(system, id) )
setObsCodes = {(rslt.code.coding[0].system, rslt.code.coding[0].code) for rslt in observations}
for obCode in setObsCodes:
    print(obCode)
