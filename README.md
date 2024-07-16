Proje özeti:

1: Grafana kurulumu yapıldı, python ile Grafana Api kullanım testleri yapıldı.
  Grafana'nın kendi sitesinden kurulum dosyasını indirip kurulumu gerçekleştirdim. Ardından internetten araştırıp Grafana Api kullanımını öğrendim ve örnek bir python kodu ile Grafana Api bağlantısını gerçekleştirdim.

2: Elasticsearch kurulumu yapıldı ve dummy veri oluşturuldu.
  ElasticSearch'ün kendi sitesinden indirip kurulumunu internetten araştırarak gerçekleştirdim. Cmd üzerinden kendime username ve password tanımladım, kullanım kolaylığı açısından bilgisayara windows hizmeti olarak da kurdum.
  Ardından Postman üzerinden Post request ile bir index oluşturup dummy veri ekledim ve Get request göndererek verileri görüntüledim.

3: OpenSearch kurulumu yapıldı ve dummy veri oluşturuldu.
  Opensearch'ün kendi sitesinden indirip kurulumunu internette az video kaynağı bulunmasından ötürü biraz zor bir şekilde gerçekleştirdim. Bazı güvenlik kısımlarında error aldığımdan dosyalardan güvenlikle alakalı bir şeyi deaktif edip öyle kurulumu gerçekleştirdim.
  Ardından Postman üzerinden Post request ile bir index oluşturup dummy veri ekledim ve Get request göndererek verileri görüntüledim.

4: Elasticsearch ile Grafana bağlantısı kuruldu, Elasticsearch'e görselleştirmeye daha uygun daha çok veri eklendi ve Grafana da dashboard oluşturuldu.
  Grafana'ya Elasticsearch bağlarken önce Authentication kısmını gözden kaçırdığım için bir süre o hatayla uğraştım sonrasında da tls certificate sorunuyla karşılaştım onu da araştırıp Skip TLS certificate validation ayarı ile düzelttim.
  Sonrasında önceden eklediğim dummy verinin görselleştirmeye uygun olmadığını fark edip (@timestamp değeri yoktu) farklı bir index oluşturup sayısal veriler oluşturdum ve ardından Grafana'da dashboard oluşturup verilerimi görebildim.

5: OpenSearch ile Grafana bağlantısı kuruldu, OpenSearch'e görselleştirmeye daha uygun daha çok veri eklendi ve Grafana da dashboard oluşturuldu.
  Grafana'ya OpenSearch bağlarken data sources kısmında bulamadım, biraz araştırdıktan sonra indirmem gerektiğini fark ettim ve indirdikten sonraki kısım Elasticsearch'e göre fazlasıyla kolay oldu sadece url ve index ismi yazmam yeterli oldu. Elasticsearch için eklediğim    verilerin benzerini OpenSearch'e de ekledim ve ve Grafana üzerinden dashboard oluşturarak onları da görüntüledim.


