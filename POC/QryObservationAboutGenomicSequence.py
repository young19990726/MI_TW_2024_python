import orjson
from fhirclient import client
from fhirclient.models.observation import Observation

# 初始化 FHIR 客戶端
settings = {
    'app_id': 'FHIRConverter',
    'api_base': 'http://fhirserver.ndmctsgh.edu.tw:18080/fhir'
}
fhirServer = client.FHIRClient(settings=settings)

# Perform a search for Observation resources
# search = Observation.where(struct={
#     'combo-code': 'http://loinc.org|55233-1'  # System and code combined
# })
search_params = {
    # 'component-code': 'http://loinc.org|48018-6', # 類別是基因分析
    # 'value-concept': 'http://www.genenames.org|HGNC:3236' # 必須完整的 Concept
    # 'combo-value-concept': 'http://www.genenames.org|' # 挑出是 HGNC 類的 Observation
    'component-value-concept': 'http://www.genenames.org|' # 挑出是 HGNC 類的 Observation
}

# Execute the search
# bundle = search.perform_resources(fhirServer.server)
listObs = Observation.where(search_params).perform_resources(fhirServer.server)

# Pretty print the result (optional)
for observation in listObs:
    print(orjson.dumps(observation.as_json(), option=orjson.OPT_INDENT_2).decode('utf-8'))
