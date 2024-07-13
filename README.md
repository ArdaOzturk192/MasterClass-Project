Proje özeti:

1: Grafana kurulumu yapıldı, python ile Grafana Api kullanım testleri yapıldı.
  Grafana'nın kendi sitesinden kurulum dosyasını indirip kurulumu gerçekleştirdim. Ardından internetten araştırıp Grafana Api kullanımını öğrendim ve örnek bir python kodu ile Grafana Api bağlantısını gerçekleştirdim.

2: ElasticSearch kurulumu yapıldı ve dummy veri oluşturuldu.
  ElasticSearch'ün kendi sitesinden indirip kurulumunu internetten araştırarak gerçekleştirdim. Cmd üzerinden kendime username ve password tanımladım, kullanım kolaylığı açısından bilgisayara windows hizmeti olarak da kurdum.
  Ardından Postman üzerinden Post request ile bir index oluşturup dummy veri ekledim ve Get request göndererek verileri görüntüledim.

3: OpenSearch kurulumu yapıldı ve dummy veri oluşturuldu.
  Opensearch'ün kendi sitesinden indirip kurulumunu internette az video kaynağı bulunmasından ötürü biraz zor bir şekilde gerçekleştirdim. Bazı güvenlik kısımlarında error aldığımdan dosyalardan güvenlikle alakalı bir şeyi deaktif edip öyle kurulumu gerçekleştirdim.
  Ardından Postman üzerinden Post request ile bir index oluşturup dummy veri ekledim ve Get request göndererek verileri görüntüledim.

4: ElasticSearch ile Grafana bağlantısı kuruldu, ElasticSearch'e görselleştirmeye daha uygun daha çok veri eklendi ve Grafana da dashboard oluşturuldu.
  Grafana'ya ElasticSearch bağlarken önce Authentication kısmını gözden kaçırdığım için bir süre o hatayla uğraştım sonrasında da tls certificate sorunuyla karşılaştım onu da araştırıp Skip TLS certificate validation ayarı ile düzelttim.
  Sonrasında önceden eklediğim dummy verinin görselleştirmeye uygun olmadığını fark edip farklı bir index oluşturup sayısal veriler oluşturdum ve ardından Grafana'da dashboard oluşturup verilerimi görebildim.

5: OpenSearch ile Grafana bağlantısı kurulacak.


