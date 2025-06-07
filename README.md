# 🔐 pin_md5_cracker.py

`pin_md5_cracker.py` adalah program Python sederhana yang digunakan untuk mencari PIN numerik 4 digit (0000–9999) berdasarkan nilai hash MD5 yang diberikan. Program ini berguna untuk melakukan _brute force_ terhadap hash MD5 dari PIN.

## 🧠 Cara Kerja

Program akan mencoba semua kemungkinan PIN dari `0000` sampai `9999` dan mencocokkannya dengan nilai hash MD5 yang diberikan. Jika ditemukan kecocokan, maka PIN akan ditampilkan bersamaan dengan waktu yang dibutuhkan untuk pencarian.

## 📝 Cara Menggunakan

1. Pastikan Anda memiliki Python 3.x terinstal.
2. Simpan file `pin_md5_cracker.py`.
3. Jalankan program melalui terminal atau command prompt:

```bash
python pin_md5_cracker.py
```

4. Masukkan hash MD5 yang ingin dicari (bisa lebih dari satu, pisahkan dengan koma).

Contoh input:
```
e10adc3949ba59abbe56e057f20f883e
```

Jika PIN ditemukan, program akan menampilkan hasil seperti berikut:
```
PIN ditemukan: 123456 (MD5: e10adc3949ba59abbe56e057f20f883e) - Waktu pencarian: 0:00:00.053871
```

## 📁 Contoh Hash MD5
| PIN     | MD5 Hash                           |
|---------|------------------------------------|
| 0000    | 670b14728ad9902aecba32e22fa4f6bd   |
| 1234    | 81dc9bdb52d04dc20036dbd8313ed055   |
| 9999    | ef775988943825d2871e1cfa75473ec0   |

## ⚠️ Peringatan
- Program ini hanya untuk tujuan edukasi dan uji coba keamanan pribadi.
- Jangan gunakan untuk tujuan yang melanggar hukum.

## 👨‍💻 Penulis
Dibuat oleh [Ezzar]

---
Lisensi: MIT