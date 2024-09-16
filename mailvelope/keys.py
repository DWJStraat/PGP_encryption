import requests


def upload_public_key_to_mailvelope(public_key, email_address):
    url = "http://keys.mailvelope.com/api/v1/keys"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_MAILVOLPE_API_KEY'
    }
    data = {
        "key": public_key,
        "email": email_address
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def download_public_key_from_mailvelope(email_address):
    url = f"https://keys.mailvelope.com/api/v1/key?email={email_address}"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['publicKeyArmored']
