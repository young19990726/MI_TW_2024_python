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
        token_data = response.json()
        print(token_data)
        # print("Token:", token_data['access_token'])
        return token_data['access_token']
    else:
        print(f"Failed to get token. Status code: {response.status_code}")
        print("Response:", response.text)


def get_access_token(auth_code):

    token_url = "http://172.18.0.58:8080/realms/mitw/protocol/openid-connect/auth"
    client_id = "fhir-twcore-0.2.2"
    client_secret = "6ML54AFeVgMLoRe7cKqshc3171UmD0CI"
    redirect_uri = "http://172.18.0.53:10002/oauth2/callback"


    payload = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'code': auth_code,
        'redirect_uri': redirect_uri
    }

    try:

        response = requests.post(token_url, data=payload, timeout=30)


        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data.get('access_token')
            print("Access Token:", access_token)
            return access_token
        else:
            print(f"Failed to get access token. Status code: {response.status_code}")
            print("Response:", response.text)
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None





if __name__ == "__main__":

    current_token = get_token()
    get_access_token(current_token)