from grafana_api import GrafanaAPI
import json
from concurrent.futures import ThreadPoolExecutor
from functools import partial
 
def search_dash(dashboard, api, search_query):
    # Bu kısmı genelleştirmek istiyoruz
    dash_json = json.dumps(api.get_dashboard_by_uid(dashboard['uid']))
    search_query_json = json.dumps(search_query['datasource'])
 
    if search_query_json in dash_json:
        return dash_json
 
def main():
    # Grafana API kendi yazdığımız bir kütüphane. Grafana HTTP API'sindeki en çok kullandığımız
    # bütün endpointlerin önünde bir katman gibi düşünelebilir.
    api = GrafanaAPI('https://<grafana_url>', '<secret_reducted>', False)
 
    data_sources = api.get_all_datasources()
    migrate_ready_data_sources = [data_source for data_source in data_sources if data_source['type'] == 'elasticsearch' and data_source['name'].startswith('LogLake')]
 
    # Eskiden elasticsearch tipinde ve LogLake projesine bağlı olan datasourceları
    # kopyalayıp, sonuna -2 ekleyip yeniden yaratıyoruz.
    for migrate_data_source in migrate_ready_data_sources:
        api.create_datasource(
            f"{migrate_data_source['name']}-2",
            'grafana-opensearch-datasource',
            'https://<datasource_url>:9200',
            additional_data={
                "basicAuth": True,
                "basicAuthUser": "<ad_user_reducted>",
                "secureJsonData": {
                    "basicAuthPassword": "<secret_reducted>"
                },
                "jsonData": {
                    "maxConcurrentShardRequests": 5,
                    "timeField": "@timestamp",
                    "database": migrate_data_source['database'],
                    "version": "2.15.0",
                    "flavor": "opensearch"
                }
            })
 
    dashboards = api.get_all_dashboards()
 
    search_query = {
        "datasource": {
        "type": "elasticsearch",
        "uid": "<uid_reducted>"
      }
    }
 
    partial_search_dash = partial(search_dash, api=api, search_query=search_query)
 
    # İçinde search_query dictionary'si geçen parçaların olduğu dashboardları belirliyoruz
    with ThreadPoolExecutor(max_workers=10) as executor:
        result = executor.map(partial_search_dash, dashboards)
 
    found_dashboards = [elem for elem in result if elem is not None]
 
    # Devamını henüz yazmadık.
 
if __name__ == '__main__':
    main()
