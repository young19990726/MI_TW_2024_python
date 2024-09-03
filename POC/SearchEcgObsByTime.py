from datetime import datetime, timedelta

from fhirclient import client
from fhirclient.models.observation import Observation


settings = {
    'app_id': 'FHIRConverter',
    'api_base': 'http://fhirserver.ndmctsgh.edu.tw:18080/fhir'
}

serverFhir = client.FHIRClient(settings=settings)

dtNow = datetime.now()
dtOneMonthAge = dtNow - timedelta(days=30)
# ge 是 greater or equal 的意思
strDateQryStart = f'ge{dtOneMonthAge.strftime("%Y-%m-%d")}'

search_params = {
    'code': 'urn:oid:2.16.840.1.113883.6.24|131328',
    'date': strDateQryStart
}

observations = Observation.where(search_params).perform_resources(serverFhir.server)

for observation in observations:
    print(f"Observation ID: {observation.id}, Date: {observation.effectiveDateTime.isostring}")
