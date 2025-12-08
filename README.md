# 🍌 Jim The Monkey

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?style=for-the-badge&logo=pygame)

> **Jim The Monkey** adalah game arkade 2D berbasis *procedural generation* di mana pemain harus mengumpulkan pisang di dalam labirin yang selalu berubah, menghindari hantu, dan mencari jalan keluar.

---

## 📋 Daftar Isi
- [Gambaran Umum](#-gambaran-umum)
- [Goals Game](#-goals-game)
- [Struktur Projek](#-struktur-projek)
- [Teknologi dan Algoritma](#-teknologi-dan-algoritma-yang-digunakan)
- [Kontribusi](#-kontribusi)
- [Lisensi](#-lisensi)

---

## 📖 Gambaran Umum

Game ini dibuat menggunakan bahasa pemrograman **Python** dan library **Pygame**. Game ini menonjolkan fitur **Procedural Map Generation**, yang berarti peta labirin dibuat secara acak setiap kali permainan dimulai atau di-reset. Tidak ada dua permainan yang sama persis.

Game ini menampilkan grafis berbasis Emoji yang unik, animasi intro *zoom-in* yang sinematik, serta sistem audio yang responsif terhadap aksi pemain.

### Fitur Utama:
* **Infinite Maps:** Map dibuat otomatis dengan algoritma penggali acak.
* **Dynamic Difficulty:** Jumlah musuh menyesuaikan luas area peta.
* **Smart Rendering:** Tampilan menggunakan Emoji (🐒, 👻, 🍌) dan mendukung animasi kamera.
* **Responsive Audio:** Musik latar dan efek suara untuk setiap interaksi.
* **Window Scaling:** Ukuran jendela permainan menyesuaikan ukuran peta secara otomatis.

---

## 🎯 Goals Game

Tujuan utama pemain sangat sederhana namun menantang:

1.  **Kumpulkan Semua Pisang (🍌):** Pemain harus menjelajahi labirin untuk mengambil semua item pisang yang tersebar.
2.  **Hindari Hantu (👻):** NPC musuh bergerak secara acak. Jika pemain bersentuhan dengan hantu, permainan berakhir (*Game Over*).
3.  **Buka Pintu Keluar (🚪):** Pintu awalnya terkunci (🔒). Setelah semua pisang terkumpul, pintu akan terbuka.
4.  **Menangkan Level:** Masuk ke pintu yang terbuka untuk memenangkan permainan.

**Kontrol:**
* `Arrow Keys` atau `WASD`: Bergerak.
* `R`: Reset / Generate Map Baru.

---

## 📂 Struktur Projek

Berikut adalah susunan file dalam direktori proyek ini:

```text
ColBan-Game/
│
├── main.py              # Kode utama game (Game Loop, Logika, Rendering)
├── README.md            # Dokumentasi proyek
├── requirements.txt     # Daftar library (pygame, pyinstaller)
│
├── assets/              # (Opsional) Folder untuk menyimpan audio
│   ├── bgm.mp3          # Musik latar
│   ├── eat.wav          # SFX makan pisang
│   ├── die.wav          # SFX kalah
│   ├── win.wav          # SFX menang
│   └── unlock.wav       # SFX pintu terbuka
│
└── dist/                # Folder hasil build (jika dijadikan .exe)
    └── Jim The Monkey.exe
```

## Kontribusi

Kami menyambut kontribusi dari komunitas. Jika Anda ingin berkontribusi, silakan ikuti langkah-langkah berikut:

1.  Fork repositori ini.
2.  Buat branch baru untuk fitur Anda (`git checkout -b feature/nama-fitur-baru`).
3.  Lakukan perubahan Anda dan commit (`git commit -m 'feat: tambahkan fitur X'`).
4.  Push ke branch Anda (`git push origin feature/nama-fitur-baru`).
5.  Buat Pull Request.

## Lisensi

Lisensi untuk proyek ini tidak secara eksplisit didefinisikan dalam file yang disediakan.
