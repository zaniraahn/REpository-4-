catatan = []
favorit = set()
target_harian = None  # dalam menit, None jika belum di-set

def tambah_catatan():
    while True:
        mapel = input("Mapel: ").strip()
        if mapel:
            break
        print("Mapel tidak boleh kosong.")

    while True:
        topik = input("Topik: ").strip()
        if topik:
            break
        print("Topik tidak boleh kosong.")

    while True:
        durasi_str = input("Durasi belajar (menit): ").strip()
        if not durasi_str:
            print("Durasi tidak boleh kosong.")
            continue
        try:
            durasi = int(durasi_str)
            if durasi <= 0:
                print("Masukkan durasi positif.")
                continue
            break
        except ValueError:
            print("Masukkan angka bulat untuk durasi (mis. 30).")

    entri = {"mapel": mapel, "topik": topik, "durasi": durasi}
    catatan.append(entri)
    print("Catatan tersimpan.")

def lihat_catatan():
    if not catatan:
        print("Belum ada catatan belajar.")
        return

    print("\n=== Daftar Catatan Belajar ===")
    for i, entri in enumerate(catatan, start=1):
        mapel = entri.get("mapel", "-")
        topik = entri.get("topik", "-")
        durasi = entri.get("durasi", 0)
        print(f"{i}. {mapel} - {topik} ({durasi} menit)")

    print(f"Total catatan: {len(catatan)}")

def total_waktu():
    if not catatan:
        print("Belum ada catatan belajar.")
        return

    total = sum(entri.get("durasi", 0) for entri in catatan)
    print(f"Total waktu belajar: {total} menit")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")
    print("5. Kelola Mapel Favorit")
    print("6. Filter per mapel")
    print("7. Target Harian")


def kelola_favorit():
    while True:
        print("\n--- Kelola Mapel Favorit ---")
        print("1. Tambah mapel favorit")
        print("2. Hapus mapel favorit")
        print("3. Lihat mapel favorit")
        print("4. Kembali")
        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            nama = input("Nama mapel yang ingin ditandai favorit: ").strip()
            if not nama:
                print("Nama mapel tidak boleh kosong.")
                continue
            favorit.add(nama)
            print(f"{nama} ditambahkan ke mapel favorit.")

        elif pilihan == "2":
            if not favorit:
                print("Belum ada mapel favorit untuk dihapus.")
                continue
            nama = input("Nama mapel yang ingin dihapus dari favorit: ").strip()
            if nama in favorit:
                favorit.remove(nama)
                print(f"{nama} dihapus dari favorit.")
            else:
                print(f"{nama} tidak ditemukan di daftar favorit.")

        elif pilihan == "3":
            if not favorit:
                print("Belum ada mapel favorit.")
            else:
                print("Mapel favorit:")
                for i, m in enumerate(sorted(favorit), start=1):
                    print(f"{i}. {m}")

        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid")


def filter_per_mapel():
    if not catatan:
        print("Belum ada catatan belajar.")
        return

    # Kumpulkan daftar mapel unik dari catatan
    mapels = sorted({e.get("mapel", "") for e in catatan if e.get("mapel")})
    if not mapels:
        print("Tidak ada mapel yang tersedia di catatan.")
        return

    print("\nDaftar mapel:")
    for i, m in enumerate(mapels, start=1):
        print(f"{i}. {m}")

    pilihan = input("Pilih nomor mapel atau ketik nama mapel: ").strip()

    # Coba interpretasi sebagai nomor
    target = None
    if pilihan.isdigit():
        idx = int(pilihan) - 1
        if 0 <= idx < len(mapels):
            target = mapels[idx]
        else:
            print("Nomor tidak valid.")
            return
    else:
        # ambil nama seperti yang diketik (case-sensitive sederhana)
        if pilihan in mapels:
            target = pilihan
        else:
            print("Nama mapel tidak ditemukan.")
            return

    # Filter dan tampilkan entri untuk mapel yang dipilih
    hasil = [e for e in catatan if e.get("mapel") == target]
    if not hasil:
        print(f"Tidak ada catatan untuk mapel {target}.")
        return

    print(f"\nCatatan untuk mapel: {target}")
    total_menit = 0
    for i, e in enumerate(hasil, start=1):
        topik = e.get("topik", "-")
        durasi = e.get("durasi", 0)
        total_menit += durasi
        print(f"{i}. {target} - {topik} ({durasi} menit)")

    print(f"Jumlah catatan: {len(hasil)}")
    print(f"Total waktu untuk {target}: {total_menit} menit")


def set_target_harian():
    global target_harian
    while True:
        print("\n--- Target Harian ---")
        print("1. Set target harian")
        print("2. Lihat target saat ini")
        print("3. Hapus target")
        print("4. Kembali")
        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            nilai = input("Masukkan target harian (menit): ").strip()
            if not nilai:
                print("Input kosong.")
                continue
            try:
                menit = int(nilai)
                if menit <= 0:
                    print("Masukkan angka positif.")
                    continue
                target_harian = menit
                print(f"Target harian diset: {target_harian} menit")
            except ValueError:
                print("Masukkan angka bulat untuk menit.")

        elif pilihan == "2":
            if target_harian is None:
                print("Belum ada target harian.")
            else:
                print(f"Target harian saat ini: {target_harian} menit")

        elif pilihan == "3":
            if target_harian is None:
                print("Belum ada target untuk dihapus.")
            else:
                target_harian = None
                print("Target harian dihapus.")

        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    elif pilihan == "5":
        kelola_favorit()
    elif pilihan == "6":
        filter_per_mapel()
    elif pilihan == "7":
        set_target_harian()
    else:
        print("Pilihan tidak valid")