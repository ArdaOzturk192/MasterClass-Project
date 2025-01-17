# MasterClass Projesi

Bu proje grafana üzerindeki tüm dashboardlarda bulunan datasourceları uyumlu şekilde farklı tipteki datasourcelara çevirmekle beraber bir kaç yan işlevin localhost:8090/swagger-ui.html üzerinden API olarak sunulmasını hedefler.


## Özellikler

- Tüm Grafana dashboard'larını almak
- Belirli bir dashboard'ın ID'sine göre detaylarını almak
- Tüm Grafana datasource'ları almak
- Belirli bir datasource'un ID'sine göre detaylarını almak
- Grafana'daki dashboard'larda bulunan datasource'ları uyumlu şekilde farklı tipteki datasourceları'na çevirmek
- Daha detaylı bilgi için requirements.md dosyasına bakın

## Gereksinimler

- Grafana: Elasticsearch ve OpenSearch datasource'larının başarıyla bağlanması ve dashboardlar oluşturulması gereklidir. 
- Elasticsearch: Dummy index ve veriler oluşturulması gereklidir. [Elasticsearch API document](https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html)
- OpenSearch : Dummy index ve veriler oluşturulması gereklidir. [OpenSearch API document](https://opensearch.org/docs/latest/api-reference/)
- Python 3+
- Flask, flask-swagger-ui: 
   ```bash
   pip install flask flask-swagger-ui

## Kurulum

- Grafana kurulum linki: https://grafana.com/grafana/download
- Elasticsearch kurulum linki: https://www.elastic.co/downloads/elasticsearch
- OpenSearch kurulum linki: https://opensearch.org/downloads.html

## Kullanım

- API (app.py) çalıştırın. Uygulama http://localhost:8090/swagger-ui.html adresinden Swagger ile erişilebilir olacaktır.

## Proje Sahibi
Arda Öztürk
