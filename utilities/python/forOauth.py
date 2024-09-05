import requests

def get_token():

    url = "http://172.18.0.58:8080/realms/mitw/protocol/openid-connect/token"
    # url = "http://220.128.182.166/realms/medical-server/protocol/openid-connect/token"
    payload = {
        'grant_type': 'client_credentials',
        'client_id': 'fhir-basic',
        'client_secret': 'UPa9VGhlwrInNup2W8PBldrxanWWsKW4'
    }

    response = requests.post(url, data=payload, timeout=30)

    if response.status_code == 200:

        token_data = response.json()
        # print(token_data)
        print("Token:", token_data['access_token'])

        token_data = response.json()['access_token']
        print(token_data)
        # print("Token:", token_data['access_token'])
        return token_data

    else:
        print(f"Failed to get token. Status code: {response.status_code}")
        print("Response:", response.text)


def getSessionWithToken():
    # 取 token
    sToken = get_token()
    # 設定新的 header ，並且綁入 Bearer token
    dictHeaders = {
        'Authorization': f'Bearer {sToken}',
        'Content-Type': 'application/json'
    }
    # 形成新的 session
    sessionAuthored = requests.Session()
    # 更新 header
    sessionAuthored.headers.update(dictHeaders)
    return sessionAuthored


if __name__ == "__main__":

    current_token = get_token()
    # print(current_token)
    # get_access_token(current_token)