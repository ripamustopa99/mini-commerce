import os

data_pengguna = [
    ["admin00@gmail.com", "admin00", "admin00", "admin", [], []],
    ["dira11@gmail.com", "dira", "1111", "user", [], []],
    [
        "bila11@gmail.com",
        "bila",
        "0000",
        "user",
        [["celana", 100000, 4], ["topi", 400000, 4]],
        [
            [[["celana", 100000, 4]], 0.2],
            [[["celana", 100000, 4], ["topi", 400000, 4]], 0.2],
        ],
    ],
]


data_produk = [
    ["kemeja", 100000, 9, 2],
    ["baju croptop", 100000, 3, 5],
    ["celana", 100000, 5, 32],
    ["topi", 100000, 50, 7],
    ["jeans", 100000, 18, 50],
    ["kaos", 150000, 140, 0],
    ["kerudung", 80000, 40, 0],
]
diskon, min_pembelian, pendapatan, logout = 0.2, 500000, 1920000, False


# ================================================================================================================
# ripa
def cls():
    os.system("cls" if os.name == "nt" else "clear")


def cek_input(pesan):
    while True:
        data = input(pesan)
        if data.isdigit():  # untuk nge cek apakah string angka atau bukan
            return int(data)
        elif not data:
            return
        else:
            print("Hanya Boleh Angka Saja yang dimasukan!!")


def hapus(akses, data_arr):
    while True:
        print("-" * 50, "\nTekan ENTER untuk kembali...")
        if data_arr == []:
            input(f" Data {akses} masih kosong!")
            return
        pilih = cek_input("Pilih NO yang mau di hapus! : ")
        if not pilih:
            return
        elif pilih > len(data_arr):
            print("NO yang dimasukan tidak valid!..")
            continue
        del data_arr[pilih - 1]
        input(f"Data {akses} berhasil di hapus!\n Tekan ENTER untuk kembali...")
        return


def ubah_jumlah(akses, data_arr):
    while True:
        print("-" * 50)
        if data_arr == []:
            input(f"Data {akses} masih kosong!\n Tekan ENTER untuk kembali...")
            return
        pilih = cek_input(
            f" Tekan ENTER untuk kembali...\nPilih NO {akses} yang mau di ubah! : "
        )
        if not pilih:
            return
        elif pilih > len(data_arr):
            print("NO yang dimasukan tidak valid!..")
            continue
        jumlah_baru = cek_input(f"Masukan {akses} baru! : ")
        if not jumlah_baru:
            return
        pilih = pilih - 1
        if akses == "jumlah beli":
            cek_stok = 0
            for i, nl in enumerate(data_produk):
                if data_arr[pilih][0] == nl[0]:
                    if jumlah_baru > nl[2]:
                        cek_stok = i
            if cek_stok:
                input(
                    f" Stok hanya tersedia ({data_produk[cek_stok][2]}) !\nTekan ENTER untuk kembali... "
                )
                continue
        data_arr[pilih][2] = jumlah_baru
        input(f"Data {akses} berhasil diubah!\n Tekan ENTER untuk kembali...")
        return


# zek
def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j][3] < data[j + 1][3]:
                data[j], data[j + 1] = data[j + 1], data[j]


def list_produk():
    print("DAFTAR PRODUK")
    bubble_sort(data_produk)
    if data_produk:
        print(
            f"{"NO":<4}{"NAMA PRODUK":<20}{"HARGA":<15}{"STOK":<6}{"TERJUAL":^10}RATING"
        )
        print("-" * 62)
        for i, nl in enumerate(data_produk):
            harga = f"{nl[1]:,}"
            stok = "habis" if nl[2] == 0 else nl[2]
            rekomendasi = f"{"⭐⭐⭐"if nl[3] > 50 else "⭐⭐" if nl[3] > 30 else "⭐"if nl[3] > 10 else ""}"
            print(f"{i+1:<4}{nl[0]:<20}Rp.{harga:<12}{stok:<6}{nl[3]:^10}{rekomendasi}")
    else:
        print("Data produk tidak tersedia!")


