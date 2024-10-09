# <h1 align="center">HasBogor</h1>

<p align="center">
    <img src="logo.png" alt="HasBogor" width="300"> <!-- Atur ukuran sesuai kebutuhan -->
</p>

## Anggota Kelompok
- **Akmal Nabil Fikri** - 2306152084
- **Rebecca Zaneta Octoria Hutajulu** - 2306275065
- **Michael Ignasius** - 2306259950
- **Ivan Jehuda Angi** - 2306152222
- **Ismail Yanuar Anwas** - 2306245781
- **Widya Mutia Ichsan** - 2306165912

## Table of Contents
- [Deskripsi Aplikasi](#deskripsi-aplikasi)
- [Daftar Modul yang Akan Diimplementasikan](#daftar-modul-yang-akan-diimplementasikan)
- [Sumber Initial Dataset Kategori Utama Produk](#sumber-initial-dataset-kategori-utama-produk)
- [Promo](#promo)
- [Role atau Peran Pengguna Beserta Deskripsinya](#role-atau-peran-pengguna-beserta-deskripsinya)
- [Desain dan Struktur Aplikasi](#desain-dan-struktur-aplikasi)
  - [USER](#USER)
  - [ADMIN](#admin)

## Deskripsi Aplikasi
**HasBogor** adalah sebuah aplikasi berbasis web yang bertujuan untuk memenuhi kebutuhan wisatawan dan masyarakat dalam menemukan produk oleh-oleh khas Bogor dengan lebih mudah dan efisien. Aplikasi ini menyediakan pusat informasi dan transaksi untuk oleh-oleh khas Bogor, termasuk makanan khas, kerajinan tangan, dan banyak lagi. Pengguna dapat memesan produk secara <i>online</i> serta berinteraksi dengan komunitas melalui ulasan dan rekomendasi produk. Aplikasi ini berawal ketika sekelompok pelajar yang berkunjung ke Bogor ingin mencari sesuatu untuk mengenang pengalaman mereka. Setelah sepakat untuk mencari beberapa oleh-oleh yang dapat dibawa kembali, mereka menemukan sebuah masalah, tidak ada toko terdekat yang menjual oleh-oleh di daerah mereka saat itu. Setelah berputar dan mengunjungi area sekitar, mereka akhirnya menemukan toko cendera mata yang mereka cari. Mengingat pengalaman tersebut, mereka memutuskan untuk membuat sebuah aplikasi yang akan membantu wisatawan lainnya dalam menemukan toko oleh-oleh terdekat sekaligus dapat memesan secara <i>online</i>.

### Kebermanfaatan Aplikasi
- Mendukung pengrajin lokal dalam menjual produk mereka.
- Meningkatkan akses wisatawan ke produk-produk khas Bogor.
- Mempermudah transaksi dan memperkaya pengalaman belanja oleh-oleh.
- Meningkatkan volume transaksi oleh-oleh di Kota Bogor.

## Daftar Modul yang Akan Diimplementasikan
| **Modul**            | **Deskripsi**                                                                            |
|----------------------|------------------------------------------------------------------------------------------|
| Autentikasi          | Mengelola login dan registrasi pengguna, termasuk pengelolaan password.                  |
| Produk               | Menampilkan daftar produk, detail produk, dan fitur pencarian.                           |
| Keranjang            | Menyimpan produk yang ditambahkan ke keranjang (semacam wishlist)                        |
| Ulasan               | Pengguna dapat memberikan ulasan dan rating pada produk.                                 |
| Promo                | Mengolah dan menampilkan promo dan diskon.                                               |
| Rekomendasi          | Memberikan rekomendasi produk kepada pengguna.                                           |
| Inventory Management | Mengelola barang yang dijual toko.                                                       |
| Pembayaran           | Berupa layanan yang memungkinkan pembeli melakukan pembayaran secara online (dummy data) |


## Sumber Initial Dataset Kategori Utama Produk
Pada sumber dataset awal ini, kami mengumpulkan informasi melalui metode manual


| **Kategori Produk** | **Deskripsi**                                                               | **Sumber Data**                     |
|---------------------|-----------------------------------------------------------------------------|-------------------------------------|
| Makanan             | Berbagai makanan khas Bogor seperti brownies, dodol, dan keripik.           | [Dataset Makanan](#dataset-makanan) |
| Souvenir            | Kerajinan tangan unik sebagai kenang-kenangan.                              | [Dataset Souvenir](#dataset-souvenir)-                                   |


---
### Dataset Makanan
| No | Nama Oleh-oleh         | Kategori        | Harga (Rp)          | Deskripsi                                                               | Referensi                                                             |
|----|------------------------|-----------------|---------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------|
| 1  | Asinan Bogor           | Makanan         | 25.000 - 50.000     | Campuran buah dan sayur dalam kuah asam manis pedas, khas Bogor         | [pergi kuliner](https://pergikuliner.com/restaurants/bogor/asinan-asli-bogor-bogor-tengah)       |
| 2  | Roti Unyil Venus       | Makanan         | 15.000 - 30.000     | Roti mini dengan berbagai varian rasa, populer sejak 1978               | [pergi kuliner](https://pergikuliner.com/restaurants/bogor/roti-unyil-venus-bogor-timur-3)       |
| 3  | Talas Bogor            | Makanan         | 20.000 - 40.000     | Umbi-umbian khas Bogor yang diolah menjadi berbagai makanan             | [superkue](https://superkue.com/v2/?page=category&cat=6)            |
| 4  | Makaroni Ngehe         | Makanan Ringan  | 15.000 - 25.000     | Makaroni kering dengan bumbu pedas khas                                 | [pergi kuliner](https://pergikuliner.com/restaurants/makaroni-ngehe-tanah-sareal/menus)          |
| 5  | Lapis Talas Bogor      | Kue             | 50.000 - 100.000    | Kue lapis dengan campuran talas, lembut dan gurih                       | [superkue](https://superkue.com/v2/?page=category&cat=6)            |
| 6  | Dodol Talas            | Makanan         | 30.000 - 60.000     | Makanan manis dan kenyal berbahan dasar talas                           | [lazada](https://www.lazada.co.id/tag/dodol-talas-bogor/)            |
| 7  | Pie Apel Bogor         | Kue             | 40.000 - 80.000     | Pie dengan isian apel segar, perpaduan manis dan asam                   | [pergikuliner](https://pergikuliner.com/restaurants/bogor/pia-apple-pie-bogor-tengah)            |
| 8  | Bolu Lapis Sangkuriang | Kue             | 60.000 - 120.000    | Bolu berlapis dengan tekstur lembut dan rasa yang khas                  | [lapisbogor](https://lapisbogor.co.id/)                             |
| 9  | Kue Soes Merdeka       | Kue             | 30.000 - 50.000     | Kue sus dengan varian isi yang beragam                                  | [pergikuliner](https://pergikuliner.com/restaurants/soes-merdeka-bogor-utara/gallery/1417446)    |
| 10 | Keripik Talas          | Makanan Ringan  | 20.000 - 40.000     | Keripik renyah berbahan dasar talas                                     | [Tokopedia Blog](https://www.tokopedia.com/find/keripik-talas-bogor) |
| 11 | Tahu Susu Lembang      | Makanan         | 25.000 - 50.000     | Tahu dengan tekstur lembut dan rasa susu yang khas                      | [shopee](https://shopee.co.id/list/Tahu/Susu/Lembang)                |
| 12 | Brownies Kukus Amanda  | Kue             | 40.000 - 80.000     | Brownies kukus dengan berbagai varian rasa                              | [pergikuliner](https://pergikuliner.com/restaurants/bogor/amanda-brownies-kukus-bogor-utara)    |
| 13 | Bakso Aux              | Makanan         | 30.000 - 60.000     | Bakso dengan tekstur kenyal dan rasa yang khas                          | [Gotravelly](https://gotravelly.com/blog/oleh-oleh-khas-bogor/)      |
| 14 | Cakwe Renata           | Makanan         | 15.000 - 30.000     | Cakwe dengan tekstur renyah dan bumbu khas                              | [gofood](https://gofood.co.id/jakarta/restaurant/cakwe-bogor-jambu-dua-3d2f417f-6c56-4c18-b542-f62a0f7179e9) |
| 15 | Emping Melinjo         | Makanan Ringan  | 20.000 - 40.000     | Keripik dari biji melinjo dengan rasa gurih khas                        | [bobobox blog](https://bobobox.com/blog/oleh-oleh-khas-bogor-yang-tahan-lama/)                   |
| 16 | Es Pala Bogor          | Minuman         | 10.000 - 20.000     | Minuman segar khas Bogor dengan ekstrak buah pala                       | [kuliner](https://rri.co.id/kuliner/651563/sensasi-manis-hangat-es-pala-bogor)                  |
| 17 | Pancake Durian D'Linow | Kue             | 50.000 - 100.000    | Pancake dengan isian durian asli                                        | [pergikuliner](https://pergikuliner.com/restaurants/pancake-durian-d-dan-d-bogor-utara/menus)   |
| 18 | Kue Lapis Talas Sari   | Kue             | 60.000 - 120.000    | Kue lapis premium dengan campuran talas Bogor                           | [Jawa Pos](https://www.jawapos.com/jpg-today/01/353456/5-oleh-oleh-khas-bogor-yang-wajib-dibeli) |
| 19 | Brownis Talas          | Makanan         | 25.000 - 50.000     | Camilan manis khas yang menggabungkan cita rasa cokelat premium dengan sentuhan unik dari talas | [traveloka](https://www.traveloka.com/id-id/explore/culinary/12-oleh-oleh-khas-bogor-yang-selalu-ramai-pengunjung/15656) |
| 20 | Kue Satu               | Kue             | 20.000 - 40.000     | Kue tradisional berbahan dasar kacang hijau                             | [shopee](https://shopee.co.id/Kue-Satu-asli-Kacang-Hijau-khas-Bogor-i.133089470.23238265659)   |
| 21 | Sambal Teri Bawang     | Makanan         | 30.000 - 60.000     | Sambal dengan campuran teri                                             | [tokopedia](https://www.tokopedia.com/sambelibukribo/sambal-teri-bawang-sambal-ibu-kribo-khas-bogor?utm_source=google&utm_medium=organic&utm_campaign=pdp-seo) |
| 22 | Mochi Talas            | Kue             | 25.000 - 50.000     | Kue mochi dengan isian talas khas Bogor                                 | [shopee](https://shopee.co.id/Mochi-Talas-Khas-Bogor-Sangkuriang-i.37756556.9644101050)         |
| 23 | Kacang Bogor           | Makanan         | 20.000 - 40.000     | Kacang Bogor                                                            | [detik](https://www.detik.com/jabar/wisata/d-6871479/10-oleh-oleh-khas-bogor-yang-terkenal-2023-cocok-dibawa-pulang) |
| 24 | Ketan Srikaya Pandan   | Makanan         | 25.000 - 50.000     | Makanan ketan srikaya dengan campuran pandan                            | [tokopedia](https://www.tokopedia.com/amantasegar/ketan-srikaya-pandan-asli-original-empuk-oleh-oleh-bogor-terlaris-enak) |
| 25 | Toge Goreng            | Makanan         | 15.000 - 30.000     | Hidangan khas Bogor dengan toge, mi, dan kuah kacang                    | [detikfood](https://food.detik.com/info-kuliner/d-5371496/kuliner-bogor-5-rekomendasi-toge-goreng-untuk-mencoba) |
| 26 | Cendol Bogor           | Minuman         | 10.000 - 20.000     | Minuman manis dan segar dengan campuran cendol                          | [detik](https://www.detik.com/jabar/wisata/d-6871479/10-oleh-oleh-khas-bogor-yang-terkenal-2023-cocok-dibawa-pulang) |
| 27 | Pudding Lapis Bogor    | Kue             | 40.000 - 80.000     | Puding berlapis dengan berbagai varian rasa                             | [gofood](https://gofood.co.id/jakarta/restaurant/pudding-lapis-bogor)                                  |
| 28 | Lempung Cianjur        | Makanan         | 30.000 - 60.000     | Lempung khas Cianjur, enak dan kenyal                                   | [Tokopedia](https://www.tokopedia.com/find/lempung)                 |
| 29 | Coto Makassar          | Makanan         | 40.000 - 80.000     | Hidangan berkuah yang kaya rempah dan rasa                              | [Bobobox](https://bobobox.com/blog/20-oleh-oleh-khas-bogor/)          |
| 30 | Kue Cubir              | Kue             | 25.000 - 50.000     | Kue cubir dengan cita rasa unik dan lezat                               | [Tokopedia](https://www.tokopedia.com/find/kue-cubir)              |
| 31 | Pie Susu Bogor         | Kue             | 25.000 - 50.000     | Pie dengan isian susu yang lembut                                       | [Tokopedia](https://www.tokopedia.com/find/pie-susu)                |
| 32 | Keripik Singkong       | Makanan Ringan  | 20.000 - 40.000     | Keripik renyah dari singkong                                            | [Tokopedia](https://www.tokopedia.com/find/keripik-singkong)       |
| 33 | Kerupuk Kulit          | Makanan Ringan  | 20.000 - 40.000     | Kerupuk dari kulit ikan yang gurih                                      | [Tokopedia](https://www.tokopedia.com/find/kerupuk-kulit)          |
| 34 | Pudding Karamel        | Kue             | 25.000 - 50.000     | Puding karamel yang lembut dan enak                                     | [Tokopedia](https://www.tokopedia.com/find/pudding-karamel)        |
| 35 | Roti Tawa              | Makanan         | 10.000 - 20.000     | Roti tawa khas Bogor yang enak                                          | [Tokopedia](https://www.tokopedia.com/find/roti-tawa)              |
| 36 | Keripik Pisang         | Makanan Ringan  | 20.000 - 40.000     | Keripik dari pisang yang renyah                                         | [Tokopedia](https://www.tokopedia.com/find/keripik-pisang)         |
| 37 | Kue Cubir Beras Ketan  | Kue             | 25.000 - 50.000     | Kue cubir dari beras ketan yang kenyal                                  | [Tokopedia](https://www.tokopedia.com/find/kue-cubir-beras-ketan)  |
| 38 | Kue Bolu Susu          | Kue             | 30.000 - 60.000     | Bolu susu dengan rasa yang lembut                                       | [Tokopedia](https://www.tokopedia.com/find/kue-bolu-susu)          |
| 39 | Kue Roti Lapis         | Kue             | 40.000 - 80.000     | Kue lapis dengan variasi rasa yang menarik                              | [Tokopedia](https://www.tokopedia.com/find/kue-roti-lapis)         |
| 40 | Kue Talas              | Kue             | 30.000 - 60.000     | Kue dari talas yang enak dan lembut                                     | [Tokopedia](https://www.tokopedia.com/find/kue-talas)              |
| 41 | Strudel Lilit| Makanan    | 30,000-35,000       |Strudel lilit Bogor| [Shopee](https://shopee.co.id/Strudel-Lilit-Bogor-i.48225756.13137855172?xptdk=758551b4-1aa4-4958-918f-d75a3d589f45) |
| 42 | Strudel Sei Sapi| Makanan    | 35,000       |Strudel Sei Bogor| [Shopee](https://shopee.co.id/Strudel-Sei-Sapi-i.48225756.9288045737?xptdk=ba92351e-c8d5-454b-b163-472456ad095c) |
| 43 | Apple Pie| Makanan    | 63,000       |Apple Pie Medium| [pergikuliner](https://pergikuliner.com/restaurants/pia-apple-pie-bogor-tengah/menus) |
| 44 | Asinan Buah| Makanan    | 35,000       |Asinan buah segar| [pergikuliner](https://pergikuliner.com/restaurants/asinan-sedap-gedung-dalam-bogor-timur/menus) |
| 45 | Asinan Sayur| Makanan    | 35,000       |Asinan sayur segar| [pergikuliner](https://pergikuliner.com/restaurants/asinan-sedap-gedung-dalam-bogor-timur/menus) |
| 46 | Asinan Campur| Makanan    | 35,000       |Asinan campuran buah dan sayur segar| [pergikuliner](https://pergikuliner.com/restaurants/asinan-sedap-gedung-dalam-bogor-timur/menus) |
| 47 | Strudel Bogor| Makanan    | 40,000-45,000       |Strudel Bogor isi pastry dengan 6 jenis isian | [Shopee](https://shopee.co.id/Strudel-Bogor-Apel-Bakso-Banana-Sweet-Cheese-Martabak-i.48225756.759746646?xptdk=17881796-05ef-45ad-a401-3bf8a068c1b5) |
| 48 | Bika Bogor             | Kue             | 30.000 - 60.000     | Bika yang lembut, harum dan enak                                     | [Shopee](https://shopee.co.id/bikabogor)       |
| 49 | Macaroni Panggang             | Makanan             | 30.000 - 150.000     | Homemade macaroni oanggang terbaik sejak 2001              | [Shopee](https://id.shp.ee/dXvE23q)    |
| 50 | Rumah Mochibo             | Kue             | 30.000 - 50.000     | Pelopor oleh-oleh kue mochi isi buah khas Bogor                                     | [pergikuliner]| 
| 51 | Lapis Tokyo Cake            | Kue             | 30.000 - 150.000     | Cake Pertama dengan fla lembut dan rasa legit               | [Tokopedia](https://www.tokopedia.com/lapistokyocake)| 
| 52 | PapaPia            | Kue             | 50.000 - 100.000     | Pia autentik dari Kota Bogor yang sangat legendaris   | [Blibli](https://www.blibli.com/brand/papapia?srsltid=AfmBOor6qhaC442f9e_AZuchX4ZmsUlIDXFSf61fB_ApHTmMdxP2MmKi)| 
| 53 | DoughSis            | Kue             | 30.000 - 100.000     | Berbagai macam kue yang terbuat dari ubi segar    | [Grab](https://food.grab.com/id/id/restaurant/doughsis-tegallega-delivery/6-CZA3E2KXGPK2TX)| 
| 54 | Roti Roll Bogor            | Kue             | 30.000 - 110.000     | Roti lembut dengan topping melimpah!!    | [Grab](https://food.grab.com/id/en/restaurant/roti-roll-bogor-gerai-pajajaran-bogor-delivery/6-C6THSFWDCCDJSA?sourceID=20240926_090326_b36bf05a2ac5f254_MEXMPS)| 
| 55 | Chocomory            | Kue             | 40.000 - 100.000     | Pie berbagai rasa yang lembut!!    | [GoFood](https://gofood.co.id/id/jakarta/restaurant/cheesy-pie-by-chocomory-pajajaran-raya-18-5384f399-3866-4d59-9864-59228f9a1810)|
| 56 | Cokelat Bogor          | Makanan           | 25,000 - 75,000  | Cokelat khas Bogor dengan kemasan kreatif sebagai oleh-oleh wisatawan.             | [Souvenir Bogor](https://souvenirbogor.com)          |
| 57 | Kue Rangin             | Makanan           | 20,000 - 50,000  | Kue tradisional dengan kemasan menarik dan sentuhan kerajinan lokal.               | [Sentra Kerajinan Bogor](https://kerajinansentul.com)  |
| 58 | Manisan Bogor          | Makanan           | 15,000 - 45,000  | Buah lokal Bogor yang diawetkan dengan sentuhan kemasan kerajinan.                 | [Pesona Kuliner](https://pesonakulinerbogor.com)          |
---

## Dataset Souvenir
| No | Nama Oleh-oleh         | Kategori          | Harga (Rp)       | Deskripsi                                                                          | Referensi                                  |
|----|------------------------|-------------------|------------------|------------------------------------------------------------------------------------|--------------------------------------------|
| 1  | Kerajinan Anyaman Bambu| Kerajinan Tangan  | 50,000 - 150,000 | Keranjang, baki, dan perabotan rumah dari bambu buatan tangan lokal.               | [Sentra Kerajinan Sentul](https://sentulcraftcenter.com) |
| 2  | Keramik Bogor          | Kerajinan Tangan  | 100,000 - 300,000| Produk keramik seperti vas bunga dan piring dekoratif oleh pengrajin lokal.        | [Perpus Teknik](https://perpusteknik.com)           |
| 3  | Ukiran Kayu Bogor      | Kerajinan Tangan  | 75,000 - 200,000 | Ukiran kayu kecil berupa patung dan hiasan dinding, merefleksikan budaya lokal.    | [Kerajinan Tangan Bogor](https://bogorhandicrafts.com)  |
| 4  | Batik Bogor            | Tekstil           | 150,000 - 500,000| Batik khas Bogor dengan motif flora dan fauna lokal.                               | [Pesona Kerajinan Sentul](https://sentulcrafts.com) |
| 5  | Miniatur Kebun Raya    | Souvenir Edukatif | 100,000 - 250,000| Miniatur replika Kebun Raya Bogor sebagai souvenir edukatif.                       | [Handicraft Bogor](https://handicraftbogor.com)        |
| 6  | Kerajinan Kertas           | Kerajinan        | 70,000     | Kerajinan kertas handmade dengan desain unik dan kreatif                                    |                                                                           |
| 7  | Lesung Keramik             | Kerajinan        | 120,000    | Keramik tangan dengan berbagai bentuk seperti mug, vas bunga, mangkuk, dan guci            | [kumparan](https://kumparan.com/jendela-dunia/5-rekomendasi-souvenir-khas-bogor-untuk-oleh-oleh-21naUlT0k1w/full) |
| 8  | Wayang Golek               | Seni             | 150,000    | Wayang golek khas Sunda yang merupakan ikon dan ciri khas kota Bogor                       | [kumparan](https://kumparan.com/jendela-dunia/5-rekomendasi-souvenir-khas-bogor-untuk-oleh-oleh-21naUlT0k1w/full) |
| 9  | Miniatur Bangunan          | Kerajinan        | 100,000    | Miniatur bangunan bersejarah di Bogor, membawa aura historis dari bangunan tersebut        | [kumparan](https://kumparan.com/jendela-dunia/5-rekomendasi-souvenir-khas-bogor-untuk-oleh-oleh-21naUlT0k1w/full) |
| 10 | Batik Tulis                | Pakaian          | 250,000    | Batik tulis khas Bogor dengan inovasi busana dari desain dan warna yang menarik            | [kumparan](https://kumparan.com/jendela-dunia/5-rekomendasi-souvenir-khas-bogor-untuk-oleh-oleh-21naUlT0k1w/full) |
| 11 | Kaos Unchal                | Pakaian          | 80,000     | Kaos Unchal khas Bogor dengan desain grafis dan kata-kata lucu yang cocok untuk oleh-oleh  | [kumparan](https://kumparan.com/jendela-dunia/5-rekomendasi-souvenir-khas-bogor-untuk-oleh-oleh-21naUlT0k1w/full) |
| 12 | Sedotan Kayu Bambu LL9     | Peralatan Minum  | 1,000      | Sedotan kayu bambu yang ramah lingkungan dan cocok digunakan untuk minuman                 | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 13 | Gantungan Kunci Botol GK53c| Aksesori         | 1,200      | Gantungan kunci berbentuk botol yang terbuat dari bahan plastik dengan desain unik         | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 14 | Gagang Kerangka Kipas 17an GSC175 | Aksesori  | 1,250      | Kerangka kipas untuk acara 17-an dengan desain klasik                                      | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 15 | Pembuka Botol LL12         | Peralatan Dapur | 1,350      | Pembuka botol yang terbuat dari bahan logam berkualitas                                    | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 16 | Gantungan Kunci Kendang Medium GK52 | Aksesori | 1,400      | Gantungan kunci berbentuk kendang dengan ukuran medium                                     | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 17 | Gagang Kerangka Kipas Tepi Kulit Hitam 19an GSC174 | Aksesori | 1,500 | Kerangka kipas dengan tepi kulit hitam yang elegan                                         | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 18 | Tempat Lilin Koting Kupu LL13 | Dekorasi     | 1,550      | Tempat lilin dengan desain kupu-kupu yang cantik                                           | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 19 | Gantungan Kunci Bahan Kulit Kacang GSC138 | Aksesori | 1,599      | Gantungan kunci dari bahan kulit kacang berukuran sekitar 2x9 cm                           | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 20 | Undangan Gulung Natural UGL1 | Undangan       | 1,700      | Undangan pernikahan berbentuk gulung dengan desain natural                                 | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 21 | Pulpen Kapsul PNS4         | Alat Tulis      | 1,700      | Pulpen berbentuk kapsul dengan warna-warna menarik                                         | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 22 | Pulpen Silver dan Emas PNS5 | Alat Tulis     | 1,700      | Pulpen dengan warna perak dan emas yang elegan                                             | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 23 | Gantungan Kunci Dompet Mini GK54 | Aksesori   | 1,600      | Gantungan kunci berbentuk dompet mini yang praktis                                         | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 24 | Pulpen Bambu PNS3          | Alat Tulis      | 1,800      | Pulpen berbahan bambu dengan desain yang ramah lingkungan                                  | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 25 | Centong Plastik Maxi GSC182 | Peralatan Dapur | 1,850      | Centong plastik dengan ukuran maxi untuk keperluan dapur                                   | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 26 | Sisir Kayu LL8             | Peralatan Pribadi| 1,900     | Sisir kayu yang cocok digunakan untuk berbagai jenis rambut                                | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/)   |
| 27 | Souvenir Gelas Enamel  | Peralatan Dapur    | 7,000        | Gelas enamel berbagai warna dengan gambar di sisinya                                 | [gisacraft](https://www.gisacraft.com/product/souvenir-gelas-enamel-warna-warni-gsc170/) |
| 28 | Pouch Rasfur Bunga     | Kerajinan          | 5,000       | Pouch yang terbuat dari rasfur dengan motif bunga                                      | [gisacraft](https://www.gisacraft.com/product/souvenir-pouch-rasfur-bunga-dpt91/) |
| 29 | Pouch Kanvas Motif Lapis Furing | Kerajinan | 4,700       | Pouch yang terbuat dari kanvas dilapisi dengan furing                                  | [gisacraft](https://www.gisacraft.com/product/souvenir-pouch-kanvas-motif-lapis-furing-pv11/) |
| 30 | Kantung Goni Kecil DPT100   | Kerajinan     | 3,000       | Kantung kecil terbuat dari karung goni untuk menyimpan barang                          | [gisacraft](https://www.gisacraft.com/product/souvenir-kantung-goni-kecil-dpt100/) |
| 31 | Dompet Anyaman Bambu GSC107 | Kerajinan     | 4,500       | Dompet sederhana terbuat dari anyaman bambu                                            | [gisacraft](https://www.gisacraft.com/product/souvenir-dompet-anyaman-bambu-gsc107/) |
| 32 | Key Holder Bahan Hosana Kancing | Aksesori  | 4,500       | Aksesori untuk menyimpan kunci terbuat dari hosana dilengkapi dengan kancing           | [gisacraft](https://www.gisacraft.com/product/gsc76/) |
| 33 | Dompet Ulir Pisang Anyaman Mendong | Kerajinan | 6,000    | Dompet berbentuk silinder yang terbuat dari anyaman mendong                            | [gisacraft](https://www.gisacraft.com/product/souvenir-dompet-ulir-pisang-anyaman-mendong-dpt104/) |
| 34 | Dompet Batik Beranak Set 3  | Kerajinan     | 6,400       | 3 dompet dengan motif batik dengan ukuran bervariasi                                   | [gisacraft](https://www.gisacraft.com/product/souvenir-dompet-batik-beranak-set-3-dpt99/) |
| 35 | Keranjang Mini anyaman Bambu | Kerajinan    | 4,000       | Keranjang mini terbuat dari anyaman bambu yang bisa menyimpan barang                   | [gisacraft](https://www.gisacraft.com/product-tag/souvenir-murah-bogor/page/10/) |
| 36 | Magnet kulkas Puncak Bogor | Kerajinan    | 22,500       | Hiasan magnet yang dapat ditempelkan pada kulkas                   | [Tokopedia]([https://www.gisacraft.com/product-tag/souvenir-murah-bogor/page/10/](https://www.tokopedia.com/novelty/souvenir-magnet-kulkas-puncak-bogor-jawa-barat-oleh-negara-indonesia?extParam=ivf%3Dfalse%26keyword%3Dsouvenir+bogor%26search_id%3D20241009160408E0DEFCAD37E2903E38UR%26src%3Dsearch&refined=true)) |
| 37 | Gantungan kunci relief  | Kerajinan    | 9,500       | Gantungan kunci dengan motif berbentuk ukiran pada kayu                   | [Tokopedia](https://www.tokopedia.com/najlaasouvenir/gantungan-kunci-khas-bogor-souvenir-khas-bogor?extParam=cmp%3D1%26ivf%3Dfalse%26keyword%3Dgantungan+kunci+bogor%26search_id%3D2024100916094966E76E8D419CA123688Y%26src%3Dsearch) |
| 38 | Gantungan kunci Tugu Kujang | Kerajinan    | 5,000       | Gantungan kunci yang berbentuk miniatur dari Tugu Kujang di Bogor                   | [Shopee](https://shopee.co.id/gantungan-kunci-tugu-kujang-bogor-i.279920477.14098230652) |
| 39 | Pot tanaman berbentuk tempat wisata | Kerajinan    | 48,000       | Pot tanaman berbentuk miniatur tempat-tempat wisata di Bogor                   | [Direktori Bogor](http://direktori.kotabogor.go.id/index.php/situs/wisatacend) |
| 40 | Pin peniti Tugu Kujang | Kerajinan    | 9,800       | pin peniti untuk menyambung kain berbentuk miniatur Tugu Kujang di Bogor                   | [Bukalapak](https://m.bukalapak.com/products/s/kujang-pin-kujang-khas-bogor) |
| 41 | Kaos motif Batik Kujang | Pakaian    | 175,000       | Baju kaos dengan motif Batik Kujang                   | [Shopee](https://shopee.co.id/BATIK-TRADISIKU-Kaos-Batik-Bogor-Kujang-Kijang-i.31828090.3976076338) |
| 42 | Kemeja motif Batik Kujang | Pakaian    | 199,000       | Baju kemeja dengan motif Batik Kujang                   | [Tokopedia]([https://www.gisacraft.com/product-tag/souvenir-murah-bogor/page/10/](https://www.tokopedia.com/batikarkanza1/batik-arkanza-motif-adinata-pendek-kemeja-batik-premium-pria-pendek-xl-809ee?extParam=ivf%3Dfalse&src=topads)) |

## Role atau Peran Pengguna Beserta Deskripsinya
| **Role**                    | **Deskripsi**                                                                       |
|-----------------------------|-------------------------------------------------------------------------------------|
| Admin                       | Menambahkan produk dan promo ke katalog, mengelola transaksi dan ulasan.            |
| User                        | Melihat dan membeli produk, memberikan ulasan, dan rating. Harus memiliki akun.     |
| Guest (Optional)            | Melihat-lihat produk, tetapi tidak bisa membeli atau memberikan ulasan.             |
| Customer Service (Optional) | Menangani pertanyaan dan keluhan pengguna, serta melihat data pengguna dan pesanan. |

## Desain dan Struktur Aplikasi

### USER <div align="center"></div>

#### Atribut User
| Atribut            | Deskripsi                                   | Tipe Data       |
|--------------------|---------------------------------------------|-----------------|
| ID User            | Identifikasi unik untuk pengguna            | Integer (UUID)  |
| Nama User          | Nama lengkap pengguna                       | String          |
| Email              | Alamat email pengguna                       | String          |
| Password           | Kata Sandi untuk login                      | String (hashed) |
| Tanggal Bergabung  | Tanggal saat pengguna mendaftar             | DateTime        |
| Status             | Status akun (Aktif, Tidak Aktif)            | String          |

#### Login Page
| Atribut     | Deskripsi                            | Tipe Data  |
|-------------|--------------------------------------|------------|
| Username    | Nama pengguna untuk login            | String     |
| Password    | Kata sandi untuk login               | String     |

#### Home Page
| Atribut            | Deskripsi                                                        | Tipe Data            |
|--------------------|------------------------------------------------------------------|----------------------|
| Kategori           | Jenis kategori oleh-oleh, dibagi menjadi 2 (makanan/barang)      | String               |
| ID Kategori        | Identifikasi unik untuk kategori                                 | Integer (UUID)       |
| Nama Kategori      | Nama lengkap kategori                                            | String               |
| Gambar Kategori    | URL gambar untuk kategori                                        | String               |
| Deskripsi Kategori | Penjelasan singkat tentang kategori                              | Text                 |
| Daftar Produk      | List produk yang termasuk dalam kategori                         | Array of Product IDs |

#### Detail Product
| Atribut              | Deskripsi                                     | Tipe Data           |
|----------------------|-----------------------------------------------|---------------------|
| ID Produk            | Identifikasi unik untuk produk                | Integer (UUID)      |
| Nama Produk          | Nama dari produk                              | String              |
| Deskripsi            | Penjelasan tentang produk                     | Text                |
| Harga                | Harga Produk                                  | Float               |
| Gambar               | URL gambar produk                             | String              |
| Ulasan dan Rating    | Ulasan pengguna dan rating produk             | Array of Objects    |
| Tambah ke Favorit    | Fitur untuk menyimpan produk sebagai Favorit  | -                   |

#### Cart Page
| Atribut           | Deskripsi                                        | Tipe Data          |
|-------------------|--------------------------------------------------|--------------------|
| Daftar Produk      | Produk yang ada di keranjang                    | Array of Products  |
| Total Harga       | Total harga produk dalam keranjang               | Float              |
| Pengiriman        | Informasi mengenai pengiriman                    | String             |
| Pembayaran        | Metode pembayaran                                | String             |
| Checkout          | Proses penyelesaian pembelian                    | String             |

#### Riwayat Pembelian
| Atribut           | Deskripsi                                        | Tipe Data         |
|-------------------|--------------------------------------------------|-------------------|
| Daftar Transaksi   | Semua transaksi yang telah dilakukan            | Array of Objects  |
| Detail Transaksi   | Detail setiap transaksi                         | Array of Objects  |
| Tanggal Pembelian  | Tanggal transaksi                               | DateTime          |
| Status Pembayaran  | Status pembayaran (Sukses/Gagal)                | String            |

### ADMIN <div align="center"></div>

#### Tabel Admin
| Atribut            | Deskripsi                                       | Tipe Data          |
|--------------------|-------------------------------------------------|--------------------|
| ID Admin           | Identifikasi unik untuk pengguna                | Integer (UUID)     |
| Nama Admin/Toko    | Nama lengkap admin                              | String             |
| Email              | Alamat email admin                              | String             |
| Password           | Kata Sandi untuk login                          | String (hashed)    |
| Tanggal Bergabung  | Tanggal saat admin mendaftar                    | DateTime           |
| Status             | Status akun (Aktif, Tidak Aktif)                | String             |

#### Product Management Page (Tambah, Edit & Hapus Product)
| Atribut           | Deskripsi                                        | Tipe Data          |
|-------------------|--------------------------------------------------|--------------------|
| ID Produk          | Identifikasi unik untuk setiap produk           | Integer (UUID)     |
| Nama Produk        | Nama dari produk                                | String             |
| Deskripsi Produk   | Keterangan produk                               | String             |
| Rating             | Rating produk                                   | Float              |
| Stok               | Jumlah ketersediaan Produk                      | Integer            |
| Toko Penjual       | Keterangan Penjual Produk                       | String             |

#### Promo Management Page (Tambah, Edit & Hapus Promo)
| Atribut            | Deskripsi                                       | Tipe Data          |
|--------------------|-------------------------------------------------|--------------------|
| ID Promo           | Identifikasi unik untuk setiap promo            | Integer (UUID)     |
| Kode               | Kode Promo                                      | String             |
| Potongan Harga     | Jumlah Potongan Harga Produk                    | Float              |
| Masa berlaku       | Rentang waktu berlaku promo                     | String             |
| Minimal Transaksi  | Minimal harga transaksi untuk mendapatkan promo | Float              |
| Toko Terkait       | Toko yang bisa menggunakan promo                | Array of Toko IDs  |
