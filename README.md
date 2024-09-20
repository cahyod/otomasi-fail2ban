# otomasi-fail2ban
Otomasi setting zona Asia/Jakarta dan Fail2ban menggunakan python3

Skrip Python3 yang akan secara otomatis mengatur zona waktu ke `Asia/Jakarta` dan memasang serta mengkonfigurasi `fail2ban` di server Ubuntu Anda. Skrip ini melakukan hal-hal berikut:

1. **Memeriksa Hak Akses Root:** Skrip ini harus dijalankan dengan hak akses root atau menggunakan `sudo`.
2. **Mengatur Zona Waktu ke Asia/Jakarta:** Menggunakan `timedatectl` untuk mengatur zona waktu.
3. **Memperbarui Daftar Paket dan Memasang Fail2Ban:** Menggunakan `apt` untuk memperbarui daftar paket dan memasang `fail2ban`.
4. **Mengaktifkan dan Memulai Layanan Fail2Ban:** Memastikan bahwa `fail2ban` berjalan dan diatur untuk memulai secara otomatis saat booting.
5. **Membuat Konfigurasi Dasar Fail2Ban untuk SSHD:** Menambahkan konfigurasi dasar untuk memantau layanan SSH.

### **Cara Menggunakan Skrip Ini**

1. **Simpan Skrip:**
   Simpan skrip di atas ke dalam file, misalnya `setup_fail2ban.py`.

2. **Beri Izin Eksekusi:**
   Buka terminal dan beri izin eksekusi pada skrip:
   ```bash
   chmod +x setup_fail2ban.py
   ```

3. **Jalankan Skrip dengan Hak Akses Root:**
   Karena skrip ini memerlukan hak akses root untuk mengubah pengaturan sistem dan memasang paket, jalankan dengan `sudo`:
   ```bash
   sudo ./setup_fail2ban.py
   ```

### **Penjelasan Skrip**

1. **Fungsi `run_command`:**
   - Menjalankan perintah shell dan menampilkan outputnya secara real-time.
   - Jika terjadi kesalahan, skrip akan berhenti dan menampilkan pesan error.

2. **Fungsi `check_root`:**
   - Memastikan skrip dijalankan dengan hak akses root. Jika tidak, skrip akan berhenti.

3. **Fungsi `set_timezone`:**
   - Mengatur zona waktu sistem menggunakan `timedatectl`.

4. **Fungsi `update_packages`:**
   - Memperbarui daftar paket dengan `apt-get update`.
   - Meningkatkan paket yang sudah ada dengan `apt-get upgrade`.

5. **Fungsi `install_fail2ban`:**
   - Memeriksa apakah `fail2ban` sudah terpasang.
   - Jika belum, memasangnya menggunakan `apt-get install fail2ban`.

6. **Fungsi `configure_fail2ban`:**
   - Menulis konfigurasi dasar untuk `fail2ban` ke file `jail.local`.
   - Konfigurasi ini mengaktifkan monitoring untuk layanan SSHD dengan parameter tertentu.

7. **Fungsi `enable_and_start_fail2ban`:**
   - Mengaktifkan layanan `fail2ban` agar berjalan saat booting.
   - Memulai atau merestart layanan `fail2ban`.
   - Menampilkan status `fail2ban` untuk memastikan semuanya berjalan dengan baik.

8. **Fungsi `main`:**
   - Menjalankan semua fungsi di atas secara berurutan.
   - Menampilkan pesan selesai setelah semua langkah berhasil dilakukan.

### **Catatan Tambahan**

- **Backup Konfigurasi:**
  Sebelum menulis ulang file konfigurasi `jail.local`, sebaiknya lakukan backup jika Anda telah memiliki konfigurasi khusus.
  ```bash
  sudo cp /etc/fail2ban/jail.local /etc/fail2ban/jail.local.backup
  ```

- **Menyesuaikan Konfigurasi:**
  Anda dapat menyesuaikan parameter seperti `maxretry`, `bantime`, dan `findtime` sesuai dengan kebutuhan keamanan Anda.

- **Menambahkan Jails Lain:**
  Jika Anda memiliki layanan lain yang ingin dipantau oleh `fail2ban`, Anda dapat menambahkannya ke dalam file `jail.local` setelah konfigurasi dasar.

- **Log Fail2Ban:**
  Untuk memeriksa log `fail2ban`, Anda dapat melihat file `/var/log/fail2ban.log`:
  ```bash
  sudo tail -f /var/log/fail2ban.log
  ```
  ### **Selesai**
