import requests

def get_token():

    url = "http://172.18.0.58:8080/realms/mitw/protocol/openid-connect/token"
    # url = "http://220.128.182.166/realms/medical-server/protocol/openid-connect/token"
    payload = {
        'grant_type': 'client_credentials',
        # 'client_id': 'yenyen1007',
        # 'client_secret': 'qwertyu'
        'client_id': 'fhir-twcore-0.2.2',
        'client_secret': '6ML54AFeVgMLoRe7cKqshc3171UmD0CI'
    }

    response = requests.post(url, data=payload, timeout=30)

    if response.status_code == 200:
        token_data = response.json()['access_token']
        print(token_data)
        # print("Token:", token_data['access_token'])
        return token_data
    else:
        print(f"Failed to get token. Status code: {response.status_code}")
        print("Response:", response.text)


if __name__ == "__main__":

    current_token = get_token()
    get_access_token(current_token)