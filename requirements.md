
# Master Project

Bu proje grafana üzerindeki tüm dashboardlarda bulunan datasourceları uyumlu şekilde farklı tipteki datasourceları çevirmeyi hedefler. 

Proje kapsamında tüm dashboardlardaki elasticsearch datasourceları opensearch datasource'una uyumlu çalışır hale çevrilmesine dair yazılacak akış yeterli olacaktır. İsterler bölümünde bulunan metodların oluşturulup **localhost:8090** üzerinden API olarak sunulması gereklidir.

## 💬 Genel Bilgiler

◼️ Dil sınırlaması bulunmamaktadır. 

◼️ Local veya docker üzerinden Grafana , Elasticsearch ve Opensearch kurulması gereklidir.

◼️ Elasticsearch ve Opensearch üzerinde dummy index ve veri oluşturulması gereklidir.

◼️ Grafana içinde en az 3 adet olacak şekilde datasource'u elasticsearch seçilen örnek dashboardların oluşturulması gereklidir.

◼️ Swagger implementasyonu yapılarak,  isterlerde bulunan methodların localhost:8090/swagger-ui.html üzerinden sunulması gereklidir.

## Teknoloji Kurulum Linkleri

◼️ https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/ 

◼️ https://www.elastic.co/downloads/elasticsearch

◼️ https://opensearch.org/versions/opensearch-2-15-0.html

◼️ https://grafana.com/get/ 

◼️ https://pypi.org/project/swagger-ui-py/



## İsterler

#### Get all dashboards

```http
  GET /api/getDashboards
```

Grafana API kullanarak sistemdeki tüm dashboard listesini döndürür.

Ref: https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/




#### Get Dashboard By Id

```http
  GET /api/getDashboard/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of dashboard to fetch |


Grafana API kullanarak sistemdeki parametre olarak girilen {id} ye ait dashboard sonucunu döndürür.

Ref: https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/


#### Get all datasources

```http
  GET /api/getDatasources
```

Grafana API kullanarak sistemdeki tüm datasource listesini döndürür.

Ref: https://grafana.com/docs/grafana/latest/developers/http_api/data_source/




#### Get Datasource By Id

```http
  GET /api/getDatasource/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of datasource to fetch |


Grafana API kullanarak sistemdeki parametre olarak girilen {id} ye ait datasource sonucunu döndürür.

Ref: https://grafana.com/docs/grafana/latest/developers/http_api/data_source/



#### Migrate Datasource to Another Datasource

```http
  GET /api/migrate/{from}/{to}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `from`      | `string` | **Required**. type of from datasource to fetch |
| `to`      | `string` | **Required**. type of to datasource to fetch |


Ex: GET api/migrate/ELASTIC/OPENSEARCH 

Grafana API kullanarak sistemdeki parametre olarak girilen {from} ye ait datasourceların bağımlı olduğu dashboardların datasource tipini {to} ya başarılı şekilde değiştirir.

Ref: https://grafana.com/docs/grafana/latest/developers/http_api/data_source/





## Proje Kazanımları / Teknoloji Yığını

REST API, Grafana, Grafana API, Opensearch, Opensearch API, Swagger 


## Mentör
17/07/2024 

Fatih Yıldızlı

