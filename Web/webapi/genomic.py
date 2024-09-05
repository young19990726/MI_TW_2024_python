# 使用 Resource 定義 API 操作
from fhirclient import client
from fhirclient.models import bundle
from fhirclient.models.bundle import BundleEntry
from fhirclient.models.molecularsequence import MolecularSequence
from flask import request, send_from_directory
from flask_restx import Resource, fields, Namespace

from utilities.python.forOauth import getSessionWithToken

settings = {
    'app_id': 'FHIRConverter',
    'api_base': 'http://172.18.0.53:10004/fhir'
}

serverFhir = client.FHIRClient(settings=settings)
# 定義命名空間
ns = Namespace('api/Genomics', description='Resources operations')
nsPage = Namespace('/', description='Resources operations')

# 定義一個模型，用於自動生成 Swagger 文檔
data_model = ns.model('dataSearch', {
    'strPtid': fields.String(required=True, description='Patient ID'),
    'strChrID': fields.String(required=True, description='染色體 ID'),
    'strVarStart': fields.String(required=True, description='變異起始位點'),
    'strVarEnd': fields.String(required=True, description='變異結束位點')
})


@ns.route('/searchMolecularSequence')
class geneVarientSearchHandler(Resource):
    @ns.expect(data_model)
    @ns.doc('search_molecular_sequence')
    def post(self):
        serverFhir.server.session = getSessionWithToken()
        bundleMolSeqs = bundle.Bundle()
        bundleMolSeqs.type = 'searchset'
        dataSearch = request.json

        if not dataSearch:
            return {"error": "No Search JSON payload provided"}, 400

        search_param = {
            'patient': f'{dataSearch["strPtid"]}',
            'chromosome': f'http://www.ensembl.org|{dataSearch["strChrID"]}',
            'variant-start': f'{dataSearch["strVarStart"]}',
            'variant-end': f'{dataSearch["strVarEnd"]}'
        }

        # 執行查詢
        MolSeqs = MolecularSequence.where(search_param).perform_resources(serverFhir.server)
        listMolSeqsEntries = [BundleEntry() for molseq in MolSeqs]

        # 使用 zip 將兩個列表配對並賦值
        for be, ms in zip(listMolSeqsEntries, MolSeqs):
            be.resource = ms
        bundleMolSeqs.entry = listMolSeqsEntries

        # 這裡要特別注意型別。
        return bundleMolSeqs.as_json(), 200


@nsPage.route('/page/<path:filename>')
class getGeneVarientPage(Resource):
    def get(self, filename):
        return send_from_directory('page', filename)
