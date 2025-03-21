import datetime
import random

perpustakaan = {}
peminjaman = {}

def tampilkan_buku():
    if not perpustakaan:
        print("\nPerpustakaan masih kosong.")
    else:
        print("\nDaftar Buku:")
        for id_buku, data in perpustakaan.items():
            if data["status"]:  
                status = "Tersedia"
            else:  
                status = f"**Dipinjam oleh {peminjaman[id_buku]['nama']}** pada {peminjaman[id_buku]['tanggal']}"
            
            print(f"ID: {id_buku} | Judul: {data['judul']} | Penulis: {data['penulis']} | Status: {status}")

def tambah_buku():
    judul = input("\nMasukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    id_buku = random.randint(1000, 9999)

    perpustakaan[id_buku] = {
        "judul": judul,
        "penulis": penulis,
        "status": True  
    }
    print(f"Buku '{judul}' berhasil ditambahkan dengan ID {id_buku}.")

def cari_buku():
    kata_kunci = input("\nMasukkan judul atau nama penulis: ").lower()
    hasil = []

    for id_buku, data in perpustakaan.items():
        if kata_kunci in data["judul"].lower() or kata_kunci in data["penulis"].lower():
            hasil.append((id_buku, data))

    if hasil:
        print("\nHasil Pencarian:")
        for id_buku, data in hasil:
            status = "Tersedia" if data["status"] else f"**Dipinjam oleh {peminjaman[id_buku]['nama']}** pada {peminjaman[id_buku]['tanggal']}"
            print(f"ID: {id_buku} | Judul: {data['judul']} | Penulis: {data['penulis']} | Status: {status}")
    else:
        print("Buku tidak ditemukan.")

def pinjam_buku():
    tampilkan_buku()
    try:
        id_buku = int(input("\nMasukkan ID buku yang ingin dipinjam: "))
        if id_buku in perpustakaan and perpustakaan[id_buku]["status"]:
            nama_peminjam = input("Masukkan nama peminjam: ")
            tanggal_pinjam = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            perpustakaan[id_buku]["status"] = False
            peminjaman[id_buku] = {
                "nama": nama_peminjam,
                "tanggal": tanggal_pinjam
            }

            print(f"Buku '{perpustakaan[id_buku]['judul']}' berhasil dipinjam oleh {nama_peminjam}.")
        else:
            print("Buku tidak tersedia atau ID tidak ditemukan.")
    except ValueError:
        print("Masukkan ID yang valid!")

def kembalikan_buku():
    try:
        id_buku = int(input("\nMasukkan ID buku yang ingin dikembalikan: "))
        if id_buku in peminjaman:
            perpustakaan[id_buku]["status"] = True
            nama_peminjam = peminjaman[id_buku]["nama"]
            tanggal_pinjam = peminjaman[id_buku]["tanggal"]
            tanggal_kembali = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f"\nBuku '{perpustakaan[id_buku]['judul']}' telah dikembalikan oleh {nama_peminjam}.")
            print(f"Tanggal Peminjaman: {tanggal_pinjam}")
            print(f"Tanggal Pengembalian: {tanggal_kembali}")

            del peminjaman[id_buku]
        else:
            print("Buku tidak sedang dipinjam atau ID salah.")
    except ValueError:
        print("Masukkan ID yang valid!")

def main():
    while True:
        print("\n=== SISTEM MANAJEMEN PERPUSTAKAAN CILACAP ===")
        print("1. Tampilkan Semua Buku")
        print("2. Tambah Buku")
        print("3. Cari Buku")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tampilkan_buku()
        elif pilihan == "2":
            tambah_buku()
        elif pilihan == "3":
            cari_buku()
        elif pilihan == "4":
            pinjam_buku()
        elif pilihan == "5":
            kembalikan_buku()
        elif pilihan == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