# ================================================================================================================
# ripa
def struk(data_transaksi, pilih):
    cls()
    print("=" * 45)
    print(f"{"MINI COMMCERCE":^45}\n{"Jl. Jayaraga No. 123, Garut Kota":^45}")
    print("-" * 45)
    print(f"No Pesanan         : {pilih}\nMetode Pembayaran  : COD")
    print("-" * 45)
    print(f"{"Produk":<18}{"Jumlah":^7}{"Harga":10}{"Total":<15}")
    print("-" * 45)
    for nl in data_transaksi[0]:
        print(f"{nl[0]:<18}{nl[2]:<7}{nl[1]:<10}{nl[2]*nl[1]:,}")
    print("-" * 45)
    subtotal = 0
    for nl in data_transaksi[0]:
        subtotal += nl[2] * nl[1]
    print(f"Sub total                   Rp. {subtotal:,.2f}")
    s_diskon = subtotal * data_transaksi[1]
    print(f"Diskon {data_transaksi[1]*100:.0f}%                 -Rp. {s_diskon:,.2f}")
    print(f"TOTAL BAYAR                 Rp. {subtotal-s_diskon:,.2f}")
    print("-" * 45)
    print(
        f"{"Simpan bukti pembayaran ini sebagai":^45}\n{"syarat klaim garansi/retur":^45}"
    )
    print("=" * 45)
    input("Tekan ENTER untuk kembali...")
    return


def riwayat_transaksi(data_transaksi):
    while True:
        if data_transaksi == []:
            print("-" * 50)
            input("Riwayat transaksi kosong!\n Tekan ENTER untuk kembali...")
            return
        cls()
        print("\nRIWAYAT TRANSAKSI")
        print("=" * 50)
        for i, nl_baris in enumerate(data_transaksi):
            print(
                f"{i + 1}  {nl_baris[0][0][0]:<25} {nl_baris[0][0][2]} pcs dan {len(nl_baris[0])-1} lainnya."
            )
            total_awal = 0
            for nl in nl_baris[0]:
                total_awal += nl[1] * nl[2]
                b_diskon = total_awal * nl_baris[1]
            print(f"   Rp. {total_awal - b_diskon:,.2f}")
            print("-" * 50)
        print("=" * 50)
        pilih = cek_input(" Tekan ENTER untuk kembali...\nPilih untuk lihat struk  : ")
        if not pilih:
            return
        elif pilih > len(data_transaksi) or pilih < 0:
            input("NO tidak valid!")
            continue
        else:
            struk(data_transaksi[pilih - 1], pilih)


def cekout(akses, pilih, jml_beli, y_login):
    global pendapatan
    total_awal = 0
    if akses == "keranjang":
        for nl in y_login[4]:
            subtotal = nl[1] * nl[2]
            total_awal += subtotal
    else:
        total_awal = data_produk[pilih][1] * jml_beli  # harga dikali jumlah beli

    total_akhir = total_awal
    if total_awal > min_pembelian and diskon != 0 / 100:
        ban_diskon = total_awal * diskon
        total_akhir = total_awal - ban_diskon
        print("-" * 50)
        print(f"Total  : {total_awal:,.2f}")
        print(f"Diskon : {ban_diskon:,.2f} => {diskon*100:,.0f}%")
    print("-" * 50)
    print(f"Total uang yang harus di bayar : Rp.{total_akhir:,.2f}\n")
    while True:
        cekout = input("Apakah anda yakin ? (ya/no)    : ")
        if not cekout:
            continue
        if cekout == "no":
            return
        if cekout == "ya":
            if akses == "keranjang":
                for nl_baris in y_login[4]:
                    for nl in data_produk:
                        if nl[0] == nl_baris[0]:
                            nl[3] += nl_baris[2]
                            nl[2] -= nl_baris[2]
                y_login[5].append([y_login[4], diskon])
                y_login[4] = []
            else:
                data_produk[pilih][2] -= jml_beli
                data_produk[pilih][3] += jml_beli
                y_login[5].append(
                    [[[data_produk[pilih][0], data_produk[pilih][1], jml_beli]], diskon]
                )
            pendapatan += total_akhir
            print("Pembelian berhasil!")
            input(" Tekan ENTER untuk kembali..")
            return


