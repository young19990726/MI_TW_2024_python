import orjson
from fhirclient import client
from fhirclient.models import bundle, molecularsequence
from fhirclient.models.bundle import BundleEntry
from fhirclient.models.molecularsequence import MolecularSequence


settings = {
    'app_id': 'FHIRConverter',
    'api_base': 'http://fhirserver.ndmctsgh.edu.tw:18080/fhir'
}

serverFhir = client.FHIRClient(settings=settings)

bundleMolSeqs = bundle.Bundle()
bundleMolSeqs.type = 'searchset'

search_param = {
    'patient': '108',
    'chromosome': 'http://www.ensembl.org|NC_000007.14',
    'variant-start': '55191822',
    'variant-end': '55191822'
}

# 執行查詢
MolSeqs = MolecularSequence.where(search_param).perform_resources(serverFhir.server)
listMolSeqsEntries = [BundleEntry() for molseq in MolSeqs]

# 使用 zip 將兩個列表配對並賦值
for be, ms in zip(listMolSeqsEntries, MolSeqs):
    be.resource = ms
bundleMolSeqs.entry = listMolSeqsEntries

print(orjson.dumps(bundleMolSeqs.as_json(), option=orjson.OPT_INDENT_2).decode('utf-8'))