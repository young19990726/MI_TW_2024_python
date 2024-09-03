from requests import get, RequestException
import json

# Function to get ServiceRequest by code
def get_svc_req(code: str):
    """
    根据提供的代码（code）从 FastAPI 服务中获取 ServiceRequest 数据。

    :param code: 需要查询的 ServiceRequest 的代码
    :return: 返回包含 ServiceRequest 数据的 JSON 响应
    """
    url = f"http://localhost:8000/api/servicerequest/{code}"

    try:
        response = get(url)

        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            return response.json()
        
        else:
            print(f"Failed to retrieve serviceRequest: {response.text}")
    
    except RequestException as e:
        print(str(e))

# Function to get Observation by ServiceRequest ID
def get_obs(svc_id: str):
    """
    根据提供的 ServiceRequest ID 从 FastAPI 服务中获取 Observation 数据。

    :param svc_id: 需要查询的 ServiceRequest 的 ID
    :return: 返回包含 Observation 数据的 JSON 响应
    """
    url = f"http://localhost:8000/api/observation/{svc_id}"

    try:
        response = get(url)

        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            return response.json()
        
        else:
            print(f"Failed to retrieve observation: {response.text}")
    
    except RequestException as e:
        print(str(e))

if __name__ == "__main__":
    
    ServiceRequest_data = get_svc_req('3130004')
    
    # ServiceRequest_data = get_svc_req('3998005')

    if ServiceRequest_data:  
        id = ServiceRequest_data[0]['id']
        get_obs(id)