# zek
def keranjang(y_login):  # array pengguna
    while True:
        cls()
        print("\nKERANJANG")
        print("-" * 50)
        if y_login[4] == []:
            print("Keranjang masih kosong.")
        total = 0
        for i, nl in enumerate(y_login[4]):  # array data keranjang
            subtotal = nl[1] * nl[2]
            total += subtotal
            rp = f"{nl[1]*nl[2]:,}"
            print(f"{i+1:<4}{nl[0]:<20}{nl[2]:<5}Rp.{rp:<12}")
        print("-" * 50)
        if total != 0:
            cetak_total = f" Rp.{total:,.2f}"
            print(f"Total:{cetak_total:>36}")
        print("\nPILIHAN MENU")
        print("-" * 50)
        print("[1] Cekout [2] Ubah jumlah beli [3] Hapus produk")
        print("-" * 50)
        print("Tekan ENTER untuk kembali...")
        pilih = input("Pilih menu(1-3) : ")
        if not pilih:
            return
        if pilih == "1":
            if y_login[4] == []:
                input(" Keranjang kosong!, Tekan ENTER untuk isi...")
                return
            else:
                cekout("keranjang", "", "", y_login)
        elif pilih == "2":
            ubah_jumlah("jumlah beli", y_login[4])  # data keranjang
        elif pilih == "3":
            hapus("keranjang", y_login[4])


def pilih_produk(akses, y_login):
    print("Tekan ENTER jika ingin kembali...")
    while True:
        pilih = cek_input("Masukan NO produk yang ingin di beli : ")
        if not pilih:
            return
        if pilih > len(data_produk) or pilih < 0:
            print("NO produk tidak valid!")
            continue
        pilih = pilih - 1
        sudah_ada = False
        for nl in y_login[4]:  # data keranjang
            if nl[0] == data_produk[pilih][0]:
                sudah_ada = True
        if sudah_ada and akses == "2":
            print("Produk sudah ada dalam keranjang!")
            continue
        if data_produk[pilih][2] == 0:
            print("Stok produk habis...")
            continue
        jml_beli = cek_input(
            f"Mau beli berapa? stok tersedia({data_produk[pilih][2]:^3})  :"
        )
        if not jml_beli:
            return
        if jml_beli > data_produk[pilih][2] or pilih < 0:
            print(f"Stok hanya tersedia({data_produk[pilih][2]})!")
            continue
        if akses == "1":
            cekout("pilih produk", pilih, jml_beli, y_login)
        else:
            y_login[4].append([data_produk[pilih][0], data_produk[pilih][1], jml_beli])
            input(" Produk berhasil dimasukan!\nTekan ENTER untuk kembali...")
        return


def dasboard_user(y_login):
    global logout
    while True:
        cls()
        print("\n" + "=" * 62)
        print(f"{"Mini Commerce App":^60}")
        print("=" * 62)
        print(f"Selamat datang {y_login[1]},selamat berbelanja!.\n")
        list_produk()
        print("\nPILIHAN MENU")
        print("-" * 62)
        print(
            "[1] Beli sekarang\n[2] Tambahkan keranjang\n[3] Lihat keranjang\n[4] Riwayat Transaksi\n[0] Logout\n"
        )
        pilih = input("Pilih menu (1-4) :")
        if pilih == "0":
            input(f" Sampai jumpa lagi {y_login[1]}\nTekan ENTER untuk kembali...")
            logout = True
            return
        elif pilih == "1":
            pilih_produk("1", y_login)
        elif pilih == "2":
            pilih_produk("2", y_login)
        elif pilih == "3":
            keranjang(y_login)
        elif pilih == "4":
            riwayat_transaksi(y_login[5])  # data transaksi
        else:
            input(" Pilihan tidak valid!\nTekan ENTER...")


# dira
def riwayat_penjualan(data_pengguna):
    while True:
        apakah_kosong = True
        for pengguna in data_pengguna:
            if pengguna[5]:
                apakah_kosong = False
        if apakah_kosong:
            print("-" * 50)
            input("Riwayat penjualan kosong!\n Tekan ENTER untuk kembali...")
            return
        cls()
        print("\nRIWAYAT PENJUALAN")
        print("=" * 50)
        for pengguna in data_pengguna:
            if pengguna[0] == "admin00@gmail.com":
                continue
            if not pengguna[5]:
                continue
            print(f" {pengguna[1]}")
            print("-" * 50)
            for i, nl_baris in enumerate(pengguna[5]):  # artinya data transaksi
                print(
                    f"{i + 1}  {nl_baris[0][0][0]:<23} {nl_baris[0][0][2]} pcs dan {len(nl_baris[0])-1} lainnya."
                )
                total_awal = 0
                for nl in nl_baris[0]:
                    total_awal += nl[1] * nl[2]
                    b_diskon = total_awal * nl_baris[1]  # besar diskon
                print(f"   Rp. {total_awal - b_diskon:,.2f}")
                print("-" * 50)
        print("=" * 50)
        input("Tekan ENTER untuk kembali...")
        return


