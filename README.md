# MasterClass Projesi

Bu proje grafana üzerindeki tüm dashboardlarda bulunan datasourceları uyumlu şekilde farklı tipteki datasourceları çevirmeyi hedefler.

Proje kapsamında tüm dashboardlardaki elasticsearch datasourceları opensearch datasource'una uyumlu çalışır hale çevrilmesine dair yazılacak akış yeterli olacaktır. İsterler bölümünde bulunan metodların oluşturulup localhost:8090 üzerinden API olarak sunulması gereklidir.


## Özellikler

- Tüm Grafana dashboard'larını almak
- Belirli bir dashboard'ın ID'sine göre detaylarını almak
- Tüm Grafana datasource'ları almak
- Belirli bir datasource'un ID'sine göre detaylarını almak
- Grafana'daki dashboard'larda bulunan datasource'ları uyumlu şekilde farklı tipteki datasourceları'na çevirmek

## Gereksinimler

- Grafana: Elasticsearch ve OpenSearch datasource'larının başarıyla bağlanması ve dashboardlar oluşturulması gereklidir. 
- Elasticsearch: Dummy index ve veriler oluşturulması gereklidir. Ref: https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html
- OpenSearch : Dummy index ve veriler oluşturulması gereklidir. Ref: https://opensearch.org/docs/latest/api-reference/
- Python 3+
- Flask
- Flasgger

## Kurulum

Grafana kurulum linki: https://grafana.com/grafana/download
Elasticsearch kurulum linki: https://www.elastic.co/downloads/elasticsearch
OpenSearch kurulum linki: https://opensearch.org/downloads.html

## Kullanım

Api yi (app.py) çalıştırın. Uygulama http://localhost:8090/apidocs adresinden Swagger ile erişilebilir olacaktır.
