import requests
from flask import request, render_template, redirect, url_for, jsonify, send_file, abort
from fhirclient import client, server
from fhirclient.models.patient import Patient
from fhirclient.models.observation import Observation
from fhirclient.models.servicerequest import ServiceRequest
from fhirclient.models.bundle import Bundle, BundleEntry

from utilities.python.forOauth import getSessionWithToken, get_token

sessionAuthed = getSessionWithToken()
# FHIR server settings
settings = {
    'app_id': 'FHIRConverter',
    'api_base': 'http://172.18.0.53:10004/fhir'
}
fhirServer = client.FHIRClient(settings=settings)

fhirServer.server.session = sessionAuthed

# Define EKG and BMD codes
ecg_codes = ['3130004', '131328']
bmd_codes = ['3998005', '38263-0', '80948-3', '80947-5', '38267-1']


def index():
    return render_template('index.html')

def search():
    try:
        if request.method == 'POST':
            patient_id = request.form.get('patient_id')
            # 查詢病人資料
            patient_data = Patient.read(patient_id, fhirServer.server)
            # 找出身份證字號
            sID = list(filter(lambda x: x.system == 'http://www.moi.gov.tw', patient_data.identifier))[0].value
            return render_template('index.html', patient_sID=sID)
        else:
            return redirect(url_for('index'))
    except Exception as e:
        return render_template('index.html', error_msg=e)

def searchObservation():
    try:
        if request.method == 'POST':
            patient_id = request.form.get('patient_id')
            loinc_code = request.form.get('CODE')
            url = f"{fhirServer.server.base_uri}/Observation?patient={patient_id}&code={loinc_code}"

            sToken = get_token()
            headers = {'Content-Type': 'application/fhir+json', 'Authorization':f'Bearer {sToken}'}
            response = requests.get(url, headers=headers)
            bundle = Bundle(response.json())
            observations = [entry.resource.as_json() for entry in bundle.entry]
            # 找出血壓
            if loinc_code == '85354-9':
                blood_pressure_data = []
                for observation in observations:
                    components = observation.get('component', [])
                    systolic = None
                    diastolic = None
                    for component in components:
                        code = component['code']['coding'][0]['code']
                        value = component['valueQuantity']['value']
                        # 收縮壓
                        if code == '8480-6':
                            systolic = value
                        # 舒張壓
                        elif code == '8462-4':
                            diastolic = value

                    if systolic is not None and diastolic is not None:
                        blood_pressure_data.append({
                            'systolic': systolic,
                            'diastolic': diastolic,
                            'date': observation.get('effectiveDateTime')
                        })
                return render_template('index.html', bloodPressureData=blood_pressure_data)
            # 找出心電圖數據
            elif loinc_code == '131328':
                ekg_data = []
                for observation in observations:
                    components = observation.get('component', [])
                    for component in components:
                        code = component['code']['coding'][0]['code']
                        value_sampled_data = component.get('valueSampledData', {})
                        data = value_sampled_data.get('data', '')
                        data_points = [float(point) for point in data.split() if point]
                        ekg_data.append({
                            'data': data_points
                        })
                return render_template('index.html', EkgData=ekg_data)

        else:
            return redirect(url_for('index'))
    except Exception as e:
        return render_template('index.html', error_msg=e)

# API endpoint: Get ServiceRequest by code
# @app.route("/api/servicerequest/<string:code>", methods=['GET'])
def get_service_request(code):
    if code in ecg_codes + bmd_codes:
        SvcReqSearch = ServiceRequest.where(struct={'code': f'http://snomed.info/sct|{code}'})
    else:
        abort(400, description="Unsupported code")

    listSvcReq = SvcReqSearch.perform_resources(fhirServer.server)

    if not listSvcReq:
        abort(404, description="ServiceRequest not found")

    return jsonify([svc.as_json() for svc in listSvcReq])

# API endpoint: Get Observation by ServiceRequest ID
# @app.route("/api/observation/<string:servicerequest_id>", methods=['GET'])
def get_observation(servicerequest_id):
    obsSearch = Observation.where(struct={'based-on': servicerequest_id})
    listObs = obsSearch.perform_resources(fhirServer.server)

    if not listObs:
        abort(404, description="Observations not found")

    for obs in listObs:
        if obs.code and obs.code.coding:
            for coding in obs.code.coding:
                if coding.code in ecg_codes + bmd_codes:
                    return jsonify(obs.as_json())

        else:
            print("No coding information in code.")

    abort(404, description="Unsupported ServiceRequest type")
