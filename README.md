# ![HasBogor](URL_GAMBAR) <!-- Replace URL_GAMBAR with the actual image link -->

# Project Title
HasBogor

A brief description of what this project does and who it's for.

**Nama-nama anggota kelompok**:
- Akmal Nabil Fikri - 2306152084
- Rebecca Zaneta Octoria Hutajulu - 2306275065
- Michael Ignasius 
- 2306259950
- Ivan Jehuda Angi - 2306152222
- Ismail Yanuar Anwas - 2306245781
- Widya Mutia Ichsan - 2306165912

## Table of Contents
- [Deskripsi Aplikasi](#deskripsi-aplikasi)
- [Daftar Modul yang Akan Diimplementasikan](#daftar-modul-yang-akan-diimplementasikan)
- [Sumber Initial Dataset Kategori Utama Produk](#sumber-initial-dataset-kategori-utama-produk)
- [Promo](#promo)
- [Role atau Peran Pengguna Beserta Deskripsinya](#role-atau-peran-pengguna-beserta-deskripsinya)
- [Desain dan Struktur Aplikasi](#desain-dan-struktur-aplikasi)
  - [USER](#user)
  - [ADMIN](#admin)
  - [Login Page](#login-page)
  - [Home Page](#home-page)
  - [Detail Product](#detail-product)
  - [Cart Page](#cart-page)
  - [Riwayat Pembelian](#riwayat-pembelian)
  - [Product Management Page](#product-management-page)
  - [Promo Management Page](#promo-management-page)

## Deskripsi Aplikasi
HasBogor adalah aplikasi web yang hadir untuk menjawab kebutuhan wisatawan dan masyarakat dalam menemukan produk oleh-oleh khas Bogor dengan lebih mudah dan efisien. Aplikasi ini menyediakan pusat informasi dan transaksi oleh-oleh khas Bogor seperti makanan khas, kerajinan tangan, dan banyak lagi. Pengguna dapat memesan produk secara online dan berinteraksi dengan komunitas melalui ulasan dan rekomendasi produk.

Kebermanfaatan aplikasi ini:
- Mendukung pengrajin lokal dalam menjual produk mereka.
- Meningkatkan akses wisatawan ke produk-produk khas Bogor.
- Mempermudah transaksi dan memperkaya pengalaman belanja oleh-oleh.

## Daftar Modul yang Akan Diimplementasikan
| **Modul**       | **Deskripsi**                                                                 |
|-----------------|-------------------------------------------------------------------------------|
| Autentikasi     | Mengelola login dan registrasi pengguna, termasuk pengelolaan password.       |
| Produk          | Menampilkan daftar produk, detail produk, dan fitur pencarian.               |
| Keranjang       | Mengelola produk yang ditambahkan ke keranjang dan proses checkout.           |
| Pembayaran      | Menangani proses pembayaran dan konfirmasi transaksi.                         |
| Ulasan          | Pengguna dapat memberikan ulasan dan rating pada produk.                     |
| Event           | Menampilkan acara lokal di Bogor.                                             |
| Kontak          | Form kontak untuk layanan pelanggan.                                          |
| Promo           | Mengolah dan menampilkan promo dan diskon.                                    |
| Rekomendasi     | Memberikan rekomendasi produk kepada pengguna.                                |

## Sumber Initial Dataset Kategori Utama Produk
| **Kategori Produk** | **Deskripsi**                                                               | **Sumber Data**            |
|---------------------|-----------------------------------------------------------------------------|----------------------------|
| Makanan             | Berbagai makanan khas Bogor seperti brownies, dodol, dan keripik.           | (dikirim oleh Ismail)       |
| Souvenir            | Kerajinan tangan unik sebagai kenang-kenangan.                             | (dikirim oleh Ismail)       |

## Promo
Diskon dan penawaran spesial untuk produk tertentu selama periode tertentu, seperti saat hari-hari besar atau tanggal kembar.

## Role atau Peran Pengguna Beserta Deskripsinya
| **Role**         | **Deskripsi**                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------|
| Admin            | Menambahkan produk dan promo ke katalog, mengelola transaksi dan ulasan.                      |
| User             | Melihat dan membeli produk, memberikan ulasan, dan rating. Harus memiliki akun.               |
| Guest (Optional) | Melihat-lihat produk, tapi tidak bisa membeli atau memberikan ulasan.                         |
| Customer Service (Optional) | Menangani pertanyaan dan keluhan pengguna. Melihat data pengguna dan pesanan.       |

## Desain dan Struktur Aplikasi

### USER
| **Atribut**       | **Deskripsi**                         | **Tipe Data**   |
|-------------------|---------------------------------------|-----------------|
| ID User           | Identifikasi unik untuk pengguna      | Integer (UIUD)  |
| Nama User         | Nama lengkap pengguna                 | String          |
| Email             | Alamat email pengguna                 | String          |
| Password          | Kata sandi yang di-hash               | String (hashed) |
| Tanggal Bergabung | Tanggal pendaftaran                   | Date Time       |
| Status            | Status akun, misal: Aktif, Tidak Aktif| String          |

### ADMIN
| **Atribut**        | **Deskripsi**                              | **Tipe Data**   |
|--------------------|--------------------------------------------|-----------------|
| ID Admin           | Identifikasi unik untuk admin              | Integer (UIUD)  |
| Nama Admin/toko    | Nama lengkap admin                         | String          |
| Email              | Email admin                                | String          |
| Password           | Kata sandi yang di-hash                    | String (hashed) |
| Tanggal Bergabung  | Tanggal admin mendaftar                    | DateTime        |
| Status             | Status admin, misal: Aktif, Tidak Aktif     | String          |

### Login Page
| **Atribut**  | **Deskripsi**                   | **Tipe Data** |
|--------------|---------------------------------|---------------|
| Username     | Nama pengguna untuk login       | String        |
| Password     | Kata sandi untuk login          | String        |

### Home Page
| **Atribut**          | **Deskripsi**                                 | **Tipe Data** |
|----------------------|-----------------------------------------------|---------------|
| Kategori             | Jenis kategori oleh-oleh (Makanan, Barang)     | String        |
| ID Kategori          | Identifikasi unik untuk kategori               | Integer (UIUD)|
| Nama Kategori        | Nama lengkap kategori                          | String        |
| Gambar Kategori      | URL gambar untuk kategori                      | String        |
| Deskripsi Kategori   | Penjelasan singkat tentang kategori             | Text          |
| Daftar Produk        | List produk yang termasuk dalam kategori        | Array of IDs  |

### Detail Product
| **Atribut**      | **Deskripsi**                                  | **Tipe Data**    |
|------------------|------------------------------------------------|------------------|
| ID Produk        | Identifikasi unik untuk produk                  | Integer (UIUD)   |
| Nama Produk      | Nama dari produk                                | String           |
| Deskripsi        | Penjelasan tentang produk                       | Text             |
| Harga            | Harga produk                                    | Float            |
| Gambar           | URL gambar produk                               | String           |
| Ulasan dan Rating| Ulasan pengguna dan rating produk               | Array of Objects |
| Tambah ke Favorit| Fitur untuk menyimpan produk sebagai favorit    | -                |

### Cart Page
| **Atribut**     | **Deskripsi**                                 | **Tipe Data** |
|-----------------|-----------------------------------------------|---------------|
| Daftar Produk   | Produk yang ada di keranjang                  | String        |
| Total Harga     | Total harga keseluruhan produk di keranjang   | Integer       |
| Pengiriman      | Informasi pengiriman                          | -             |
| Pembayaran      | Informasi pembayaran                          | -             |
| Checkout        | Proses finalisasi transaksi                   | -             |

### Riwayat Pembelian
| **Atribut**         | **Deskripsi**                               | **Tipe Data**     |
|---------------------|---------------------------------------------|-------------------|
| Daftar Transaksi    | Semua transaksi yang sudah dilakukan        | Array of Objects  |
| Detail Transaksi    | Detail dari setiap transaksi                | Array of Objects  |
| Tanggal Pembelian   | Tanggal transaksi                           | DateTime          |
| Status Pembayaran   | Status pembayaran (Sukses/Gagal)            | String            |

### Product Management Page
| **Atribut**       | **Deskripsi**                                   | **Tipe Data**   |
|-------------------|-------------------------------------------------|-----------------|
| ID Produk         | Identifikasi unik untuk setiap produk           | Integer (UIUD)  |
| Nama Produk       | Nama produk                                     | String          |
| Deskripsi Produk  | Keterangan produk                               | String          |
| Rating            | Rating produk                                   | Float           |
| Stok              | Jumlah produk tersedia                          | Integer         |
| Toko Penjual      | Nama penjual produk                             | String          |

### Promo Management Page
| **Atribut**       | **Deskripsi**                                 | **Tipe Data**   |
|-------------------|-----------------------------------------------|-----------------|
| ID Promo          | Identifikasi unik untuk promo                 | Integer (UIUD)  |
| Kode              | Kode promo                                    | String          |
| Potongan Harga    | Diskon dari promo                             | String          |
| Masa berlaku      | Rentang waktu promo berlaku                   | Float           |
| Minimal Transaksi | Batas minimal harga produk untuk promo berlaku | Integer         |
