document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('getTokenButton').addEventListener('click', async function() {
        try {
            const tokenEndpoint = 'http://172.18.0.58:8080/realms/mitw/protocol/openid-connect/token';


            const response = await fetch(tokenEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    grant_type: 'client_credentials',
                    client_id: 'fhir-basic',
                    client_secret: 'UPa9VGhlwrInNup2W8PBldrxanWWsKW4'
                })
            });


            if (!response.ok) {
                throw new Error('這是錯誤訊息');
            }

            const data = await response.json();

            const token = data.access_token;

            document.getElementById('result').textContent = `TOKEN是: ${token}`;
        } catch (error) {
            console.error('TOKEN沒拿到:', error);
            document.getElementById('result').textContent = `TOKEN沒拿到: ${error.message}`;
        }
    });
});