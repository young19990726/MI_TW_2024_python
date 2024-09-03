from fhirclient import client
from fhirclient.models.observation import Observation
from fhirclient.models.servicerequest import ServiceRequest
import decimal
import numpy as np
import matplotlib.pyplot as plt


settings = {
    'app_id': 'FHIRConverter',
    'api_base': 'http://fhirserver.ndmctsgh.edu.tw:18080/fhir'
}

serverFhir = client.FHIRClient(settings=settings)

SvcReqSearch = ServiceRequest.where(struct={'code': 'http://snomed.info/sct|3130004'})
listSvcReqEkg = SvcReqSearch.perform_resources(serverFhir.server)

for svcreq in listSvcReqEkg:
    obsSearch = Observation.where(struct={'based-on': svcreq.id})
    listObsEkg = obsSearch.perform_resources(serverFhir.server)

    for obsEkg in listObsEkg:
        print(f'Observation ID: {obsEkg.id}, Status: {obsEkg.status}')

obsEkgExample = listObsEkg[0]

# FHIR Observation Resource - Example Data
ekg_data = obsEkgExample.component

# Function to process sampled data
def process_sampled_data(data_str, origin, factor):
    data_points = np.array(list(map(decimal.Decimal, data_str.split(' '))))
    processed_data = (data_points - origin) * factor
    return processed_data

# Function to plot EKG graph
def plot_ekg(ekg_data):
    plt.figure(figsize=(12, 40))
    iSubplotRows = 6
    lambdaGetCols = lambda x: x // iSubplotRows if x % iSubplotRows == 0 else x // iSubplotRows + 1
    iSubplotsCols = lambdaGetCols(len(ekg_data))
    # 創造一個兩欄的網格
    fig, axs = plt.subplots(iSubplotRows, iSubplotsCols, figsize=(24, 20))
    lead_names = []
    for i, (component, ax) in enumerate(zip(ekg_data, axs.T.reshape(iSubplotRows, iSubplotsCols).flat)):
        lead_name = component.code.coding[0].display
        lead_names.append(lead_name)
        origin = component.valueSampledData.origin.value
        factor = component.valueSampledData.factor
        data_str = component.valueSampledData.data

        # Process the data
        processed_data = process_sampled_data(data_str, origin, factor)
        time = np.arange(len(processed_data)) * 0.001  # period = 1ms = 0.001s

        # Plot
        ax.plot(time, processed_data,linewidth=0.5, label=lead_name)
        # 設定 x 軸和 y 軸的標籤
        ax.set_xlabel("s")
        ax.set_ylabel("mV")

        # 設定 x 軸主要刻度和次要刻度
        ax.set_xticks(np.arange(0, len(time)*0.001, 0.2))  # 主要刻度
        ax.set_xticks(np.arange(0, len(time)*0.001, 0.04), minor=True)  # 次要刻度

        # 設定 y 軸主要刻度
        ax.set_yticks(np.arange(-2.5, 2.5, 0.5))
        # 設定 y 軸次要刻度
        ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))  # 次要刻度

        # 顯示 x 軸的格線
        ax.xaxis.grid(True, color='gray')
        ax.xaxis.grid(which='minor', color='pink')
        # 顯示 y 軸的格線
        ax.yaxis.grid(True, color='gray')
        ax.yaxis.grid(which='minor', color='pink')

        ax.axhline(0, color='red', linewidth=1)
        ax.legend(loc='upper right')

    fig.suptitle("12-Lead ECG")
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

# Plot EKG
plot_ekg(ekg_data)

