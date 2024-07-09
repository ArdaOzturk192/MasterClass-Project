import requests

def get_datasource(api_url, token):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        print("Successful!")
        return response.json()
    else:
        print(f"Hata: {response.status_code}")
        print(response.text)
        return None

def main():
    # API endpointi
    grafana_url = 'http://localhost:3000/api/datasources'
    
    api_token = 'glsa_icqAfZecHkWTpahAtQ7XuKaTaFJKJhAs_c3b94302'
    
    datasource_data = get_datasource(grafana_url, api_token)
    
    if datasource_data:
        print(datasource_data)

if __name__ == '__main__':
    main()
