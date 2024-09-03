from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_restx import Api
from Web.webapi.genomic import ns, nsPage
from Web.webapi.route import index, searchObservation


def create_app():
    app = Flask(__name__,
                template_folder='page',
                static_folder='resources')
    app.add_url_rule('/', 'index', index, methods=['GET'])
    app.add_url_rule('/searchObservation', 'searchObservation', searchObservation, methods=['POST'])
    return app


app = create_app()

apiFHIR = Api(app, version='1.0', title='Genomic Data API', description='API for FHIR genomic data', doc='/swagger/')
CORS(app, resources={
    r"/": {"origins": "*"},
    # 只允許特定來源
    # r"/items/*": {"origins": ["http://example.com", "http://another-example.com"]},
    # 可以配置允許的方法
    r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"]}
})
apiFHIR.add_namespace(ns)
apiFHIR.add_namespace(nsPage)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30001, debug=True)
