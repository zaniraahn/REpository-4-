catatan = []

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
    else:
        print("Pilihan tidak valid")