def kelola_diskon():
    global diskon, min_pembelian
    while True:
        print("-" * 62)
        print(f"\nDiskon saat ini  : {diskon * 100:.0f}%")
        print(f"Minimal Pembelian: {min_pembelian:,}")
        print("-" * 62)
        pilih = input("Tekan [1] untuk ubah : ")
        if not pilih:
            return
        elif pilih == "1":
            print("-" * 62, "\n Tekan ENTER jika tidak ingin di ubah!")
            diskon_b = cek_input(f"Masukan diskon baru ({diskon * 100:.0f}%) : ")
            if not diskon_b:
                return
            min_p = cek_input(f"Minimal Pembelian ({min_pembelian:,}): ")
            if not min_p:
                min_p = 0
            diskon = diskon_b / 100
            min_pembelian = min_p
            print("-" * 62)
            input("Diskon Berhasil Di Ubah!!\n Tekan ENTER untuk kembali...")
            return
        else:
            input(" Pilihan tidak valid, Tekan ENTER...")


def edit_produk():
    while True:
        print("-" * 62, "\nTekan ENTER jika tidak ingin di edit!")
        no_p = cek_input("Masukan No Berapa yang mau di edit : ")

        if not no_p:
            return
        nama_p = input(f"Masukan Nama Produk Baru ({data_produk[no_p - 1][0]}) : ")
        if not nama_p:
            nama_p = data_produk[no_p - 1][0]
        harga_p = cek_input(f"Masukan Harga Baru ({data_produk[no_p - 1][1]:,}) : ")
        if not harga_p:
            harga_p = data_produk[no_p - 1][1]
        stok_p = cek_input(f"Masukan Stok Baru ({data_produk[no_p - 1][2]}) : ")
        if not stok_p:
            stok_p = data_produk[no_p - 1][2]
        data_produk[no_p - 1][0] = nama_p
        data_produk[no_p - 1][1] = harga_p
        data_produk[no_p - 1][2] = stok_p
        print("-" * 62)
        input("Data produk berhasil diubah!\n Tekan ENTER untuk kembali...")
        return


def tambah_produk():
    print("-" * 62)
    while True:
        nama_p = input(
            " Tekan ENTER sebelum isi untuk kembali...\nMasukan Nama Produk : "
        )
        if not nama_p:
            return
        sudah_ada = False
        for nl in data_produk:
            if nama_p == nl[0]:
                sudah_ada = True
                break
        if sudah_ada:
            print("Produk Sudah Ada!")
            continue
        harga_p = cek_input("Masukan Harga : ")
        stok_p = cek_input("Masukan Stok : ")
        data_produk.append(
            [nama_p, harga_p if harga_p else 0, stok_p if stok_p else 0, 0]
        )
        input("Produk Baru Berhasil Di tambahkan!!\nTekan ENTER untuk kembali...")
        return


def kelola_produk():
    while True:
        cls()
        print("=" * 62)
        print(f"{"Kelola Produk":^62}")
        print("=" * 62)
        notif()
        list_produk()
        print("PILIHAN MENU")
        print("-" * 62)
        print(
            "[1] Tambah Produk [2] Edit produk [3] Edit stok [4] Hapus\n\nTekan ENTER untuk kembali..."
        )
        pilih = input("Pilih menu (1-4) : ")
        if not pilih:
            return
        elif pilih == "1":
            tambah_produk()
        elif pilih == "2":
            edit_produk()
        elif pilih == "3":
            ubah_jumlah("stok", data_produk)
        elif pilih == "4":
            hapus("produk", data_produk)
        else:
            input(" Pilihan tidak valid, Tekan ENTER...")


# bila
def notif():
    stok_habis = []
    for nl in data_produk:
        if nl[2] < 5:
            stok_habis.append(nl)
    if stok_habis:
        print("-" * 62)
        print(
            f"NOTIFIKASI: {stok_habis[0][0]} sisa ({stok_habis[0][2]}) dan {len(stok_habis)-1} lainnya!"
        )
        print("-" * 62)


