import requests
import json

def get_dashboard(api_url, token):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        print("Dashboard data received successfully!")
        return response.json()
    else:
        print(f"Hata: {response.status_code}")
        print(response.text)
        return None

def update_dashboard(api_url, token, dashboard_data):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    
    data = {
        "dashboard": dashboard_data["dashboard"],
        "folderId": dashboard_data["meta"]["folderId"],
        "message": "Updated dashboard title",
        "overwrite": True
    }
    
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print("Dashboard updated successfully!")
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def main():
    # API endpointi
    grafana_url = 'http://localhost:3000/'
    api_token = 'glsa_icqAfZecHkWTpahAtQ7XuKaTaFJKJhAs_c3b94302'
    elasticsearch_uid = "edrny9vqcmz9cf"
    opensearch_uid = "ddrxdjvgugs1se"
    
    """
    grafana_url = input("Please enter the Grafana base URL: ")
    api_token = input("Please enter the Grafana API token: ")
    elasticsearch_uid = input("Please enter the Elasticsearch dashboard UID: ")
    opensearch_uid = input("Please enter the OpenSearch dashboard UID: ")
    """
    # Dashboard endpoints
    elasticsearch_dashboard_url = grafana_url + "api/dashboards/uid/" + elasticsearch_uid
    opensearch_dashboard_url = grafana_url + "api/dashboards/uid/" + opensearch_uid

    elasticsearch_dashboard_data = get_dashboard(elasticsearch_dashboard_url, api_token)
    opensearch_dashboard_data = get_dashboard(opensearch_dashboard_url, api_token)
    
     # Update titles
    if elasticsearch_dashboard_data:
        elasticsearch_dashboard_data['dashboard']['title'] = "Updated Elasticsearch Dashboard Title"
        update_dashboard(grafana_url + 'api/dashboards/db', api_token, elasticsearch_dashboard_data)

    if opensearch_dashboard_data:
        opensearch_dashboard_data['dashboard']['title'] = "Updated OpenSearch Dashboard Title"
        update_dashboard(grafana_url + 'api/dashboards/db', api_token, opensearch_dashboard_data)

    # Print dashboards
    if elasticsearch_dashboard_data:
        print(json.dumps(elasticsearch_dashboard_data, indent=4, ensure_ascii=False))
        print("\n--------------------\n")

    if opensearch_dashboard_data:
        print(json.dumps(opensearch_dashboard_data, indent=4, ensure_ascii=False)) 

if __name__ == '__main__':
    main()
