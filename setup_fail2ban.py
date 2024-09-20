#!/usr/bin/env python3

import subprocess
import sys
import os

def run_command(command, check=True):
    """
    Jalankan perintah shell dan tampilkan outputnya secara real-time.
    """
    try:
        result = subprocess.run(command, shell=True, check=check, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error menjalankan perintah: {command}")
        print(e.stderr)
        sys.exit(1)

def check_root():
    """
    Periksa apakah skrip dijalankan sebagai root.
    """
    if os.geteuid() != 0:
        print("Skrip ini harus dijalankan dengan hak akses root. Gunakan sudo.")
        sys.exit(1)

def set_timezone(timezone):
    """
    Atur zona waktu sistem.
    """
    print(f"Mengatur zona waktu ke {timezone}...")
    run_command(f"timedatectl set-timezone {timezone}")

def update_packages():
    """
    Perbarui daftar paket dan tingkatkan paket yang sudah ada.
    """
    print("Memperbarui daftar paket...")
    run_command("apt-get update -y")
    print("Meningkatkan paket yang sudah ada...")
    run_command("apt-get upgrade -y")

def install_fail2ban():
    """
    Pasang fail2ban jika belum terpasang.
    """
    print("Memeriksa apakah fail2ban sudah terpasang...")
    try:
        subprocess.run("fail2ban-client --version", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Fail2Ban sudah terpasang.")
    except subprocess.CalledProcessError:
        print("Memasang Fail2Ban...")
        run_command("apt-get install fail2ban -y")

def configure_fail2ban():
    """
    Konfigurasi dasar Fail2Ban untuk SSHD.
    """
    jail_local = "/etc/fail2ban/jail.local"
    print(f"Mengkonfigurasi Fail2Ban di {jail_local}...")
    config = """
[sshd]
enabled = true
port    = ssh
filter  = sshd
logpath = /var/log/auth.log
maxretry = 5
bantime = 600
findtime = 600
"""
    try:
        with open(jail_local, "w") as f:
            f.write(config)
        print("Konfigurasi Fail2Ban berhasil ditulis.")
    except Exception as e:
        print(f"Gagal menulis konfigurasi Fail2Ban: {e}")
        sys.exit(1)

def enable_and_start_fail2ban():
    """
    Aktifkan dan mulai layanan Fail2Ban.
    """
    print("Mengaktifkan layanan Fail2Ban agar berjalan saat boot...")
    run_command("systemctl enable fail2ban")
    print("Memulai layanan Fail2Ban...")
    run_command("systemctl restart fail2ban")
    print("Memeriksa status Fail2Ban...")
    run_command("fail2ban-client status")

def main():
    check_root()
    set_timezone("Asia/Jakarta")
    update_packages()
    install_fail2ban()
    configure_fail2ban()
    enable_and_start_fail2ban()
    print("Otomasi selesai. Zona waktu telah diatur ke Asia/Jakarta dan Fail2Ban telah dipasang serta dikonfigurasi.")

if __name__ == "__main__":
    main()