def dasboard_admin(y_login):
    global logout
    while True:
        cls()
        print("\n" + "=" * 62)
        print(f"{"Mini Commerce App":^60}")
        print("=" * 62)
        notif()
        print(f"Selamat datang {y_login[1]},selamat bekerja!.")
        uang = f"{pendapatan:,.2f}"
        dsk = f"{diskon*100:,.0f}%"
        print("    ________________    _______________    _______________")
        print("   |                |  |               |  |               |")
        print(f"   | {uang:^15}|  |{dsk:^15}|  |{len(data_pengguna)-1:^15}|")
        print("   |   Pendapatan   |  |     Diskon    |  |    Pengguna   |")
        print("   |________________|  |_______________|  |_______________|")
        print("\nPILIHAN MENU")
        print("-" * 62)
        print(
            "[1] Kelola produk\n[2] Kelola diskon\n[3] Riwayat Transaksi\n[0] Logout\n"
        )
        pilih = input("Pilih menu (0-3) : ")
        if pilih == "0":
            input(f" Sampai jumpa lagi {y_login[1]}!\nTekan ENTER untuk kembali...")
            logout = True
            return
        elif pilih == "1":
            kelola_produk()
        elif pilih == "2":
            kelola_diskon()
        elif pilih == "3":
            riwayat_penjualan(data_pengguna)
        else:
            input(" Pilihan tidak valid, Tekan ENTER...")


def registrasi():
    while True:
        cls()
        print(f"{"Tekan ENTER sebelum input jika ingin kembali...":^50}")
        print("     --------- Registrasi Pengguna Baru ---------")
        email = input("\nMasukkan Email Anda       : ")
        if not email:
            return
        elif len(email) < 9 or not ("@" in email and "." in email):
            input(" Email tidak valid!, Tekan ENTER...")
            continue
        username = input("Username (min 4 karakter) : ")
        if len(username) < 4:
            input(" Username min 4 karakter!, Tekan ENTER...")
            continue
        password = input("Password (min 4 karakter) : ")
        if len(password) < 4:
            input(" Password min 4 karakter!, Tekan ENTER...")
            continue
        konfir_password = input("Konfirmasi Password       : ")
        if password != konfir_password:
            input(" Password tidak sama!, Tekan ENTER...")
            continue
        sudah_ada = False
        for nl in data_pengguna:
            if nl[0] == email or nl[1] == username:
                sudah_ada = True
                break
        if sudah_ada:
            input("\n Email atau Username sudah terdaftar!, Tekan ENTER...")
            continue
        data_pengguna.append([email, username, password, "user", [], []])
        input(f"\n {username} berhasil registrasi!\nTekan ENTER untuk kembali...")
        return


def login():
    login_gagal = 0
    while True:
        cls()
        print("Tekan ENTER sebelum input jika ingin kembali...")
        print("\n     ------ Halaman Login ------")
        masuk = input("Username/Email : ")
        if not masuk:
            return
        password = input("Password       : ")
        if not password:
            input("\n Password tidak boleh kosong, Tekan ENTER...")
            continue
        y_login = None
        for nl in data_pengguna:
            if (nl[0] == masuk or nl[1] == masuk) and nl[2] == password:
                y_login = nl
                break
        if y_login:
            if y_login[3] == "admin":
                dasboard_admin(y_login)
            else:
                dasboard_user(y_login)
            if logout:
                return
            login_gagal = 0
        else:
            login_gagal += 1
            if login_gagal < 3:
                input("\n Username atau password salah, Tekan ENTER...")
            else:
                input(" Anda sudah gagal tiga kali!, Tekan Enter untuk kembali...")
                return


def main():
    while True:
        cls()
        print("\n" + "*" * 50)
        print(f"{"Mini Commerce App":^50}")
        print("*" * 50)
        print("=" * 50)
        print(f"|{"MENU UTAMA":^48}|")
        print("=" * 50)
        print("\n[1] Login Pengguna/Admin [2] Registrasi [0] Keluar")
        print("-" * 50)
        pilih = input("Pilih menu (1-3): ")
        if pilih == "1":
            login()
        elif pilih == "2":
            registrasi()
        elif pilih == "0":
            print("\nTerima kasih telah menggunakan aplikasi kami. Sampai jumpa!")
            return
        else:
            input("\n Pilihan tidak valid, Tekan ENTER...")


main()
