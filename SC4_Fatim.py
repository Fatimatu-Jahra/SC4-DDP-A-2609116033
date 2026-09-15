data_buku = {
    "buku1"   : {
    "judul"   : "Cinta Brontosaurus",
    "penulis" : "Raditya Dika",
    "tahun terbit" : 2005
    },
    "buku2"   : {
    "judul"   : "Marmut Merah Jambu",
    "penulis" : "Raditya Dika",
    "tahun terbit" : 2010
    },
    "buku3"   : {
    "judul"   : "Koala Kumal",
    "penulis" : "Raditya Dika",
    "tahun terbit" : 2011
    },
}

while True:
    print("=== MENU ===")
    print("1. Tampilkan Data Buku")
    print("2. Tambahkan Data Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("5. Selesai")

    pilihan = input("Masukkan pilihan (1-4): ")

    if pilihan == "1":
        print(data_buku)

    elif pilihan == "2":
        print("Pilih buku yang ingin ditambahkan penerbitnya:")
        print("1. Buku1")
        print("2. Buku2")
        print("3. Buku3")
        print("4. Tampilkan Data Buku")
        buku_pilihan = input("Masukkan pilihan buku (1-4): ")

        if buku_pilihan == "1":
            penerbit = input("Masukkan nama penerbit untuk Buku1: ")
            data_buku["buku1"]["penerbit"] = penerbit
            print("Data baru buku1 : ", data_buku["buku1"])

        elif buku_pilihan == "2":
            penerbit = input("Masukkan nama penerbit untuk Buku2: ")
            data_buku["buku2"]["penerbit"] = penerbit
            print("Data baru buku2 : ", data_buku["buku2"])

        elif buku_pilihan == "3":
            penerbit = input("Masukkan nama penerbit untuk Buku3: ")
            data_buku["buku3"]["penerbit"] = penerbit
            print("Data baru buku3 : ", data_buku["buku3"])

        elif buku_pilihan == "4":
            print(data_buku)

        else:
            print("Pilihan tidak ditemukan.")

    elif pilihan == "3":
        print("Pilih buku yang ingin diubah penulisnya:")
        print("1. Buku1")
        print("2. Buku2")
        print("3. Buku3")
        print("4. Tampilkan Data Buku")
        buku_pilihan = input("Masukkan pilihan buku (1-4): ")

        if buku_pilihan == "1":
            penulis_baru = input("Masukkan nama penulis baru untuk Buku1: ")
            data_buku["buku1"]["penulis"] = penulis_baru
            print("Data baru buku1 : ", data_buku["buku1"])

        elif buku_pilihan == "2":
            penulis_baru = input("Masukkan nama penulis baru untuk Buku2: ")
            data_buku["buku2"]["penulis"] = penulis_baru
            print("Data baru buku2 : ", data_buku["buku2"])

        elif buku_pilihan == "3":
            penulis_baru = input("Masukkan nama penulis baru untuk Buku3: ")
            data_buku["buku3"]["penulis"] = penulis_baru
            print("Data baru buku3 : ", data_buku["buku3"])

        elif buku_pilihan == "4":
            print(data_buku)

        else:
            print("Pilihan tidak ditemukan.")

    elif pilihan == "4":
        print("Pilih buku yang ingin dihapus penerbitnya:")
        print("1. Buku1")
        print("2. Buku2")
        print("3. Buku3")
        print("4. Tampilkan Data Buku")
        buku_pilihan = input("Masukkan pilihan buku (1-4): ")

        if buku_pilihan == "1":
            if "penerbit" in data_buku["buku1"]:
                del data_buku["buku1"]["penerbit"]
                print("Data baru buku1 : ", data_buku["buku1"])
            else:
                print("Tidak ada penerbit pada Buku1.")

        elif buku_pilihan == "2":
            if "penerbit" in data_buku["buku2"]:
                del data_buku["buku2"]["penerbit"]
                print("Data baru buku2 : ", data_buku["buku2"])
            else:
                print("Tidak ada penerbit pada Buku2.")

        elif buku_pilihan == "3":
            if "penerbit" in data_buku["buku3"]:
                del data_buku["buku3"]["penerbit"]
                print("Data baru buku3 : ", data_buku["buku3"])
            else:
                print("Tidak ada penerbit pada Buku3.")

        elif buku_pilihan == "4":
            print(data_buku)

        else:
            print("Pilihan tidak ditemukan.")

    elif pilihan == "5":
        print("Terima kasih telah menggunakan program ini.")
        break



