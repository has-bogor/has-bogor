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
  - [USER](#user)
  - [ADMIN](#admin)

## Deskripsi Aplikasi
**HasBogor** adalah aplikasi web yang bertujuan untuk memenuhi kebutuhan wisatawan dan masyarakat dalam menemukan produk oleh-oleh khas Bogor dengan lebih mudah dan efisien. Aplikasi ini menyediakan pusat informasi dan transaksi untuk oleh-oleh khas Bogor, termasuk makanan khas, kerajinan tangan, dan banyak lagi. Pengguna dapat memesan produk secara online serta berinteraksi dengan komunitas melalui ulasan dan rekomendasi produk.

### Kebermanfaatan Aplikasi
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
| Makanan             | Berbagai makanan khas Bogor seperti brownies, dodol, dan keripik.           | Menyusul                  |
| Souvenir            | Kerajinan tangan unik sebagai kenang-kenangan.                             | Menyusul                  |

## Role atau Peran Pengguna Beserta Deskripsinya
| **Role**         | **Deskripsi**                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------|
| Admin            | Menambahkan produk dan promo ke katalog, mengelola transaksi dan ulasan.                      |
| User             | Melihat dan membeli produk, memberikan ulasan, dan rating. Harus memiliki akun.               |
| Guest (Optional) | Melihat-lihat produk, tetapi tidak bisa membeli atau memberikan ulasan.                      |
| Customer Service (Optional) | Menangani pertanyaan dan keluhan pengguna, serta melihat data pengguna dan pesanan.  |

## Desain dan Struktur Aplikasi

### USER <div align="center"></div>

#### Atribut User
| Atribut            | Deskripsi                                   | Tipe Data      |
|--------------------|---------------------------------------------|-----------------|
| ID User            | Identifikasi unik untuk pengguna            | Integer (UUID)  |
| Nama User          | Nama lengkap pengguna                       | String          |
| Email              | Alamat email pengguna                       | String          |
| Password           | Kata Sandi untuk login                      | String (hashed)  |
| Tanggal Bergabung  | Tanggal saat pengguna mendaftar            | DateTime        |
| Status             | Status akun (Aktif, Tidak Aktif)          | String          |

#### Login Page
| Atribut     | Deskripsi                            | Tipe Data  |
|-------------|--------------------------------------|------------|
| Username    | Nama pengguna untuk login            | String     |
| Password    | Kata sandi untuk login               | String     |

#### Home Page
| Atribut            | Deskripsi                                                        | Tipe Data          |
|--------------------|------------------------------------------------------------------|---------------------|
| Kategori           | Jenis kategori oleh-oleh, dibagi menjadi 2 (makanan/barang)     | String              |
| ID Kategori        | Identifikasi unik untuk kategori                                   | Integer (UUID)      |
| Nama Kategori      | Nama lengkap kategori                                             | String              |
| Gambar Kategori    | URL gambar untuk kategori                                          | String              |
| Deskripsi Kategori | Penjelasan singkat tentang kategori                               | Text                |
| Daftar Produk      | List produk yang termasuk dalam kategori                          | Array of Product IDs |

#### Detail Product
| Atribut              | Deskripsi                                 | Tipe Data          |
|----------------------|-------------------------------------------|---------------------|
| ID Produk            | Identifikasi unik untuk produk            | Integer (UUID)      |
| Nama Produk          | Nama dari produk                          | String              |
| Deskripsi            | Penjelasan tentang produk                 | Text                |
| Harga                | Harga Produk                             | Float               |
| Gambar               | URL gambar produk                         | String              |
| Ulasan dan Rating    | Ulasan pengguna dan rating produk        | Array of Objects    |
| Tambah ke Favorit    | Fitur untuk menyimpan produk sebagai Favorit | -                  |

#### Cart Page
| Atribut           | Deskripsi                                   | Tipe Data         |
|-------------------|---------------------------------------------|--------------------|
| Daftar Produk      | Produk yang ada di keranjang               | Array of Products   |
| Total Harga       | Total harga produk dalam keranjang          | Float               |
| Pengiriman        | Informasi mengenai pengiriman               | String              |
| Pembayaran        | Metode pembayaran                            | String              |
| Checkout          | Proses penyelesaian pembelian               | String              |

#### Riwayat Pembelian
| Atribut           | Deskripsi                                  | Tipe Data         |
|-------------------|--------------------------------------------|--------------------|
| Daftar Transaksi   | Semua transaksi yang telah dilakukan       | Array of Objects    |
| Detail Transaksi   | Detail setiap transaksi                     | Array of Objects    |
| Tanggal Pembelian  | Tanggal transaksi                          | DateTime           |
| Status Pembayaran  | Status pembayaran (Sukses/Gagal)          | String              |

### ADMIN <div align="center"></div>

#### Tabel Admin
| Atribut           | Deskripsi                                   | Tipe Data         |
|-------------------|---------------------------------------------|--------------------|
| ID Admin           | Identifikasi unik untuk pengguna            | Integer (UUID)     |
| Nama Admin/Toko    | Nama lengkap admin                          | String             |
| Email              | Alamat email admin                          | String             |
| Password           | Kata Sandi untuk login                      | String (hashed)    |
| Tanggal Bergabung   | Tanggal saat admin mendaftar               | DateTime           |
| Status             | Status akun (Aktif, Tidak Aktif)          | String             |

#### Product Management Page (Tambah, Edit & Hapus Product)
| Atribut           | Deskripsi                                   | Tipe Data         |
|-------------------|---------------------------------------------|--------------------|
| ID Produk          | Identifikasi unik untuk setiap produk       | Integer (UUID)     |
| Nama Produk        | Nama dari produk                            | String             |
| Deskripsi Produk   | Keterangan produk                          | String             |
| Rating             | Rating produk                              | Float              |
| Stok               | Jumlah ketersediaan Produk                 | Integer            |
| Toko Penjual       | Keterangan Penjual Produk                  | String             |

#### Promo Management Page (Tambah, Edit & Hapus Promo)
| Atribut            | Deskripsi                                   | Tipe Data         |
|--------------------|---------------------------------------------|--------------------|
| ID Promo           | Identifikasi unik untuk setiap promo       | Integer (UUID)     |
| Kode               | Kode Promo                                 | String             |
| Potongan Harga     | Jumlah Potongan Harga Produk               | Float              |
| Masa berlaku       | Rentang waktu berlaku promo                 | String             |
| Minimal Transaksi  | Minimal harga transaksi untuk mendapatkan promo | Float              |
| Toko Terkait      | Toko yang bisa menggunakan promo            | Array of Toko IDs  |
